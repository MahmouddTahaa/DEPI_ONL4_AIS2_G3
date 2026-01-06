import numpy as np
import pytest
import sys
import os

try:
    from core import ArrayUtils
except ModuleNotFoundError:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    from core import ArrayUtils


@pytest.fixture
def rand_shape() -> tuple:
    return (np.random.randint(1, 10), np.random.randint(1, 10))


@pytest.fixture
def rng0() -> np.random.Generator:
    return np.random.default_rng(0)


@pytest.mark.parametrize(
    "mode,expected_fn",
    [
        ("zeros", lambda s: np.zeros(shape=s)),
        ("ones", lambda s: np.ones(shape=s)),
        ("eye", lambda s: np.eye(N=s[0], M=s[1])),
        ("identity", lambda s: np.eye(N=s[0], M=s[1])),
    ],
)
def test_smart_array_generator_deterministic_modes(mode, expected_fn, rand_shape):
    expected = expected_fn(rand_shape)
    result = ArrayUtils.smart_array_generator(mode=mode, shape=rand_shape)
    assert np.array_equal(result, expected), f"{expected} should equal {result}"


def test_smart_array_generator_random_with_rng(rand_shape, rng0):
    expected = np.random.default_rng(0).integers(low=1, high=100, size=rand_shape)
    result = ArrayUtils.smart_array_generator(
        mode="random", shape=rand_shape, low=1, high=100, rng=np.random.default_rng(0)
    )
    assert np.array_equal(result, expected)


def test_smart_array_generator_random_without_rng(rand_shape):
    result = ArrayUtils.smart_array_generator(
        mode="random", shape=rand_shape, low=5, high=15
    )
    assert result.shape == rand_shape
    assert np.all(result >= 5) and np.all(result < 15)


def test_smart_array_generator_invalid_mode(rand_shape):
    with pytest.raises(ValueError) as excinfo:
        ArrayUtils.smart_array_generator(mode="invalid_mode", shape=rand_shape)
    assert "Invalid Mode, Please Try Again" in str(excinfo.value)


def test_smart_array_generator_shape_validation():
    with pytest.raises(ValueError):
        ArrayUtils.smart_array_generator(mode="zeros", shape=(-3, 4))
    with pytest.raises(TypeError):
        ArrayUtils.smart_array_generator(mode="ones", shape=(3.5, 4.2))


def test_smart_array_generator_large_shape():
    shape = (1000, 1000)
    result = ArrayUtils.smart_array_generator(mode="zeros", shape=shape)
    expected = np.zeros(shape=shape)
    assert np.array_equal(result, expected), "Large zero array should equal expected"


def test_apply_threshold_numeric_array(rand_shape):
    rng = np.random.default_rng(0)
    arr = rng.random(size=rand_shape)
    result = ArrayUtils.apply_threshold(arr, threshold=0.6, replacement_value=-1)
    expected = np.where(arr >= 0.6, -1, arr)
    assert np.array_equal(result, expected)


def test_apply_threshold_mixed_and_non_comparable():
    invalid_arr = [["a", "b"], ["c", "d"]]
    result = ArrayUtils.apply_threshold(
        invalid_arr, threshold=0.5, replacement_value=-1
    )
    assert np.array_equal(result, invalid_arr), f"{invalid_arr} should equal {result}"

    arr_mixed = np.array([1, 2, "a", 4])
    result_mixed = ArrayUtils.apply_threshold(
        arr_mixed, threshold=2, replacement_value=-1
    )
    assert np.array_equal(
        result_mixed, arr_mixed
    ), f"{arr_mixed} should equal {result_mixed}"


def test_apply_threshold_mixed_numeric_types():
    arr = np.array([1, 2, 3.5, 4])
    result = ArrayUtils.apply_threshold(arr, threshold=3, replacement_value=-1)
    expected = np.where(arr >= 3, -1, arr)
    assert np.array_equal(result, expected)


def test_apply_threshold_no_and_all_replacements():
    arr = np.array([1, 2, 3, 4, 5])
    res_no = ArrayUtils.apply_threshold(arr, threshold=10, replacement_value=-1)
    assert np.array_equal(res_no, arr)

    res_all = ArrayUtils.apply_threshold(arr, threshold=0, replacement_value=-1)
    expected_all = np.full(arr.shape, -1)
    assert np.array_equal(res_all, expected_all)


def test_apply_threshold_negative_replacement():
    arr = np.array([1, 2, 3, 4, 5])
    result = ArrayUtils.apply_threshold(arr, threshold=3, replacement_value=-5)
    expected = np.where(arr >= 3, -5, arr)
    assert np.array_equal(result, expected)


def test_apply_threshold_empty_and_nan():
    empty = np.array([])
    result_empty = ArrayUtils.apply_threshold(empty, threshold=1, replacement_value=-1)
    assert np.array_equal(result_empty, empty), "Empty array should equal result"

    arr_nan = np.array([1, 2, np.nan, 4, 5])
    result_nan = ArrayUtils.apply_threshold(arr_nan, threshold=3, replacement_value=-1)
    expected_nan = np.where(arr_nan >= 3, -1, arr_nan)
    assert np.array_equal(result_nan, expected_nan, equal_nan=True)


def test_secure_reshape_and_stack_valid_inputs():
    data1 = np.array([[1, 2], [3, 4], [5, 6]])
    data2 = np.array([[7, 8, 9], [9, 10, 11]])
    new_shape = (2, 3)

    result = ArrayUtils.secure_reshape_and_stack(data1, data2, new_shape)
    expected_data1 = data1.reshape(new_shape)
    expected = np.vstack((expected_data1, data2))

    assert np.array_equal(result, expected), f"{expected} should equal {result}"


def test_secure_reshape_and_stack_invalid_reshape():
    data1 = np.array([[1, 2], [3, 4], [5, 6]])
    data2 = np.array([[7, 8], [9, 10]])
    new_shape = (4, 2)

    with pytest.raises(ValueError) as excinfo:
        ArrayUtils.secure_reshape_and_stack(data1, data2, new_shape)
    assert "Invalid input data or reshape operation" in str(excinfo.value)


def test_secure_reshape_and_stack_column_mismatch():
    data1 = np.array([[1, 2], [3, 4], [5, 6]])
    data2 = np.array([[7, 8, 9], [10, 11, 12]])
    new_shape = (3, 2)

    with pytest.raises(ValueError) as excinfo:
        ArrayUtils.secure_reshape_and_stack(data1, data2, new_shape)
    assert (
        "Both matrices must have the same number of columns for vertical stacking."
        in str(excinfo.value)
    )


def test_secure_reshape_and_stack_non_array_inputs():
    data1 = [[1, 2], [3, 4], [5, 6]]
    data2 = (7, 8), (9, 10)
    new_shape = (3, 2)

    result = ArrayUtils.secure_reshape_and_stack(data1, data2, new_shape)
    expected_data1 = np.array(data1).reshape(new_shape)
    expected_data2 = np.array(data2)
    expected = np.vstack((expected_data1, expected_data2))

    assert np.array_equal(result, expected), f"{expected} should equal {result}"


def test_secure_reshape_and_stack_1d_data2():
    data1 = np.array([[1, 2], [3, 4], [5, 6]])
    data2 = np.array([7, 8])
    new_shape = (3, 2)

    result = ArrayUtils.secure_reshape_and_stack(data1, data2, new_shape)
    expected_data1 = data1.reshape(new_shape)
    expected_data2 = data2.reshape(-1, 2)
    expected = np.vstack((expected_data1, expected_data2))

    assert np.array_equal(result, expected), f"{expected} should equal {result}"

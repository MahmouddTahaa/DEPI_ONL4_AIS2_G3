"""A module containing the ArrayUtils class with static methods for array manipulation"""

import numpy as np
from typing import Any, Optional


class ArrayUtils:
    """A collection of static methods for array manipulations using NumPy."""

    @staticmethod
    def smart_array_generator(
        mode: str,
        shape: tuple,
        low: int = 0,
        high: int = 10,
        rng: Optional[np.random.Generator] = None,
    ) -> np.ndarray:
        """
        Generates different types of NumPy arrays based on the specified mode.

        :param mode: Different modes for array generation ("zeros", "ones", "random", "identity"/"eye")
        :type mode: str
        :param shape: Shape of the desired array
        :type shape: tuple
        :param low: Lower bound for random integer generation
        :type low: int
        :param high: Upper bound for random integer generation
        :type high: int
        :param rng: Random number generator instance
        :type rng: Optional[np.random.Generator]
        :return: Generated NumPy array
        :rtype: ndarray[_AnyShape, dtype[Any]]
        """

        if mode.lower() == "zeros":
            return np.zeros(shape=shape)
        elif mode.lower() == "ones":
            return np.ones(shape=shape)
        elif mode.lower() == "random":
            if rng is None:
                rng = np.random.default_rng()
            return rng.integers(low=low, high=high, size=shape)
        elif mode.lower() == "identity" or mode.lower() == "eye":
            try:
                return np.eye(N=shape[0], M=shape[1])
            except Exception as e:
                print(f"An Error Occured: {e}")
                return np.array([])
        else:
            raise ValueError("Invalid Mode, Please Try Again")

    @staticmethod
    def apply_threshold(
        arr: Any, threshold: float, replacement_value: float
    ) -> np.ndarray:
        """
        A method that replaces elements in an array based on a threshold.

        :param arr: Input array-like structure
        :type arr: Any
        :param threshold: Threshold value for comparison
        :type threshold: float
        :param replacement_value: Value to replace elements that meet the condition
        :type replacement_value: float
        :return: Array with replaced elements
        :rtype: np.ndarray
        """

        new_arr = arr

        try:
            arr = np.array(arr)
        except ValueError as ve:
            print(f"Something went wrong with parameter `arr`: {ve}")
            return new_arr
        else:
            try:
                cond = arr >= threshold
                new_arr = np.where(cond, replacement_value, arr)

            except Exception as e:
                print(f"Input array contains non comparable elements:\n{e}")

            return new_arr

    @staticmethod
    def secure_reshape_and_stack(
        data1: Any, data2: Any, new_shape: tuple
    ) -> np.ndarray:
        """
        Reshapes the first dataset to the specified shape and vertically stacks it with the second dataset.

        :param data1: First dataset to be reshaped and stacked
        :type data1: Any
        :param data2: Second dataset to be stacked
        :type data2: Any
        :param new_shape: Desired shape for the first dataset
        :type new_shape: tuple
        :return: Vertically stacked NumPy array
        :rtype: np.ndarray
        """

        try:
            arr1 = np.asarray(data1)
            arr2 = np.asarray(data2)
            if arr2.ndim == 1:
                arr2 = arr2.reshape(-1, arr2.shape[0])

            if len(new_shape) != 2:
                raise ValueError("new_shape must be a 2D shape (rows, columns)")

            reshaped_arr1 = arr1.reshape(new_shape)

        except (TypeError, ValueError) as e:
            raise ValueError("Invalid input data or reshape operation") from e

        if reshaped_arr1.shape[1] != arr2.shape[1]:  # type: ignore
            raise ValueError(
                "Both matrices must have the same number of columns for vertical stacking."
            )

        return np.vstack([reshaped_arr1, arr2])

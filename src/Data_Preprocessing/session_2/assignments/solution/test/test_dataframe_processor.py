import pandas as pd
import sys
import os

try:
    from core import DataframeProcessor
except ModuleNotFoundError:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    from core import DataframeProcessor


def test_automated_stat_analyzer_numerical():
    data = {
        "customer_age": [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    }
    df = pd.DataFrame(data)
    processor = DataframeProcessor(df)

    result = processor.automated_stat_analyzer("customer_age", skip_plot=True)

    assert "Mean" in result
    assert "Median" in result
    assert "Skew" in result
    assert "Skewness" in result


def test_automated_stat_analyzer_categorical():
    data = {
        "customer_name": ["Alice", "Bob", "Charlie", "Alice", "Bob", "Alice"],
    }
    df = pd.DataFrame(data)
    processor = DataframeProcessor(df)

    result = processor.automated_stat_analyzer("customer_name", skip_plot=True)

    assert "Mode" in result
    assert result["Mode"] == "Alice"


def test_null_handler_mean():
    data = {
        "customer_age": [25, 30, None, 40, 45, None, 55, 60, 65, 70],
    }
    df = pd.DataFrame(data)
    processor = DataframeProcessor(df)

    processed_df = processor.handle_null_values("customer_age")

    assert processed_df["customer_age"].isnull().sum() == 0
    assert processed_df["customer_age"].iloc[2] == 48.75
    assert processed_df["customer_age"].iloc[5] == 48.75


def test_null_handler_median():
    data = {
        "customer_age": [25, 30, 1000, 40, 45, None, 55, 60, 65, 70],
    }
    df = pd.DataFrame(data)
    processor = DataframeProcessor(df)

    processed_df = processor.handle_null_values("customer_age")

    assert processed_df["customer_age"].isnull().sum() == 0
    assert processed_df["customer_age"].iloc[5] == 55


def test_null_handler_mode():
    data = {
        "letters": ["A", "B", "A", None, "C", None, "A"],
    }
    df = pd.DataFrame(data)
    processor = DataframeProcessor(df)

    processed_df = processor.handle_null_values("letters")

    assert processed_df["letters"].isnull().sum() == 0
    assert processed_df["letters"].iloc[5] == "A"
    assert processed_df["letters"].iloc[3] == "A"


def test_null_handler_no_nulls():
    data = {
        "customer_age": [25, 30, 35, 40, 45],
    }
    df = pd.DataFrame(data)
    processor = DataframeProcessor(df)

    processed_df = processor.handle_null_values("customer_age")

    assert processed_df.equals(df)

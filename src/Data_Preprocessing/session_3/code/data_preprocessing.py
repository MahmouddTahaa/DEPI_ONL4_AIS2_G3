import pandas as pd
from typing import Tuple
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def to_cat(df: pd.DataFrame, columns) -> pd.DataFrame:
    return df[columns].astype("category")


def check_types(df: pd.DataFrame) -> pd.DataFrame:
    dtypes = df.dtypes
    n_unique = df.nunique()

    return pd.DataFrame({"dtype": dtypes, "num_unique": n_unique})


def calculate_null_val_percentages(df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "null_percentage": df.isnull().sum().sort_values(ascending=False)
            / df.shape[0],
        }
    )


def check_null_values(df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({"no_of_nulls": df.isnull().sum().sort_values(ascending=False)})


def replace_null_with_median(df: pd.DataFrame, column: str) -> None:
    df[column].fillna(df[column].median(), inplace=True)


def find_quartiles(df: pd.DataFrame, column: str) -> Tuple[float, ...]:
    q1 = df[column].quantile(0.25)
    median = df[column].quantile(0.50)
    q3 = df[column].quantile(0.75)

    return q1, median, q3


def find_upper_lower_bounds(df: pd.DataFrame, column: str) -> Tuple[float, ...]:
    q1, _, q3 = find_quartiles(df, column)
    iqr = q3 - q1

    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)

    return lower_bound, upper_bound


def eliminate_outliers(df: pd.DataFrame) -> None:
    for col in df.select_dtypes(include=["number"]).columns:
        lower_bound, upper_bound = find_upper_lower_bounds(df, col)
        filter = (df[col] > upper_bound) | (df[col] < lower_bound)
        df = df[~filter]


def replace_outliers_with_upper_lower(df: pd.DataFrame) -> None:
    for col in df.select_dtypes(include=["number"]).columns:
        lower_bound, upper_bound = find_upper_lower_bounds(df, col)
        lower_outliers = df[col] < lower_bound
        upper_outliers = df[col] < lower_bound
        df[col].replace(lower_outliers, lower_bound, inplace=True)
        df[col].replace(upper_outliers, upper_bound, inplace=True)


def visualize_histograms(df: pd.DataFrame) -> None:
    numerical_cols = df.select_dtypes("number").columns

    plt.figure(figsize=(12, 2))

    for i, column in enumerate(numerical_cols):
        plt.subplot(1, 2, i + 1)
        plt.hist(df[column], edgecolor="k")
        plt.xlabel(f"{column}")
        plt.ylabel("Frequency")
        plt.title(f"{column} Histogram")

    plt.show()


def visualize_categorical_v2(df: pd.DataFrame) -> None:
    cat_cols = df.select_dtypes("category").columns

    num_cols = len(cat_cols)
    rows = (num_cols // 3) + (1 if num_cols % 3 != 0 else 0)

    plt.figure(figsize=(20, 5 * rows))

    for i, column in enumerate(cat_cols):
        plt.subplot(rows, 3, i + 1)
        plt.pie(
            df[column].value_counts(),
            labels=df[column].value_counts().index,
            startangle=140,
            autopct="%1.1f%%",
            explode=[0.1 for i in range(df[column].nunique())],
        )
        plt.xlabel(f"{column}")
        plt.ylabel("Frequency")
        plt.title(f"{column} Distribution")

    plt.tight_layout()
    plt.show()

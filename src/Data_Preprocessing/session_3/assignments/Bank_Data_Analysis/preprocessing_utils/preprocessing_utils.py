import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def check_types(df: pd.DataFrame) -> pd.DataFrame:
    dtypes = df.dtypes
    n_unique = df.nunique()

    return pd.DataFrame({"dtype": dtypes, "num_unique": n_unique})


def check_null_values(df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({"no_of_nulls": df.isnull().sum().sort_values(ascending=False)})


def calculate_null_val_percentages(df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "null_percentage": df.isnull().sum().sort_values(ascending=False)
            / df.shape[0]
        }
    )


def find_quartiles(df: pd.DataFrame, column: str):
    q1 = df[column].quantile(0.25)
    median = df[column].quantile(0.50)
    q3 = df[column].quantile(0.75)

    return q1, median, q3


def find_upper_lower_bounds(df: pd.DataFrame, column: str):
    q1, _, q3 = find_quartiles(df, column)
    iqr = q3 - q1

    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)

    return lower_bound, upper_bound


def visualize_histograms(df: pd.DataFrame) -> None:
    numerical_cols = df.select_dtypes("number").columns
    num_cols_list = list(numerical_cols)
    num_plots = len(num_cols_list)
    rows = (num_plots // 3) + (1 if num_plots % 3 != 0 else 0)

    plt.figure(figsize=(18, 5 * rows))

    for i, column in enumerate(num_cols_list):
        plt.subplot(rows, 3, i + 1)
        plt.hist(df[column], edgecolor="k", bins=30)
        plt.xlabel(f"{column}")
        plt.ylabel("Frequency")
        plt.title(f"{column} Histogram")

    plt.tight_layout()
    plt.show()


def visualize_kde(df: pd.DataFrame) -> None:
    numerical_cols = df.select_dtypes("number").columns
    num_cols_list = list(numerical_cols)
    num_plots = len(num_cols_list)
    rows = (num_plots // 3) + (1 if num_plots % 3 != 0 else 0)

    plt.figure(figsize=(18, 5 * rows))

    for i, column in enumerate(num_cols_list):
        plt.subplot(rows, 3, i + 1)
        sns.kdeplot(x=df[column], fill=True)
        plt.xlabel(f"{column}")
        plt.ylabel("Density")
        plt.title(f"{column} KDE Plot")

    plt.tight_layout()
    plt.show()


def visualize_categorical(df: pd.DataFrame) -> None:
    cat_cols = df.select_dtypes("category").columns
    num_cols = len(cat_cols)
    rows = (num_cols // 3) + (1 if num_cols % 3 != 0 else 0)

    plt.figure(figsize=(20, 5 * rows))

    for i, column in enumerate(cat_cols):
        plt.subplot(rows, 3, i + 1)
        sns.countplot(x=column, data=df)
        plt.xlabel(f"{column}")
        plt.ylabel("Count")
        plt.title(f"{column} Count Plot")
        plt.xticks(rotation=45, ha="right")

    plt.tight_layout()
    plt.show()


def visualize_categorical_pie(df: pd.DataFrame) -> None:
    cat_cols = df.select_dtypes("category").columns
    num_cols = len(cat_cols)
    rows = (num_cols // 3) + (1 if num_cols % 3 != 0 else 0)

    plt.figure(figsize=(20, 5 * rows))

    for i, column in enumerate(cat_cols):
        plt.subplot(rows, 3, i + 1)
        value_counts = df[column].value_counts()
        plt.pie(
            value_counts,
            labels=value_counts.index,
            startangle=140,
            autopct="%1.1f%%",
            explode=[0.05 for _ in range(len(value_counts))],
        )
        plt.title(f"{column} Distribution")

    plt.tight_layout()
    plt.show()

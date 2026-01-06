import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scienceplots


def skew_type(df: pd.DataFrame, column_name: str) -> str:
    if df[column_name].skew() > 1:  # type: ignore
        return "Positively Skewed"
    elif df[column_name].skew() < -1:  # type: ignore
        return "Negatively Skewed"

    return "Not Skewed"


def plot_dist(df: pd.DataFrame, column_name: str) -> None:
    with plt.style.context(["science", "notebook", "grid"]):
        sns.histplot(data=df, x=column_name, kde=True)
        plt.xlabel(column_name.replace("_", " ").title())
        plt.ylabel("Frequency")
        plt.title(f"Distribution of {column_name.replace('_', ' ').title()}")
        plt.show()

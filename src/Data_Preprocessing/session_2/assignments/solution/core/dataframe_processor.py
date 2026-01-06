import pandas as pd
import matplotlib.pyplot as plt
from .utils import plot_dist, skew_type


class DataframeProcessor:
    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df

    def automated_stat_analyzer(
        self, column_name: str, skip_plot: bool = False
    ) -> dict:
        data_type = self.df[column_name].dtype

        if data_type == "object":
            mode = self.df[column_name].mode()[0]
            if not skip_plot:
                plot_dist(self.df, column_name)
            return {"Mode": mode}

        if data_type == "int" or data_type == "float":
            mean = float(self.df[column_name].mean())
            median = float(self.df[column_name].median())
            skewness = float(self.df[column_name].skew())  # type: ignore
            if not skip_plot:
                plot_dist(self.df, column_name)

            return {
                "Mean": mean,
                "Median": median,
                "Skew": skew_type(self.df, column_name),
                "Skewness": skewness,
            }

        return {"Error": "Data type not supported"}

    def handle_null_values(self, column_name: str) -> pd.DataFrame:
        if self.df[column_name].dtype == "object":
            mode_value = self.df[column_name].mode()[0]
            self.df[column_name].fillna(mode_value, inplace=True)
            print(f"Null values filled with mode: {mode_value}")
            return self.df
        else:
            if self.df[column_name].isnull().sum() == 0:
                print("No null values found.")
                return self.df

            Q1 = self.df[column_name].quantile(0.25)
            Q3 = self.df[column_name].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            outliers = self.df[
                (self.df[column_name] < lower_bound)
                | (self.df[column_name] > upper_bound)
            ]

            if not outliers.empty:
                median_value = self.df[column_name].median()
                self.df[column_name].fillna(median_value, inplace=True)
                print(
                    f"Outliers detected. Null values filled with median: {median_value}"
                )
                return self.df

            else:
                mean_value = self.df[column_name].mean()
                self.df[column_name].fillna(mean_value, inplace=True)
                print(f"Null values filled with mean: {mean_value}")
                return self.df

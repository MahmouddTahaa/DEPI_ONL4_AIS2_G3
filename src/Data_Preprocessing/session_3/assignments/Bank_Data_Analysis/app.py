import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings
import sys

# Add current directory to path to import preprocessing_utils
sys.path.append(str(Path(__file__).parent))
from preprocessing_utils.preprocessing_utils import *

warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="Bank Data Dashboard",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        padding: 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    </style>
""",
    unsafe_allow_html=True,
)


@st.cache_data
def load_data():
    BASE_DIR = Path(__file__).parent.parent
    data_path = BASE_DIR.parents[3] / "Data" / "bank.csv"
    df = pd.read_csv(data_path)
    return df


@st.cache_data
def preprocess_data(df):
    object_cols = df.select_dtypes("object").columns
    df[object_cols] = df[object_cols].astype("category")

    df = df.drop_duplicates()

    return df


def main():
    st.markdown(
        '<h1 class="main-header">🏦 Bank Data Dashboard</h1>', unsafe_allow_html=True
    )
    st.markdown("---")

    df = load_data()
    df = preprocess_data(df)

    st.header("📊 Key Metrics")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Total Records", f"{len(df):,}")
    with col2:
        st.metric("Total Features", len(df.columns))
    with col3:
        st.metric("Numerical Features", len(df.select_dtypes("number").columns))
    with col4:
        st.metric("Categorical Features", len(df.select_dtypes("category").columns))
    with col5:
        missing = df.isnull().sum().sum()
        st.metric("Missing Values", missing if missing > 0 else "✅ None")

    st.markdown("---")

    st.header("📋 Dataset Overview")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Dataset Preview")
        st.dataframe(df.head(10), use_container_width=True)

    with col2:
        st.subheader("Dataset Information")
        st.write(f"**Shape:** {df.shape[0]} rows × {df.shape[1]} columns")
        st.write("**Data Types:**")
        st.dataframe(check_types(df), use_container_width=True)

        st.write("**Missing Values:**")
        null_df = check_null_values(df)
        if null_df["no_of_nulls"].sum() == 0:
            st.success("✅ No missing values found!")
        else:
            st.dataframe(null_df, use_container_width=True)

    st.markdown("---")

    st.header("🎯 Target Variable Distribution")
    target_col = "deposit"
    if target_col in df.columns:
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Count:**")
            st.dataframe(
                df[target_col].value_counts().to_frame(), use_container_width=True
            )
        with col2:
            st.write("**Percentage:**")
            st.dataframe(
                (df[target_col].value_counts(normalize=True) * 100).to_frame(),
                use_container_width=True,
            )

        fig, ax = plt.subplots(1, 2, figsize=(12, 4))
        df[target_col].value_counts().plot(
            kind="bar", ax=ax[0], color=["#1f77b4", "#ff7f0e"]
        )
        ax[0].set_title("Target Variable Count")
        ax[0].set_xlabel("Deposit")
        ax[0].set_ylabel("Count")

        df[target_col].value_counts().plot(
            kind="pie", ax=ax[1], autopct="%1.1f%%", startangle=90
        )
        ax[1].set_title("Target Variable Distribution")
        ax[1].set_ylabel("")

        st.pyplot(fig)
        plt.close()

    st.markdown("---")

    st.header("📈 Statistical Summary")
    st.dataframe(df.describe(), use_container_width=True)

    st.markdown("---")

    st.header("🔢 Numerical Features Analysis")
    numerical_cols = df.select_dtypes("number").columns

    selected_num_col = st.selectbox(
        "Select a numerical column to analyze", numerical_cols, key="num_select"
    )

    col1, col2 = st.columns(2)
    with col1:
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.hist(df[selected_num_col], bins=30, edgecolor="k", color="#1f77b4")
        ax.set_title(f"{selected_num_col} Histogram")
        ax.set_xlabel(selected_num_col)
        ax.set_ylabel("Frequency")
        st.pyplot(fig)
        plt.close()

    with col2:
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.kdeplot(data=df, x=selected_num_col, fill=True, ax=ax)
        ax.set_title(f"{selected_num_col} KDE Plot")
        st.pyplot(fig)
        plt.close()

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(data=df, y=selected_num_col, ax=ax)
    ax.set_title(f"{selected_num_col} Boxplot")
    st.pyplot(fig)
    plt.close()

    st.markdown("---")

    st.header("📊 Categorical Features Analysis")
    categorical_cols = df.select_dtypes("category").columns

    selected_cat_col = st.selectbox(
        "Select a categorical column to analyze", categorical_cols, key="cat_select"
    )

    col1, col2 = st.columns(2)
    with col1:
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.countplot(data=df, x=selected_cat_col, ax=ax)
        ax.set_title(f"{selected_cat_col} Count Plot")
        ax.set_xlabel(selected_cat_col)
        ax.set_ylabel("Count")
        plt.xticks(rotation=45, ha="right")
        st.pyplot(fig)
        plt.close()

    with col2:
        fig, ax = plt.subplots(figsize=(8, 5))
        value_counts = df[selected_cat_col].value_counts()
        ax.pie(
            value_counts, labels=value_counts.index, autopct="%1.1f%%", startangle=90
        )
        ax.set_title(f"{selected_cat_col} Pie Chart")
        st.pyplot(fig)
        plt.close()

    st.markdown("---")

    st.header("🔗 Correlation Analysis")
    numerical_df = df.select_dtypes("number")
    corr = numerical_df.corr()

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(
        corr,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        center=0,
        square=True,
        linewidths=1,
        cbar_kws={"shrink": 0.8},
        ax=ax,
    )
    ax.set_title("Correlation Matrix of Numerical Variables")
    st.pyplot(fig)
    plt.close()

    st.markdown("---")

    st.header("🎯 Feature vs Target Analysis")
    target_col = "deposit"

    feature_type = st.radio(
        "Select feature type", ["Numerical", "Categorical"], horizontal=True
    )

    if feature_type == "Numerical":
        numerical_cols = df.select_dtypes("number").columns
        selected_col = st.selectbox(
            "Select a numerical feature", numerical_cols, key="num_target"
        )

        fig, ax = plt.subplots(figsize=(10, 5))
        sns.boxplot(data=df, x=target_col, y=selected_col, ax=ax)
        ax.set_title(f"{selected_col} vs {target_col}")
        st.pyplot(fig)
        plt.close()

    else:
        categorical_cols = df.select_dtypes("category").columns
        categorical_cols = [col for col in categorical_cols if col != target_col]
        selected_col = st.selectbox(
            "Select a categorical feature", categorical_cols, key="cat_target"
        )

        fig, ax = plt.subplots(figsize=(10, 5))
        crosstab = pd.crosstab(df[selected_col], df[target_col])
        sns.heatmap(crosstab, annot=True, fmt="d", cmap="Blues", ax=ax)
        ax.set_title(f"{selected_col} vs {target_col}")
        st.pyplot(fig)
        plt.close()

    st.markdown("---")

    st.header("📄 Full Dataset")
    st.dataframe(df, use_container_width=True)


if __name__ == "__main__":
    main()

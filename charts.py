import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def histogram_chart(df):
    if "Value" not in df.columns:
        return

    values = df["Value"].dropna()

    if len(values) == 0:
        return

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.hist(values, bins=30)
    ax.set_title("Distribution of Values")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)


def line_chart(df):
    if "Year" not in df.columns or "Value" not in df.columns:
        return

    trend = df.groupby("Year")["Value"].mean().dropna()

    if len(trend) == 0:
        return

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(trend.index, trend.values)
    ax.set_title("Average Value by Year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Average Value")
    st.pyplot(fig)


def scatter_chart(df):
    if "Year" not in df.columns or "Value" not in df.columns:
        return

    sample = df.dropna(subset=["Value"])

    if len(sample) > 5000:
        sample = sample.sample(5000, random_state=42)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.scatter(sample["Year"], sample["Value"], alpha=0.5)
    ax.set_title("Year vs Value")
    ax.set_xlabel("Year")
    ax.set_ylabel("Value")
    st.pyplot(fig)


def area_chart(df):
    if "Year" not in df.columns or "Value" not in df.columns:
        return

    trend = df.groupby("Year")["Value"].mean().dropna()

    if len(trend) == 0:
        return

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.fill_between(trend.index, trend.values)
    ax.set_title("Average Value Over Time")
    ax.set_xlabel("Year")
    ax.set_ylabel("Average Value")
    st.pyplot(fig)


def box_chart(df):
    if "Year" not in df.columns or "Value" not in df.columns:
        return

    sample = df.dropna(subset=["Value"])

    if len(sample) > 10000:
        sample = sample.sample(10000, random_state=42)

    fig, ax = plt.subplots(figsize=(12, 5))
    sns.boxplot(data=sample, x="Year", y="Value", ax=ax)

    ax.set_title("Distribution by Year")
    plt.xticks(rotation=90)

    st.pyplot(fig)


def heatmap_chart(df):
    if (
        "Country Name" not in df.columns
        or "Year" not in df.columns
        or "Value" not in df.columns
    ):
        return

    pivot = df.pivot_table(
        values="Value",
        index="Country Name",
        columns="Year",
        aggfunc="mean"
    )

    if pivot.empty:
        return

    if len(pivot) > 25:
        pivot = pivot.head(25)

    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(
        pivot.fillna(0),
        cmap="viridis",
        ax=ax
    )

    ax.set_title("Country-Year Heatmap")
    st.pyplot(fig)


def bar_chart(df):
    if "Country Name" not in df.columns or "Value" not in df.columns:
        return

    country_avg = (
        df.groupby("Country Name")["Value"]
        .mean()
        .dropna()
        .sort_values(ascending=False)
        .head(15)
    )

    if len(country_avg) == 0:
        return

    fig, ax = plt.subplots(figsize=(10, 6))
    country_avg.sort_values().plot(
        kind="barh",
        ax=ax
    )

    ax.set_title("Top 15 Countries by Average Value")
    ax.set_xlabel("Average Value")
    st.pyplot(fig)


def pie_chart(df):
    if "Indicator Name" not in df.columns:
        return

    counts = (
        df["Indicator Name"]
        .value_counts()
        .head(8)
    )

    if len(counts) == 0:
        return

    fig, ax = plt.subplots(figsize=(7, 7))

    ax.pie(
        counts.values,
        labels=counts.index,
        autopct="%1.1f%%"
    )

    ax.set_title("Top Indicators")
    st.pyplot(fig)


def count_plot_chart(df):
    if "Indicator Name" not in df.columns:
        return

    top = (
        df["Indicator Name"]
        .value_counts()
        .head(10)
        .index
    )

    temp = df[df["Indicator Name"].isin(top)]

    fig, ax = plt.subplots(figsize=(10, 5))

    sns.countplot(
        data=temp,
        y="Indicator Name",
        ax=ax
    )

    ax.set_title("Indicator Frequency")
    st.pyplot(fig)


def violin_plot_chart(df):
    if "Year" not in df.columns or "Value" not in df.columns:
        return

    sample = df.dropna(subset=["Value"])

    years = sorted(sample["Year"].unique())

    if len(years) > 10:
        selected_years = years[::max(1, len(years) // 10)]
        sample = sample[sample["Year"].isin(selected_years)]

    fig, ax = plt.subplots(figsize=(12, 5))

    sns.violinplot(
        data=sample,
        x="Year",
        y="Value",
        ax=ax
    )

    plt.xticks(rotation=45)
    ax.set_title("Value Distribution by Year")

    st.pyplot(fig)

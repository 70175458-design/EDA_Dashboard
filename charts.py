import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


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
    trend = df.groupby("Year")["Value"].mean().dropna()

    if trend.empty:
        return

    fig, ax = plt.subplots(figsize=(10, 4))

    ax.plot(
        trend.index,
        trend.values,
        marker="o"
    )

    ax.set_title("Average Value by Year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Average Value")

    st.pyplot(fig)


def scatter_chart(df):
    sample = df.dropna(subset=["Value"])

    if len(sample) > 5000:
        sample = sample.sample(
            5000,
            random_state=42
        )

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.scatter(
        sample["Year"],
        sample["Value"],
        alpha=0.5
    )

    ax.set_title("Year vs Value")
    ax.set_xlabel("Year")
    ax.set_ylabel("Value")

    st.pyplot(fig)


def area_chart(df):
    trend = df.groupby("Year")["Value"].mean().dropna()

    if trend.empty:
        return

    fig, ax = plt.subplots(figsize=(10, 4))

    ax.fill_between(
        trend.index,
        trend.values
    )

    ax.set_title("Average Value Over Time")
    ax.set_xlabel("Year")
    ax.set_ylabel("Average Value")

    st.pyplot(fig)


def bar_chart(df):
    country_avg = (
        df.groupby("Country Name")["Value"]
        .mean()
        .dropna()
        .sort_values(ascending=False)
        .head(15)
    )

    if country_avg.empty:
        return

    fig, ax = plt.subplots(figsize=(10, 6))

    country_avg.sort_values().plot(
        kind="barh",
        ax=ax
    )

    ax.set_title("Top 15 Countries by Average Value")
    ax.set_xlabel("Average Value")

    st.pyplot(fig)


def heatmap_chart(df):
    pivot = df.pivot_table(
        values="Value",
        index="Country Name",
        columns="Year",
        aggfunc="mean"
    )

    if pivot.empty:
        return

    pivot = pivot.head(20)

    fig, ax = plt.subplots(figsize=(12, 8))

    sns.heatmap(
        pivot.fillna(0),
        cmap="viridis",
        ax=ax
    )

    ax.set_title("Country-Year Heatmap")

    st.pyplot(fig)

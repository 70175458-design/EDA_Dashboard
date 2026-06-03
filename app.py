import streamlit as st
import pandas as pd

from filters import sidebar_filters
from charts import *

st.set_page_config(
    page_title="EdStats Dashboard",
    layout="wide"
)

st.title("📊 EdStats Dashboard")

# Load dataset
df = pd.read_csv("EdStatsData_Sample.csv")

# Remove unnamed columns
df = df.loc[
    :,
    ~df.columns.str.contains("^Unnamed")
]

# Year columns
year_cols = [
    col
    for col in df.columns
    if str(col).isdigit()
]

# Convert wide -> long format
df = df.melt(
    id_vars=[
        "Country Name",
        "Country Code",
        "Indicator Name",
        "Indicator Code"
    ],
    value_vars=year_cols,
    var_name="Year",
    value_name="Value"
)

df["Year"] = pd.to_numeric(
    df["Year"],
    errors="coerce"
)

df["Value"] = pd.to_numeric(
    df["Value"],
    errors="coerce"
)

df = df.dropna(subset=["Value"])

# Sidebar Filters
df = sidebar_filters(df)

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Countries",
    df["Country Name"].nunique()
)

col2.metric(
    "Indicators",
    df["Indicator Name"].nunique()
)

col3.metric(
    "Records",
    f"{len(df):,}"
)

col4.metric(
    "Average Value",
    round(df["Value"].mean(), 2)
)

st.divider()

# Charts
line_chart(df)

col1, col2 = st.columns(2)

with col1:
    histogram_chart(df)

with col2:
    scatter_chart(df)

col1, col2 = st.columns(2)

with col1:
    area_chart(df)

with col2:
    bar_chart(df)

heatmap_chart(df)

import streamlit as st
import pandas as pd
from filters import sidebar_filters
from charts import *

st.set_page_config(page_title="EdStats Dashboard", layout="wide")

st.title("📊 EdStats Dashboard")

df = pd.read_csv("EdStatsData_Sample.csv")

# Remove empty columns
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

# Identify year columns
year_cols = [c for c in df.columns if str(c).isdigit()]

# Convert to long format
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

df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df["Value"] = pd.to_numeric(df["Value"], errors="coerce")

df = sidebar_filters(df)

col1, col2 = st.columns(2)
col1.metric("Rows", df.shape[0])
col2.metric("Columns", df.shape[1])

histogram_chart(df)
line_chart(df)
scatter_chart(df)
area_chart(df)

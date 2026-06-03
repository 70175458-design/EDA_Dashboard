import streamlit as st
import pandas as pd
from charts import bar_chart

st.set_page_config(
page_title="EdStats Dashboard",
layout="wide"
)

st.title("📊 EdStats Dashboard")

df = pd.read_csv("EdStatsData_Sample.csv")

st.success("Dataset Loaded Successfully!")

col1, col2 = st.columns(2)

with col1:
st.metric("Rows", df.shape[0])

with col2:
st.metric("Columns", df.shape[1])

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Bar Chart")
bar_chart(df)

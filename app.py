import streamlit as st
import pandas as pd

st.set_page_config(page_title="EdStats Dashboard")

st.title("📊 EdStats Dashboard")

df = pd.read_csv("EdStatsData_Sample.csv")

st.success("Dataset Loaded Successfully!")

st.write("Rows:", df.shape[0])
st.write("Columns:", df.shape[1])

st.dataframe(df.head())

import streamlit as st
import pandas as pd
from filters import sidebar_filters
from charts import *

st.set_page_config(page_title="EdStats Dashboard", layout="wide")

st.title("📊 EdStats Dashboard")

df = pd.read_csv("EdStatsData_Sample.csv")

df = sidebar_filters(df)

st.metric("Rows", df.shape[0])
st.metric("Columns", df.shape[1])

pie_chart(df)
histogram_chart(df)
line_chart(df)
bar_chart(df)
scatter_chart(df)
box_chart(df)
heatmap_chart(df)
area_chart(df)
count_plot_chart(df)
violin_plot_chart(df)

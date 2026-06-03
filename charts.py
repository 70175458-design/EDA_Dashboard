import streamlit as st
import matplotlib.pyplot as plt

def bar_chart(df):
region_avg = df.groupby("Region")["Value"].mean().dropna()

```
fig, ax = plt.subplots(figsize=(10,5))
region_avg.sort_values().plot(kind="barh", ax=ax)

ax.set_title("Average Value by Region")

st.pyplot(fig)


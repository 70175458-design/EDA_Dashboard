import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def pie_chart(df):
    if "Income Group" not in df.columns:
        return

    fig, ax = plt.subplots()
    data = df.groupby("Income Group")["Value"].count()
    ax.pie(data.values, labels=data.index, autopct="%1.1f%%")
    ax.set_title("Pie Chart")
    st.pyplot(fig)

def histogram_chart(df):
    fig, ax = plt.subplots()
    vals = df["Value"].dropna()
    ax.hist(vals, bins=30)
    ax.set_title("Histogram")
    st.pyplot(fig)

def line_chart(df):
    if "Year" not in df.columns or "Value" not in df.columns:
        return

    trend = df.groupby("Year")["Value"].mean()
    fig, ax = plt.subplots()
    ax.plot(trend.index, trend.values)
    ax.set_title("Line Chart")
    st.pyplot(fig)

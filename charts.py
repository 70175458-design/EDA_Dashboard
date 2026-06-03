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

def bar_chart(df):
if "Region" not in df.columns:
return
data = df.groupby("Region")["Value"].mean().dropna()
fig, ax = plt.subplots()
data.sort_values().plot(kind="barh", ax=ax)
ax.set_title("Bar Chart")
st.pyplot(fig)

def scatter_chart(df):
if "Year" not in df.columns:
return
sample = df.dropna(subset=["Value"])
fig, ax = plt.subplots()
ax.scatter(sample["Year"], sample["Value"], alpha=0.5)
ax.set_title("Scatter Plot")
st.pyplot(fig)

def box_chart(df):
if "Region" not in df.columns:
return
fig, ax = plt.subplots(figsize=(10,5))
sns.boxplot(data=df, x="Region", y="Value", ax=ax)
plt.xticks(rotation=45)
ax.set_title("Box Plot")
st.pyplot(fig)

def heatmap_chart(df):
if "Region" not in df.columns or "Year" not in df.columns:
return
pivot = df.pivot_table(values="Value", index="Region", columns="Year", aggfunc="mean")
fig, ax = plt.subplots(figsize=(10,5))
sns.heatmap(pivot.fillna(0), ax=ax)
ax.set_title("Heatmap")
st.pyplot(fig)

def area_chart(df):
if "Year" not in df.columns:
return
trend = df.groupby("Year")["Value"].mean()
fig, ax = plt.subplots()
ax.fill_between(trend.index, trend.values)
ax.set_title("Area Chart")
st.pyplot(fig)

def count_plot_chart(df):
if "Region" not in df.columns:
return
fig, ax = plt.subplots()
sns.countplot(y=df["Region"], ax=ax)
ax.set_title("Count Plot")
st.pyplot(fig)

def violin_plot_chart(df):
if "Income Group" not in df.columns:
return
fig, ax = plt.subplots(figsize=(10,5))
sns.violinplot(data=df, x="Income Group", y="Value", ax=ax)
plt.xticks(rotation=45)
ax.set_title("Violin Plot")
st.pyplot(fig)








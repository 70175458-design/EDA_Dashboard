import streamlit as st
import pandas as pd

st.set_page_config(page_title="EdStats Dashboard")

st.title("📊 EdStats Dashboard")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:
df = pd.read_csv(uploaded_file)

```
st.success("File uploaded successfully!")

st.write("Rows:", df.shape[0])
st.write("Columns:", df.shape[1])

st.dataframe(df.head())


else:
st.info("Please upload a CSV file.")

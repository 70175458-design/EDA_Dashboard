import streamlit as st
import pandas as pd
from filters import sidebar_filters

st.set_page_config(
page_title="EdStats Dashboard",
layout="wide"
)

st.title("📊 Global Education Statistics Dashboard")

uploaded_file = st.file_uploader(
"Upload CSV File",
type=["csv"]
)

if uploaded_file is not None:

```
df = pd.read_csv(uploaded_file)

filtered_df = sidebar_filters(df)

st.success("Dataset Loaded Successfully")

st.write("Rows:", filtered_df.shape[0])
st.write("Columns:", filtered_df.shape[1])

st.dataframe(filtered_df.head())
```

else:
st.info("Please upload your CSV file.")

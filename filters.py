import streamlit as st

def sidebar_filters(df):

```
if "Region" in df.columns:
    regions = st.sidebar.multiselect(
        "Region",
        sorted(df["Region"].dropna().unique()),
        default=sorted(df["Region"].dropna().unique())
    )
    df = df[df["Region"].isin(regions)]

if "Income Group" in df.columns:
    income = st.sidebar.multiselect(
        "Income Group",
        sorted(df["Income Group"].dropna().unique()),
        default=sorted(df["Income Group"].dropna().unique())
    )
    df = df[df["Income Group"].isin(income)]

return df


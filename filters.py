import streamlit as st

def sidebar_filters(df):

```
st.sidebar.header("Filters")

regions = st.sidebar.multiselect(
    "Region",
    sorted(df["Region"].dropna().unique()),
    default=sorted(df["Region"].dropna().unique())
)

income_groups = st.sidebar.multiselect(
    "Income Group",
    sorted(df["Income Group"].dropna().unique()),
    default=sorted(df["Income Group"].dropna().unique())
)

filtered_df = df[
    (df["Region"].isin(regions))
    & (df["Income Group"].isin(income_groups))
]

return filtered_df
```

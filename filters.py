import streamlit as st


def sidebar_filters(df):
    st.sidebar.header("🔎 Filters")

    countries = st.sidebar.multiselect(
        "Country",
        sorted(df["Country Name"].dropna().unique())
    )

    indicators = st.sidebar.multiselect(
        "Indicator",
        sorted(df["Indicator Name"].dropna().unique())
    )

    year_min = int(df["Year"].min())
    year_max = int(df["Year"].max())

    year_range = st.sidebar.slider(
        "Year Range",
        min_value=year_min,
        max_value=year_max,
        value=(year_min, year_max)
    )

    if countries:
        df = df[df["Country Name"].isin(countries)]

    if indicators:
        df = df[df["Indicator Name"].isin(indicators)]

    df = df[
        (df["Year"] >= year_range[0]) &
        (df["Year"] <= year_range[1])
    ]

    return df

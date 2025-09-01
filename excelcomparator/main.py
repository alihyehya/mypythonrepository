import streamlit as st
import pandas as pd
from excel_comparator_utils import read_excel_any, show_insights, clean_dataframe, match_and_compare_by_name

st.set_page_config(page_title="Excel Comparator", layout="wide")
st.title("Excel Comparator")

f1 = st.file_uploader("Upload file1.xlsx", type=["xlsx"])
f2 = st.file_uploader("Upload file2.xlsx", type=["xlsx"])

if f1 and f2:
    df1 = read_excel_any(f1)
    df2 = read_excel_any(f2)

    c1, c2 = st.columns(2)
    with c1: show_insights(df1, "Insights (file1 before cleaning)")
    with c2: show_insights(df2, "Insights (file2 before cleaning)")

    df1c = clean_dataframe(df1, subset=["name", "amount"], how="any")
    df2c = clean_dataframe(df2, subset=["name", "amount"], how="any")

    c1, c2 = st.columns(2)
    with c1: show_insights(df1c, "Insights (file1 after cleaning)")
    with c2: show_insights(df2c, "Insights (file2 after cleaning)")

    matches, only1, only2 = match_and_compare_by_name(
        df1c, df2c, "name", "amount", "name", "amount", tolerance=0.0
    )

    st.subheader("Matches (names in both, with amount comparison)")
    st.dataframe(matches, use_container_width=True)

    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Only in file1.xlsx")
        st.metric("Count", only1.shape[0])
        st.dataframe(only1, use_container_width=True)
    with c2:
        st.subheader("Only in file2.xlsx")
        st.metric("Count", only2.shape[0])
        st.dataframe(only2, use_container_width=True)
else:
    st.info("Upload both Excel files to begin.")

import pandas as pd
import streamlit as st
def read_excel_any(file_obj, sheet_name=0):
    return pd.read_excel(file_obj, sheet_name=sheet_name)

def basic_insights(df):
    return {
        "row_count": len(df),
        "column_count": df.shape[1],
        "column_names": list(df.columns),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "nulls_by_column": df.isna().sum().to_dict(),
        "total_nulls": int(df.isna().sum().sum())
    }

def clean_dataframe(df, subset=None, how="any", drop_duplicate_rows=False):
    cleaned = df.dropna(subset=subset, how=how)
    if drop_duplicate_rows:
        cleaned = cleaned.drop_duplicates()
    return cleaned.reset_index(drop=True)

import pandas as pd

def match_and_compare_by_name(
    left, right,
    left_name_col, left_amount_col,
    right_name_col, right_amount_col,
    tolerance=0.0
):

    left = left.copy()
    right = right.copy()
    left[left_amount_col] = pd.to_numeric(left[left_amount_col], errors="coerce")
    right[right_amount_col] = pd.to_numeric(right[right_amount_col], errors="coerce")

    merged = left.merge(
        right,
        left_on=left_name_col,
        right_on=right_name_col,
        how="outer",
        suffixes=("_left", "_right"),
        indicator=True,
    )


    amt_left = f"{left_amount_col}_left" if f"{left_amount_col}_left" in merged.columns else left_amount_col
    amt_right = f"{right_amount_col}_right" if f"{right_amount_col}_right" in merged.columns else right_amount_col

    both = merged[merged["_merge"] == "both"].copy()
    both["amount_diff"] = (both[amt_left] - both[amt_right]).abs()
    both["amount_match"] = both["amount_diff"] <= float(tolerance)

    only_left = merged[merged["_merge"] == "left_only"].copy()
    only_right = merged[merged["_merge"] == "right_only"].copy()

    return both, only_left, only_right


def show_insights(df, title):
    info = basic_insights(df)
    st.subheader(title)
    top = pd.DataFrame([{
        "rows": info["row_count"],
        "columns": info["column_count"],
        "total_nulls": info["total_nulls"],
    }])
    st.table(top)
    st.write("Columns:", ", ".join(info["column_names"]))
    st.write("Dtypes")
    st.table(pd.DataFrame(info["dtypes"].items(), columns=["column","dtype"]))
    st.write("Nulls by column")
    st.table(pd.DataFrame(info["nulls_by_column"].items(), columns=["column","nulls"]))
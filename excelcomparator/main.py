import io
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Excel Comparator", page_icon="📊", layout="wide")
st.title("📊 Excel Comparator (simple & readable)")

# ---------- Helpers ----------
def read_table(upload):
    """Read CSV/XLS/XLSX into a DataFrame."""
    if upload is None:
        return None
    name = upload.name.lower()
    try:
        if name.endswith(".csv"):
            return pd.read_csv(upload)
        else:  # xls/xlsx
            return pd.read_excel(upload)
    except Exception as e:
        st.error(f"Could not read {upload.name}: {e}")
        return None

def normalize_name(s):
    """Basic name cleanup: strip, collapse spaces, uppercase."""
    if s is None:
        return None
    return (
        s.astype(str)
         .str.strip()
         .str.replace(r"\s+", " ", regex=True)
         .str.upper()
    )

def clean_amount(s):
    """Coerce to numeric, treat blanks/non-numeric as 0."""
    return pd.to_numeric(s, errors="coerce").fillna(0.0)

def quick_insights(df, title):
    with st.expander(f"🔎 Insights: {title}", expanded=False):
        st.write(f"Rows: **{len(df)}**, Columns: **{df.shape[1]}**")
        st.write("Nulls per column:")
        st.dataframe(df.isna().sum().to_frame("null_count"))

def to_csv_download(df, filename):
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("⬇️ Download CSV", data=csv, file_name=filename, mime="text/csv")

# ---------- Upload ----------
left_file = st.file_uploader("File A (.csv/.xls/.xlsx)", type=["csv", "xls", "xlsx"], key="a")
right_file = st.file_uploader("File B (.csv/.xls/.xlsx)", type=["csv", "xls", "xlsx"], key="b")

df_a = read_table(left_file)
df_b = read_table(right_file)

if df_a is not None:
    st.subheader("Preview: File A")
    st.dataframe(df_a.head(10), use_container_width=True)
    quick_insights(df_a, "File A")

if df_b is not None:
    st.subheader("Preview: File B")
    st.dataframe(df_b.head(10), use_container_width=True)
    quick_insights(df_b, "File B")

# ---------- Column selection ----------
if (df_a is not None) and (df_b is not None):
    st.markdown("---")
    st.subheader("Choose matching columns")

    col1, col2 = st.columns(2)
    with col1:
        name_col_a = st.selectbox("File A: name column", df_a.columns, key="name_a")
        amt_col_a  = st.selectbox("File A: amount column", df_a.columns, key="amt_a")
    with col2:
        name_col_b = st.selectbox("File B: name column", df_b.columns, key="name_b")
        amt_col_b  = st.selectbox("File B: amount column", df_b.columns, key="amt_b")

    tol = st.number_input("Amount match tolerance", min_value=0.0, value=0.01, step=0.01)

    # ---------- Cleaning ----------
    work_a = df_a.copy()
    work_b = df_b.copy()

    work_a["__NAME__"] = normalize_name(work_a[name_col_a])
    work_b["__NAME__"] = normalize_name(work_b[name_col_b])

    work_a["__AMT__"] = clean_amount(work_a[amt_col_a])
    work_b["__AMT__"] = clean_amount(work_b[amt_col_b])

    # Report rows with null names
    na_rows_a = work_a[work_a["__NAME__"].isna()]
    na_rows_b = work_b[work_b["__NAME__"].isna()]

    with st.expander("⚠️ Rows with missing names", expanded=False):
        if not na_rows_a.empty:
            st.write("File A:")
            st.dataframe(na_rows_a)
        if not na_rows_b.empty:
            st.write("File B:")
            st.dataframe(na_rows_b)
        if na_rows_a.empty and na_rows_b.empty:
            st.write("None 🎉")

    # ---------- Match by name ----------
    merged = work_a[["__NAME__", "__AMT__"]].rename(columns={"__AMT__": "AMT_A"})
    merged = merged.groupby("__NAME__", dropna=False, as_index=False)["AMT_A"].sum()

    tmp = work_b[["__NAME__", "__AMT__"]].rename(columns={"__AMT__": "AMT_B"})
    tmp = tmp.groupby("__NAME__", dropna=False, as_index=False)["AMT_B"].sum()

    merged = merged.merge(tmp, on="__NAME__", how="outer")

    # Classify
    merged["AMT_A"] = merged["AMT_A"].fillna(0.0)
    merged["AMT_B"] = merged["AMT_B"].fillna(0.0)
    merged["DIFF"]  = merged["AMT_A"] - merged["AMT_B"]
    merged["MATCHED_NAME"] = (~merged["__NAME__"].isna()) & merged[["AMT_A","AMT_B"]].notna().all(axis=1)
    merged["AMOUNT_MATCH"]  = merged["DIFF"].abs() <= tol

    # Views
    in_both = merged[merged["MATCHED_NAME"]]
    exact_or_tol = in_both[in_both["AMOUNT_MATCH"]].sort_values("__NAME__")
    mismatched   = in_both[~in_both["AMOUNT_MATCH"]].sort_values("__NAME__")
    only_a = merged[merged["AMT_B"].eq(0) & ~merged["AMT_A"].eq(0)].sort_values("__NAME__")
    only_b = merged[merged["AMT_A"].eq(0) & ~merged["AMT_B"].eq(0)].sort_values("__NAME__")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "✅ Name & Amount match",
        "❗ Name matches, Amount differs",
        "🅰️ Only in File A",
        "🅱️ Only in File B",
        "📦 Full result",
    ])

    with tab1:
        st.dataframe(exact_or_tol.rename(columns={"__NAME__": "NAME"}), use_container_width=True)
        to_csv_download(exact_or_tol.rename(columns={"__NAME__": "NAME"}), "matches.csv")

    with tab2:
        st.dataframe(mismatched.rename(columns={"__NAME__": "NAME"}), use_container_width=True)
        to_csv_download(mismatched.rename(columns={"__NAME__": "NAME"}), "amount_mismatches.csv")

    with tab3:
        st.dataframe(only_a.rename(columns={"__NAME__": "NAME"}), use_container_width=True)
        to_csv_download(only_a.rename(columns={"__NAME__": "NAME"}), "only_in_A.csv")

    with tab4:
        st.dataframe(only_b.rename(columns={"__NAME__": "NAME"}), use_container_width=True)
        to_csv_download(only_b.rename(columns={"__NAME__": "NAME"}), "only_in_B.csv")

    with tab5:
        st.dataframe(merged.rename(columns={"__NAME__": "NAME"}), use_container_width=True)
        to_csv_download(merged.rename(columns={"__NAME__": "NAME"}), "full_comparison.csv")

    st.success("Done. Use the tabs above to review and download results.")
else:
    st.info("Upload **both** files to start.")

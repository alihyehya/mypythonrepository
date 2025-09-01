from cruds import *
import streamlit as st

st.set_page_config(page_title="Available Courses", page_icon="📚", layout="centered")
st.title("Available Courses")
st.caption("Browse the current catalog and pick what suits you best.")
display_courses()

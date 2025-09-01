from cruds import *
import streamlit as st

st.set_page_config(page_title="Admin Dashboard", page_icon="📊", layout="wide")

st.title("Admin Dashboard")
st.caption("Monitor registrations and course performance at a glance.")

c1, c2, c3 = st.columns(3)
with c1:
    student_total()
with c2:
    courses_total()
with c3:
    course_max()

st.divider()

tab_students, tab_stats = st.tabs(["👥 Registered Students", "📈 Statistics"])

with tab_students:
    st.subheader("Registered Students")
    display_students()

with tab_stats:
    st.subheader("Course Registration Counts")
    course_stat()

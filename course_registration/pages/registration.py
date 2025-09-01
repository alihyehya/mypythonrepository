from cruds import *
import streamlit as st

st.set_page_config(page_title="Student Registration", page_icon="📝", layout="centered")
st.title("Student Registration")

with st.form("reg_form", clear_on_submit=False, border=True):
    st.write("Fill in your details")
    c1, c2 = st.columns(2)
    with c1:
        name = st.text_input("Name", placeholder="Jane Doe")
    with c2:
        email = st.text_input("Email", placeholder="jane@example.com")
    title_to_id, id_to_title = read_courses()
    options = list(title_to_id.keys())
    selected_option = st.selectbox("Select a course", options, index=0)
    registered_course_id = title_to_id[selected_option]
    submitted = st.form_submit_button("Submit")

if submitted:
    create_student(name, email, registered_course_id)
    st.success("Successfully Registered ✅")

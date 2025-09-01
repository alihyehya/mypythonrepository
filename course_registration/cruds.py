import sqlite3
import streamlit as st

def read_courses():
    conn = sqlite3.connect('course_registration.db')
    cursor = conn.cursor()
    title_to_id = {}
    id_to_title = {}
    for row in cursor.execute("SELECT * FROM courses"):
        l = list(row)
        title_to_id[l[1]] = l[0]
        id_to_title[l[0]] = l[1]
    conn.close()
    return title_to_id, id_to_title

def display_courses():
    conn = sqlite3.connect('course_registration.db')
    cursor = conn.cursor()
    for row in cursor.execute("SELECT * FROM courses"):
        l = list(row)
        with st.container(border=True):
            st.markdown(f"**{l[1]}**")
            st.caption(f"ID: {l[0]}")
            if l[2]:
                st.write(l[2])
    conn.close()

def create_student(name, email, registered_course_id):
    conn = sqlite3.connect('course_registration.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, email, registered_course_id) VALUES (?, ?, ?)", (name, email, registered_course_id))
    conn.commit()
    conn.close()

def display_students():
    title_to_id, id_to_title = read_courses()
    conn = sqlite3.connect('course_registration.db')
    cursor = conn.cursor()
    for row in cursor.execute("SELECT * FROM students"):
        l = list(row)
        with st.expander(f"{l[1]} · {id_to_title.get(l[3], 'Unassigned')}"):
            c1, c2 = st.columns(2)
            with c1:
                st.markdown(f"**Student ID:** {l[0]}")
                st.markdown(f"**Email:** {l[2]}")
            with c2:
                st.markdown(f"**Course:** {id_to_title.get(l[3], 'Unassigned')}")
    conn.close()

def course_stat():
    conn = sqlite3.connect('course_registration.db')
    cursor = conn.cursor()
    cols = st.columns(3)
    i = 0
    for row in cursor.execute("SELECT c.name AS course_name, COUNT(s.student_id) AS student_count FROM courses c LEFT JOIN students s ON c.course_id = s.registered_course_id GROUP BY c.course_id ORDER BY student_count DESC;"):
        l = list(row)
        with cols[i % 3]:
            st.metric(label=l[0], value=int(l[1]))
        i += 1
    conn.close()

def student_total():
    conn = sqlite3.connect('course_registration.db')
    cursor = conn.cursor()
    for row in cursor.execute("SELECT COUNT(*) AS total_students FROM students;"):
        l = list(row)
        st.metric(label="Total Registered Students", value=int(l[0]))
    conn.close()

def courses_total():
    conn = sqlite3.connect('course_registration.db')
    cursor = conn.cursor()
    for row in cursor.execute("SELECT COUNT(*) AS total_courses FROM courses;"):
        l = list(row)
        st.metric(label="Total Courses Offered", value=int(l[0]))
    conn.close()

def course_max():
    conn = sqlite3.connect('course_registration.db')
    cursor = conn.cursor()
    for row in cursor.execute("SELECT c.name AS course_name, COUNT(s.student_id) AS student_count FROM courses c LEFT JOIN students s ON c.course_id = s.registered_course_id GROUP BY c.course_id ORDER BY student_count DESC LIMIT 1;"):
        l = list(row)
        st.metric(label="Most Registered Course", value=l[0], delta=int(l[1]))
    conn.close()

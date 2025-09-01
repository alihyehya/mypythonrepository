import sqlite3

conn = sqlite3.connect("course_registration.db")
cursor = conn.cursor()

with open("schema.sql", "r") as file:
    script = file.read()

cursor.executescript(script)
conn.commit()
conn.close()
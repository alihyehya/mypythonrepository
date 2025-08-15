import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect("tips_database.db")
cursor = conn.cursor()

with open("schema.sql", "r") as file:
    script = file.read()

cursor.executescript(script)
conn.commit()
conn.close()
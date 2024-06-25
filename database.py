import sqlite3

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('students.db')
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            subject TEXT NOT NULL,
                            grade Integer);''')
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def add_student(conn, student, subject, grade):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students(name, subject, grade) VALUES(?, ?, ?)", (student, subject, grade))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def get_students(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        return rows
    except sqlite3.Error as e:
        print(e)
        return []

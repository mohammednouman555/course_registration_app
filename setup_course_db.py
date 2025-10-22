import sqlite3

conn = sqlite3.connect('courses.db')
c = conn.cursor()

# Students table
c.execute('''CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    roll_no TEXT
)''')

# Courses table
c.execute('''CREATE TABLE IF NOT EXISTS courses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT,
    instructor TEXT
)''')

# Registrations table
c.execute('''CREATE TABLE IF NOT EXISTS registrations(
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(id),
    FOREIGN KEY(course_id) REFERENCES courses(id)
)''')

conn.commit()
conn.close()

print("Database and tables created successfully!")

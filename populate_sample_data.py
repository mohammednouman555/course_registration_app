import sqlite3

# Connect to database
conn = sqlite3.connect('courses.db')
c = conn.cursor()

# Add sample students
students = [
    ("Mohammed Nouman", "160323733114"),
    ("Ayesha Khan", "160323733115"),
    ("Rohit Sharma", "160323733116")
]

for name, roll_no in students:
    c.execute("INSERT INTO students(name, roll_no) VALUES (?, ?)", (name, roll_no))

# Add sample courses
courses = [
    ("Python Programming", "Prof. Rao"),
    ("Data Structures", "Prof. Singh"),
    ("Web Development", "Prof. Sharma")
]

for course_name, instructor in courses:
    c.execute("INSERT INTO courses(course_name, instructor) VALUES (?, ?)", (course_name, instructor))

conn.commit()
conn.close()

print("Sample students and courses added successfully!")

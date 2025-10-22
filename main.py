from fastapi import FastAPI, Form
import sqlite3
from fastapi.responses import HTMLResponse

app = FastAPI()

# View all courses
@app.get("/courses")
def view_courses():
    conn = sqlite3.connect('courses.db')
    c = conn.cursor()
    c.execute("SELECT * FROM courses")
    courses = c.fetchall()
    conn.close()
    return {"courses": courses}

# Register student for a course
@app.post("/register")
def register_course(student_id: int = Form(...), course_id: int = Form(...)):
    conn = sqlite3.connect('courses.db')
    c = conn.cursor()
    c.execute("INSERT INTO registrations(student_id, course_id) VALUES (?, ?)", (student_id, course_id))
    conn.commit()
    conn.close()
    return {"status": "Registration successful"}

# Optional homepage
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h2>Course Registration</h2>
    <form action="/register" method="post">
        Student ID: <input type="text" name="student_id"><br>
        Course ID: <input type="text" name="course_id"><br>
        <input type="submit" value="Register">
    </form>
    """

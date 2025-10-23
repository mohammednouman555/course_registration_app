from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import sqlite3

app = FastAPI()
DB_FILE = "courses.db"
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request, message: str = None):
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute("SELECT id, name FROM students")
        students = c.fetchall()
        c.execute("SELECT id, course_name FROM courses")
        courses = c.fetchall()
    return templates.TemplateResponse(
        "course_registration.html",
        {"request": request, "students": students, "courses": courses, "message": message}
    )


@app.post("/register", response_class=HTMLResponse)
def register_course(request: Request, student_id: int = Form(...), course_id: int = Form(...)):
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        # Validate student
        c.execute("SELECT name FROM students WHERE id=?", (student_id,))
        student = c.fetchone()
        if not student:
            return home(request, message="Error: Student not found")

        # Validate course
        c.execute("SELECT course_name FROM courses WHERE id=?", (course_id,))
        course = c.fetchone()
        if not course:
            return home(request, message="Error: Course not found")

        # Check duplicate
        c.execute("SELECT * FROM registrations WHERE student_id=? AND course_id=?", (student_id, course_id))
        if c.fetchone():
            return home(request, message="Error: Already registered for this course")

        # Insert registration
        c.execute("INSERT INTO registrations(student_id, course_id) VALUES (?, ?)", (student_id, course_id))
        conn.commit()

    return home(request, message=f"Success: {student[0]} registered for {course[0]}")


@app.get("/registrations", response_class=HTMLResponse)
def view_registrations(request: Request):
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute('''
            SELECT students.name, courses.course_name
            FROM registrations
            JOIN students ON registrations.student_id = students.id
            JOIN courses ON registrations.course_id = courses.id
        ''')
        registrations = c.fetchall()
    return templates.TemplateResponse("registrations.html", {"request": request, "registrations": registrations})

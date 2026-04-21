from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import sqlite3
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

app.mount("/static", StaticFiles(directory="static"), name="static")


def get_db_connection():
    conn = sqlite3.connect("courses.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    conn = get_db_connection()
    students = conn.execute("SELECT * FROM students").fetchall()
    courses = conn.execute("SELECT * FROM courses").fetchall()
    conn.close()

    return templates.TemplateResponse("course_registration.html", {
        "request": request,
        "students": students,
        "courses": courses,
        "message": ""
    })


@app.post("/register", response_class=HTMLResponse)
def register(request: Request, student_id: int = Form(...), course_id: int = Form(...)):
    conn = get_db_connection()

    student = conn.execute("SELECT * FROM students WHERE id=?", (student_id,)).fetchone()
    course = conn.execute("SELECT * FROM courses WHERE id=?", (course_id,)).fetchone()

    if not student:
        conn.close()
        return RedirectResponse("/?message=Student not found", status_code=303)

    if not course:
        conn.close()
        return RedirectResponse("/?message=Course not found", status_code=303)

    existing = conn.execute(
        "SELECT * FROM registrations WHERE student_id=? AND course_id=?",
        (student_id, course_id)
    ).fetchone()

    if existing:
        conn.close()
        return RedirectResponse("/?message=Already registered", status_code=303)

    conn.execute(
        "INSERT INTO registrations (student_id, course_id) VALUES (?, ?)",
        (student_id, course_id)
    )
    conn.commit()
    conn.close()

    return RedirectResponse("/", status_code=303)


@app.get("/courses", response_class=HTMLResponse)
def view_courses(request: Request):
    conn = get_db_connection()
    courses = conn.execute("SELECT * FROM courses").fetchall()
    conn.close()

    return templates.TemplateResponse("view_courses.html", {
        "request": request,
        "courses": courses
    })


@app.get("/registrations", response_class=HTMLResponse)
def view_registrations(request: Request):
    conn = get_db_connection()

    data = conn.execute("""
        SELECT students.name, courses.course_name
        FROM registrations
        JOIN students ON students.id = registrations.student_id
        JOIN courses ON courses.id = registrations.course_id
    """).fetchall()

    conn.close()

    return templates.TemplateResponse("view_registrations.html", {
        "request": request,
        "registrations": data
    })
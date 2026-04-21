# Course Registration Web App

A **FastAPI-based web application** for registering students to courses using **SQLite**. Includes:

- Dynamic registration form
- Success/error messages
- View all registrations
- Clean UI with CSS

## Features

- Register students for courses
- Prevent duplicate registrations
- View courses and registrations
- Fully dynamic and interactive

## Setup

1. Clone the repository:
```bash
git clone https://github.com/USERNAME/course_registration.git
cd course_registration
Create and activate virtual environment:

bash
Copy code
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Setup database and sample data:

bash
Copy code
python setup_course_db.py
python populate_sample_data.py
Run the app:

bash
Copy code
uvicorn main:app --reload
Open browser:

cpp
Copy code
http://127.0.0.1:8000
Author
Mohammed Nouman

GitHub: mohammednouman555

Email: mohammednouman555@gmail.com

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

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/USERNAME/course_registration.git](https://github.com/USERNAME/course_registration.git)
    cd course_registration
    ```

2.  **Create and activate a virtual environment:**
    * Create the environment:
        ```bash
        python -m venv .venv
        ```
    * Activate the environment:
        * On Windows:
            ```bash
            .venv\Scripts\activate
            ```
        * On Linux/Mac:
            ```bash
            source .venv/bin/activate
            ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Setup the database and sample data:**
    ```bash
    python setup_course_db.py
    python populate_sample_data.py
    ```

5.  **Run the app:**
    ```bash
    uvicorn main:app --reload
    ```

6.  **Open your browser** and visit:
    `http://127.0.0.1:8000`

---

## Author

**Mohammed Nouman**
* **GitHub:** [@mohammednouman555](https://github.com/mohammednouman555)
* **Email:** mohammednouman555@gmail.com

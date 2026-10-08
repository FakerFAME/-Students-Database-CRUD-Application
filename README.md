# 🎓 Student Management CRUD API

A production-ready, modular RESTful API built with **FastAPI** and **SQLite** for managing student records. This project strictly adheres to enterprise clean architecture and includes an optional AI integration using **Google Gemini** to answer natural language queries based on student records.

---

## 🚀 Features

- **Dynamic Interactive Web Hub**: A modern, animated glassmorphism web dashboard at `/` featuring live metric counters, instant client-side search, course filter tabs, full modal CRUD operations, and an interactive AI Advisor terminal.
- **Full CRUD Operations**: Create, Read, Update, and Delete student records with informative, descriptive responses.
- **Data Validation & Integrity**: Strict payload validation using Pydantic v2 schemas and automatic SQLite seed initialization.
- **Clean Architecture**: Highly modular, isolated route handlers with zero circular dependencies.
- **Spicy AI Reasoning Engine**: Ask questions in natural language grounded strictly on real-time database records using **Google Gemini 3.8 Flash**, returning beautifully formatted, structured Markdown with wit and flair.
- **Performance Telemetry**: Microsecond execution headers (`X-Process-Time`, `X-Powered-By`) on all HTTP responses.


---

## 🏗️ Architecture

```text
Request 
  └── main.py (FastAPI app)
       └── app/routes/base.py (APIRouter)
            ├── app/routes/create_student.py  (Route Handler)
            ├── app/routes/get_student.py     (Route Handler)
            ├── ...
            │    ├── app/schemas.py           (Pydantic validation)
            │    ├── app/database.py          (SQLAlchemy Session)
            │    └── app/model.py             (SQLAlchemy Models) -> SQLite DB
            │
            └── app/routes/ai_query.py        (AI Extension)
                 └── langchain_google_genai -> Gemini API
```

---

## ⚙️ Prerequisites

- **Python 3.9+**
- **Gemini API Key**

---

## 🛠️ Setup & Installation

### 1. Clone & Environment Setup
Clone the repository and set up your virtual environment:

```bash
# Create the virtual environment
python -m venv venv

# Activate the virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies
Install the required packages using pip:

```bash
pip install -r requirements.txt
```

### 3. Environment Variables
Make sure to configure your `.env` file with your Gemini API key:

```bash
GEMINI_MODEL=gemini-3.8-flash
GEMINI_API_KEY=your-gemini-api-key
```

---

## 🚀 Running the Server

Start the Uvicorn ASGI server with live reloading enabled:

```bash
uvicorn main:app --reload
```
*The server will start on `http://127.0.0.1:8000`*

---

## 🌐 Dynamic Web Hub & Interactive Playground

Open your browser to: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

The live dashboard provides:
- **Instant Search & Course Filtering**: Search scholars by name, email, or curriculum in real time.
- **Interactive Professor Nova AI Terminal**: Test natural language questions with instant Markdown responses, presets, and latency telemetry.
- **Visual Modal CRUD**: Add, edit, or delete scholar profiles directly with animated feedback toasts.

---

## 🧪 Interactive Swagger API Documentation

FastAPI automatically generates interactive Swagger documentation. 
Navigate your browser to: **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**


### Sample API Payloads

<details>
<summary><b>1. Create a Student (POST <code>/students/</code>)</b></summary>

```json
{
  "student_name": "Alice Johnson",
  "date_of_birth": "2000-05-14",
  "email": "alice.johnson@example.com",
  "phone": "+1-555-1234",
  "course": "Computer Science",
  "address": "123 Main St, Springfield",
  "enrollment_date": "2023-09-01"
}
```
</details>

<details>
<summary><b>2. Update a Student (PUT/PATCH <code>/students/{id}</code>)</b></summary>

```json
{
  "course": "Data Science",
  "phone": "+1-555-9876"
}
```
</details>

<details>
<summary><b>3. Query via AI (POST <code>/students/ai-query/</code>)</b></summary>

```json
{
  "question": "Which students are enrolled in Computer Science?"
}
```
</details>

---
*Developed as part of the EWB Edu Tech Pvt. Ltd. Internship Assignment.*

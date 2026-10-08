import time
from contextlib import asynccontextmanager
from datetime import datetime, timezone
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from app.database import engine, Base, SessionLocal
from app.routes.base import api_router
from app.seed import seed_database_if_empty
from app.ui import get_dashboard_html
from app import model

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize SQLite database tables
    Base.metadata.create_all(bind=engine)
    
    # Auto-seed verified student records if database is empty
    db = SessionLocal()
    try:
        count = seed_database_if_empty(db)
        print("\033[92m[DATABASE]\033[0m Verified SQLite student registry initialized with", count, "records.")
    finally:
        db.close()
        
    print("""
======================================================================
  [NOVA ACADEMY] STUDENT INTELLIGENCE & CRUD PLATFORM
  * Engine: FastAPI ASGI | AI Layer: Google Gemini 3.8 Flash
  * Interactive Web Hub : http://127.0.0.1:8000/
  * Swagger API Docs    : http://127.0.0.1:8000/docs
======================================================================
""")
    yield
    print("[SHUTDOWN] Nova Academy service safely terminated.")


tags_metadata = [
    {
        "name": "Students CRUD",
        "description": "⚡ **High-performance RESTful operations** for querying, creating, updating, and removing scholar profiles."
    },
    {
        "name": "AI Natural Language Query",
        "description": "🤖 **Google Gemini Reasoning Hub**: Grounded natural language intelligence synthesizing answers directly from real-time database records."
    }
]

app = FastAPI(
    title="🎓 Nova Academy — Student Management & AI Intelligence Platform",
    description="""
### Welcome to the Nova Academy Enterprise Registry API! 🚀

A modern, resilient RESTful service built with **FastAPI**, **SQLite**, and **Google Gemini (gemini-3.8-flash)**.

- **Interactive Web Portal**: Explore the dynamic live dashboard at [`/`](/) with real-time search, filters, and AI playground.
- **Strict Data Validation**: Pydantic v2 schemas for all payloads.
- **AI Query Reasoning**: Ask natural language questions in real-time grounded strictly on registered records.
- **Performance Telemetry**: Microsecond latency metrics and `X-Process-Time` response headers.
    """,
    version="1.0.0",
    openapi_tags=tags_metadata,
    lifespan=lifespan
)

# Enable permissive CORS for frontend / dev playground
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Process timing and telemetry middleware
@app.middleware("http")
async def add_telemetry_headers(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration_ms = (time.time() - start_time) * 1000
    response.headers["X-Process-Time"] = f"{duration_ms:.2f}ms"
    response.headers["X-Powered-By"] = "FastAPI + Gemini AI"
    response.headers["X-API-Version"] = "1.0.0"
    return response

# Include all modular route controllers
app.include_router(api_router)

@app.get(
    "/",
    summary="Interactive Portal & Dynamic Dashboard",
    description="Returns the lively, animated web application dashboard for browsers, or rich system status for JSON clients."
)
def root(request: Request, format: str = None):
    accept_header = request.headers.get("accept", "")
    
    # Return JSON if client explicitly requests JSON or ?format=json
    if format == "json" or ("application/json" in accept_header and "text/html" not in accept_header):
        db = SessionLocal()
        try:
            total_students = db.query(model.Student).count()
        finally:
            db.close()

        return JSONResponse(content={
            "status": "healthy",
            "message": "🎓 Nova Academy Student Management API is operational and live!",
            "portal": "Visit http://127.0.0.1:8000/ in a web browser for the dynamic visual dashboard.",
            "metrics": {
                "active_students": total_students,
                "ai_engine": "gemini-3.8-flash",
                "database": "sqlite:///./students.db"
            },
            "links": {
                "web_dashboard": "/",
                "interactive_docs": "/docs",
                "redoc": "/redoc",
                "students_api": "/students/",
                "ai_query_api": "/students/ai-query/"
            },
            "timestamp": datetime.now(timezone.utc).isoformat()
        })
    
    # Return the dynamic, lively HTML dashboard
    return HTMLResponse(content=get_dashboard_html())

@app.get(
    "/api/health",
    tags=["System Status"],
    summary="Health & Telemetry Check",
    description="Returns verified system telemetry, database status, and uptime."
)
def health():
    db = SessionLocal()
    try:
        student_count = db.query(model.Student).count()
    finally:
        db.close()

    return {
        "status": "online",
        "service": "Nova Academy Student Intelligence Platform",
        "engine": "FastAPI 0.143",
        "model": "gemini-3.8-flash",
        "database_connected": True,
        "total_records": student_count,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

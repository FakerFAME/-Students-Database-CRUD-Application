from fastapi import APIRouter
from . import create_student, get_student, update_student, delete_student, ai_query

api_router = APIRouter()

api_router.include_router(create_student.router, prefix="/students", tags=["Students CRUD"])
api_router.include_router(get_student.router, prefix="/students", tags=["Students CRUD"])
api_router.include_router(update_student.router, prefix="/students", tags=["Students CRUD"])
api_router.include_router(delete_student.router, prefix="/students", tags=["Students CRUD"])
api_router.include_router(ai_query.router, prefix="/students", tags=["AI Natural Language Query"])

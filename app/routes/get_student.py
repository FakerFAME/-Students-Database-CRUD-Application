from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import schemas, model, database

router = APIRouter()

@router.get("/", response_model=List[schemas.StudentResponse])
def get_students(course: Optional[str] = None, skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    query = db.query(model.Student)
    if course:
        query = query.filter(model.Student.course == course)
    return query.offset(skip).limit(limit).all()

@router.get("/{student_id}", response_model=schemas.StudentResponse)
def get_student(student_id: int, db: Session = Depends(database.get_db)):
    student = db.query(model.Student).filter(model.Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return student

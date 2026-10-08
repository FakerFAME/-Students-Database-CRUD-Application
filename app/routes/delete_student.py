from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, model, database

router = APIRouter()

@router.delete("/{student_id}", status_code=status.HTTP_200_OK)
def delete_student(student_id: int, db: Session = Depends(database.get_db)):
    db_student = db.query(model.Student).filter(model.Student.id == student_id).first()
    if not db_student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    
    deleted_name = db_student.student_name
    db.delete(db_student)
    db.commit()
    return {
        "status": "success",
        "message": f"Successfully deleted record for {deleted_name} (ID #{student_id})",
        "deleted_id": student_id,
        "student_name": deleted_name,
        "detail": f"Student '{deleted_name}' deleted successfully"
    }


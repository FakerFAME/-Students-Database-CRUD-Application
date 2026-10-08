from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class StudentBase(BaseModel):
    student_name: str = Field(
        ...,
        description="Full legal name of the student",
        examples=["Aria Chen"]
    )
    date_of_birth: str = Field(
        ...,
        description="Date of birth formatted as ISO 8601 (YYYY-MM-DD)",
        examples=["2003-05-14"]
    )
    email: EmailStr = Field(
        ...,
        description="Unique institutional or personal email address",
        examples=["aria.chen@nexus.edu"]
    )
    phone: str = Field(
        ...,
        description="Contact phone number including country code",
        examples=["+1-415-555-0199"]
    )
    course: Optional[str] = Field(
        default=None,
        description="Academic program, major, or enrolled course",
        examples=["Quantum Computing & AI"]
    )
    address: Optional[str] = Field(
        default=None,
        description="Residential address or campus dormitory specification",
        examples=["Suite 404, Ada Lovelace Hall, Cambridge"]
    )
    enrollment_date: Optional[str] = Field(
        default=None,
        description="Date of initial matriculation or enrollment (YYYY-MM-DD)",
        examples=["2024-09-01"]
    )

class StudentCreate(StudentBase):
    model_config = {
        "json_schema_extra": {
            "example": {
                "student_name": "Aria Chen",
                "date_of_birth": "2003-05-14",
                "email": "aria.chen@nexus.edu",
                "phone": "+1-415-555-0199",
                "course": "Quantum Computing & AI",
                "address": "Suite 404, Ada Lovelace Hall, Cambridge",
                "enrollment_date": "2024-09-01"
            }
        }
    }

class StudentUpdate(BaseModel):
    student_name: Optional[str] = Field(None, description="Updated full legal name", examples=["Aria Chen-Vance"])
    date_of_birth: Optional[str] = Field(None, description="Updated date of birth (YYYY-MM-DD)", examples=["2003-05-14"])
    email: Optional[EmailStr] = Field(None, description="Updated email address", examples=["aria.vance@nexus.edu"])
    phone: Optional[str] = Field(None, description="Updated contact phone number", examples=["+1-415-555-0288"])
    course: Optional[str] = Field(None, description="Updated course or academic department", examples=["Autonomous Systems & Robotics"])
    address: Optional[str] = Field(None, description="Updated residential address", examples=["Building 7, Innovation District, Boston"])
    enrollment_date: Optional[str] = Field(None, description="Updated enrollment date (YYYY-MM-DD)", examples=["2024-09-01"])

    model_config = {
        "json_schema_extra": {
            "example": {
                "course": "Autonomous Systems & Robotics",
                "phone": "+1-415-555-0288",
                "address": "Building 7, Innovation District, Boston"
            }
        }
    }

class StudentResponse(StudentBase):
    id: int = Field(..., description="System assigned unique integer primary key", examples=[1])

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "example": {
                "id": 1,
                "student_name": "Aria Chen",
                "date_of_birth": "2003-05-14",
                "email": "aria.chen@nexus.edu",
                "phone": "+1-415-555-0199",
                "course": "Quantum Computing & AI",
                "address": "Suite 404, Ada Lovelace Hall, Cambridge",
                "enrollment_date": "2024-09-01"
            }
        }
    }

class AIQueryRequest(BaseModel):
    question: str = Field(
        ...,
        description="Natural language question to ask the neural model against the student database",
        examples=["Which students are enrolled in Quantum Computing & AI?"]
    )

    model_config = {
        "json_schema_extra": {
            "example": {
                "question": "Which students are enrolled in Quantum Computing & AI?"
            }
        }
    }

class AIQueryResponse(BaseModel):
    question: str = Field(..., description="The verbatim inquiry submitted for reasoning", examples=["Which students are enrolled in Quantum Computing & AI?"])
    answer: str = Field(..., description="AI response synthesized strictly from database records", examples=["Aria Chen is currently enrolled in Quantum Computing & AI."])
    records_considered: int = Field(..., description="Total student records synthesized during reasoning context construction", examples=[1])
    status: Optional[str] = Field("success", description="Status of the reasoning process", examples=["success"])
    timestamp: Optional[str] = Field(None, description="ISO timestamp of reasoning synthesis", examples=["2024-09-01T12:00:00Z"])
    execution_time_ms: Optional[float] = Field(None, description="Inference latency in milliseconds", examples=[342.5])
    model_name: Optional[str] = Field(None, description="Gemini model employed for synthesis", examples=["gemini-3.8-flash"])

    model_config = {
        "json_schema_extra": {
            "example": {
                "question": "Which students are enrolled in Quantum Computing & AI?",
                "answer": "✨ **Academic Intelligence Report** 🎓\n\n* **Aria Chen** is enrolled in **Quantum Computing & AI** (Enrolled: 2024-09-01).\n* **Zara Washington** is also enrolled in **Quantum Computing & AI** (Enrolled: 2024-09-01).\n\n💡 *Advisor Insight:* Both students share the exact same matriculation date!",
                "records_considered": 6,
                "status": "success",
                "timestamp": "2024-09-01T12:00:00Z",
                "execution_time_ms": 342.5,
                "model_name": "gemini-3.8-flash"
            }
        }
    }



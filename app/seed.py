from sqlalchemy.orm import Session
from . import model

INITIAL_STUDENTS = [
    {
        "student_name": "Aria Chen",
        "date_of_birth": "2003-05-14",
        "email": "aria.chen@nexus.edu",
        "phone": "+1-415-555-0199",
        "course": "Quantum Computing & AI",
        "address": "Suite 404, Ada Lovelace Hall, Cambridge",
        "enrollment_date": "2024-09-01"
    },
    {
        "student_name": "Liam Gallagher",
        "date_of_birth": "2002-11-20",
        "email": "liam.g@nexus.edu",
        "phone": "+1-206-555-0144",
        "course": "Cybersecurity & Cryptography",
        "address": "742 Evergreen Terrace, Seattle",
        "enrollment_date": "2023-09-15"
    },
    {
        "student_name": "Maya Patel",
        "date_of_birth": "2004-02-18",
        "email": "maya.patel@nexus.edu",
        "phone": "+1-617-555-0182",
        "course": "Machine Learning & Robotics",
        "address": "Unit 12B, Turing Tower, Boston",
        "enrollment_date": "2024-01-10"
    },
    {
        "student_name": "Mateo Rodriguez",
        "date_of_birth": "2001-08-30",
        "email": "mateo.r@nexus.edu",
        "phone": "+1-312-555-0167",
        "course": "Cloud Architecture & DevOps",
        "address": "312 Michigan Ave, Chicago",
        "enrollment_date": "2023-08-25"
    },
    {
        "student_name": "Zara Washington",
        "date_of_birth": "2003-12-05",
        "email": "zara.w@nexus.edu",
        "phone": "+1-212-555-0191",
        "course": "Quantum Computing & AI",
        "address": "88 Wall Street, New York",
        "enrollment_date": "2024-09-01"
    },
    {
        "student_name": "Ethan Hunt",
        "date_of_birth": "2002-04-12",
        "email": "ethan.hunt@nexus.edu",
        "phone": "+1-415-555-0177",
        "course": "Cybersecurity & Cryptography",
        "address": "Suite 909, Cyber Operations Lab, San Francisco",
        "enrollment_date": "2023-09-15"
    }
]

def seed_database_if_empty(db: Session):
    count = db.query(model.Student).count()
    if count == 0:
        for s in INITIAL_STUDENTS:
            student = model.Student(**s)
            db.add(student)
        db.commit()
        return len(INITIAL_STUDENTS)
    return count

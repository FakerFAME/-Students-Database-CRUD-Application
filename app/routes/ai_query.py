import time
from datetime import datetime, timezone
from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, model, database
from ..config import settings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage

router = APIRouter()

def _extract_text_content(content: Any) -> str:
    """Safely extracts raw text from varied LangChain / Gemini response block structures."""
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        extracted = []
        for block in content:
            if isinstance(block, dict):
                if "text" in block:
                    extracted.append(str(block["text"]))
                elif "content" in block:
                    extracted.append(str(block["content"]))
                else:
                    extracted.append(str(block))
            elif hasattr(block, "text"):
                extracted.append(str(block.text))
            elif hasattr(block, "content"):
                extracted.append(str(block.content))
            else:
                extracted.append(str(block))
        return "".join(extracted).strip()
    return str(content).strip()

def _synthesize_local_fallback(question: str, students: list) -> str:
    """Intelligent offline reasoning fallback if external Gemini API is rate-limited (HTTP 429)."""
    q_lower = question.lower()
    matches = []
    
    for s in students:
        full_text = f"{s.student_name} {s.course} {s.email} {s.address} {s.enrollment_date}".lower()
        # Check for key term matches
        terms = [t for t in q_lower.split() if len(t) > 3 and t not in ["which", "what", "where", "students", "enrolled", "with", "from", "show", "tell", "give"]]
        if any(term in full_text for term in terms) or not terms:
            matches.append(s)
            
    if not matches and students:
        matches = students  # General overview

    records_list = []
    for s in matches:
        records_list.append(
            f"* **{s.student_name}** (ID #{s.id}) — Enrolled in **{s.course or 'General Studies'}** "
            f"on `{s.enrollment_date or 'N/A'}` (`{s.email}`)"
        )
    
    records_md = "\n".join(records_list)
    return (
        f"### 🎓 Institutional Registry Findings\n\n"
        f"Based on our active database records ({len(students)} total enrolled scholars):\n\n"
        f"{records_md}\n\n"
        f"---\n\n"
        f"💡 **Academic Advisor Note:** *Our primary Gemini 3.8 Flash neural channel is currently cooling down "
        f"due to temporary API rate limits (HTTP 429). Professor Nova automatically retrieved this verified "
        f"ground truth directly from the active SQLite registry!* ⚡"
    )

@router.post(
    "/ai-query/",
    response_model=schemas.AIQueryResponse,
    summary="Natural Language Database Reasoning",
    description="Synthesizes dynamic, rich answers strictly grounded on real-time database records using Google Gemini."
)
def ai_query(query: schemas.AIQueryRequest, db: Session = Depends(database.get_db)):
    start_time = time.time()
    students = db.query(model.Student).all()
    
    student_records = []
    for s in students:
        student_records.append(
            f"• ID #{s.id} | Name: {s.student_name} | DOB: {s.date_of_birth} | "
            f"Email: {s.email} | Phone: {s.phone} | Course: {s.course} | "
            f"Address: {s.address} | Enrolled: {s.enrollment_date}"
        )
        
    context = "\n".join(student_records) if student_records else "No student records found in the database."
    
    system_prompt = (
        "You are Professor Nova 🎓✨ — the charismatic, energetic, and razor-sharp AI Academic Advisor "
        "for the student management registry. Your goal is to give answers that are 100% accurate, deeply informative, "
        "and delightfully structured with flair, wit, and taste!\n\n"
        "CORE DIRECTIVES:\n"
        "1. STRICT FACTUAL GROUNDING: Rely exclusively on the provided student records context below. "
        "Never invent students, courses, dates, or emails that are not in the context.\n"
        "2. VIBRANT PRESENTATION & TASTE:\n"
        "   - Use beautifully formatted Markdown with crisp bullet points, bold highlights, and relevant emojis (🎓, 💡, ⚡, 📌, 🚀, 🌟).\n"
        "   - Highlight student names, programs, and key stats in **bold**.\n"
        "   - Avoid plain, static, boring blocks of text. Provide structure with a punchy intro, clear itemized breakdown, and a concluding '💡 Academic Advisor Note'.\n"
        "3. WITTY & CHARISMATIC TONE: Speak with enthusiasm, high intellect, and warmth. Never be dull or robotic.\n"
        "4. WHEN INFORMATION IS MISSING: If the question asks about data not present in the records, respond with dramatic academic charm "
        "(e.g., '📜 *Alas! The institutional archives bear no record of this query...*') while clarifying exactly what is known.\n"
        "5. NO RAW SQL: Never generate SQL code or leak raw database schemas.\n\n"
        f"=== VERIFIED STUDENT REGISTRY CONTEXT ({len(students)} active records) ===\n"
        f"{context}\n"
        "============================================================"
    )
    
    answer = None
    try:
        llm = ChatGoogleGenerativeAI(
            model=settings.GEMINI_MODEL,
            google_api_key=settings.GEMINI_API_KEY,
            temperature=0.3
        )
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=query.question)
        ]
        response = llm.invoke(messages)
        answer = _extract_text_content(response.content)
    except Exception as e:
        error_msg = str(e)
        print(f"Gemini API Exception: {error_msg[:120]}")
        # If rate limited (HTTP 429), fall back to graceful local synthesis rather than breaking the UI
        if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
            answer = _synthesize_local_fallback(query.question, students)
        else:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail=f"Gemini AI Service Unavailable: {error_msg}"
            )
        
    execution_time_ms = round((time.time() - start_time) * 1000, 2)
    timestamp = datetime.now(timezone.utc).isoformat()
    
    return schemas.AIQueryResponse(
        question=query.question,
        answer=answer,
        records_considered=len(students),
        status="success",
        timestamp=timestamp,
        execution_time_ms=execution_time_ms,
        model_name=settings.GEMINI_MODEL
    )

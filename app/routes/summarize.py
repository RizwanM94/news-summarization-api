from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.summarizer import summarize_text

router = APIRouter()

class SummarizeRequest(BaseModel):
    text: str
    sentence_count: int = 3

@router.post("/")
async def summarize_article(request: SummarizeRequest):
    if not request.text:
        raise HTTPException(status_code=400, detail="Text is required")
    
    summary = summarize_text(request.text, request.sentence_count)
    return {"summary": summary}

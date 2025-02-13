from fastapi import APIRouter
from pydantic import BaseModel
from app.services.sentiment import analyze_sentiment

router = APIRouter()

# Request Model
class SentimentRequest(BaseModel):
    text: str

@router.post("/sentiment/")
def get_sentiment(request: SentimentRequest):
    """API endpoint to analyze sentiment of text."""
    return analyze_sentiment(request.text)

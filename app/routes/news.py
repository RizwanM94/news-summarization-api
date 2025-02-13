from fastapi import APIRouter, Query
from app.utils.news_fetcher import fetch_news

router = APIRouter()

@router.get("/")
def get_news(country: str = "us", category: str = "technology"):
    """Fetch news based on country and category"""
    news = fetch_news(country, category)
    return {"news": news}

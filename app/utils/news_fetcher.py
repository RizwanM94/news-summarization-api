import httpx
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"

def fetch_news(country: str = "us", category: str = "technology"):
    """Fetch latest news from NewsAPI"""
    params = {
        "country": country,
        "category": category,
        "apiKey": NEWS_API_KEY
    }
    try:
        response = httpx.get(NEWS_API_URL, params=params)
        response.raise_for_status()
        return response.json().get("articles", [])  # Extract only articles
    except httpx.HTTPStatusError as e:
        return {"error": f"Failed to fetch news: {str(e)}"}

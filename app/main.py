from fastapi import FastAPI
from app.routes import analyze, news, summarize

app = FastAPI(title="News Summarization API", description="Fetch, summarize, and analyze news articles.")

# Include route files
app.include_router(news.router, prefix="/news", tags=["News"])

app.include_router(summarize.router, prefix="/summarize", tags=["Summarization"])
app.include_router(analyze.router, prefix="/analyze", tags=["Sentiment Analysis"])

@app.get("/")
def home():
    return {"message": "Welcome to the News Summarization API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)

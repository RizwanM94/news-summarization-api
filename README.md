# 📰 News Summarization API

A FastAPI-based News Summarization and Sentiment Analysis API that fetches news, summarizes articles, and analyzes sentiment.

## 🚀 Features
- Fetch latest news articles
- Summarize news content
- Perform sentiment analysis using VADER

## 🛠️ Installation

### 1️⃣ Clone the repository

git clone https://github.com/YOUR_GITHUB_USERNAME/news-summarization-api.git
cd news-summarization-api

###  Create Virtual Environment
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate  # On Windows

### Install Dependencies
pip install -r requirements.txt

### Download Required NLTK Data
python -m nltk.downloader vader_lexicon

### Running the API
uvicorn app.main:app --reload
Then open http://127.0.0.1:8000/docs to test the API.


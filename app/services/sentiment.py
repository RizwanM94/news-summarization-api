from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize VADER
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    """Analyze sentiment of the given text using VADER."""
    sentiment_score = sia.polarity_scores(text)
    return {
        "text": text,
        "positive": sentiment_score["pos"],
        "neutral": sentiment_score["neu"],
        "negative": sentiment_score["neg"],
        "compound": sentiment_score["compound"],  # Overall sentiment score
    }

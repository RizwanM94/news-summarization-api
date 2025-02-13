import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("NEWS_API_KEY")

if api_key:
    print(f"API Key Loaded: {api_key[:5]}********")  # Masked for security
else:
    print("API Key NOT found! Check your .env file.")

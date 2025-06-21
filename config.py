# config.py
from dotenv import load_dotenv
import os

load_dotenv()  # reads .env

TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
POLYGON_API_KEY       = os.getenv("POLYGON_API_KEY")
FINNHUB_API_KEY       = os.getenv("FINNHUB_API_KEY")

assert all([TWITTER_BEARER_TOKEN, POLYGON_API_KEY, FINNHUB_API_KEY]), \
    "Missing one or more API keys in .env"

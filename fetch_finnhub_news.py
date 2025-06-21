# fetch_finnhub_news.py
import finnhub
from config import FINNHUB_API_KEY

client = finnhub.Client(api_key=FINNHUB_API_KEY)

def get_finnhub_news(category="general"):
    return client.general_news(category, min_id=0)[:5]

if __name__ == "__main__":
    for article in get_finnhub_news():
        print(f"{article['headline']} — {article['datetime']}")

# fetch_polygon_news.py
import requests
from config import POLYGON_API_KEY

def get_polygon_news(limit=5):
    url = "https://api.polygon.io/v2/reference/news"
    params = {"limit": limit, "apiKey": POLYGON_API_KEY}
    r = requests.get(url, params=params)
    r.raise_for_status()
    return r.json().get("results", [])

if __name__ == "__main__":
    for item in get_polygon_news():
        print(f"{item['title']} — {item['published_utc']}")

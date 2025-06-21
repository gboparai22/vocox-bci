# fetch_tweets.py
import requests
from config import TWITTER_BEARER_TOKEN

def get_recent_tweets(query, max_results=5):
    url = "https://api.twitter.com/2/tweets/search/recent"
    headers = {"Authorization": f"Bearer {TWITTER_BEARER_TOKEN}"}
    params  = {"query": query, "max_results": max_results}
    r = requests.get(url, headers=headers, params=params)
    r.raise_for_status()
    return r.json().get("data", [])

if __name__ == "__main__":
    for t in get_recent_tweets("stocks OR crypto"):
        print(f"{t['text']}\n")

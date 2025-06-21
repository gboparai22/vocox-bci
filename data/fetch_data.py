# data/fetch_data.py
import yfinance as yf
import os

os.makedirs("data", exist_ok=True)

def fetch_spy(days=7):
    """
    Fetches the last `days` days of 1m SPY data,
    because Yahoo limits 1m bars to ~7 days per request.
    """
    df = yf.download("SPY", period=f"{days}d", interval="1m", auto_adjust=True)
    path = f"data/SPY_{days}d_1m.csv"
    df.to_csv(path)
    print(f"Saved {len(df)} rows to {path}")

if __name__ == "__main__":
    fetch_spy(7)
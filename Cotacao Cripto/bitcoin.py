import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"

params = {
    "vs_currency": "usd",
    "days": "max"
}

response = requests.get(url, params=params)
data = response.json()
df = pd.DataFrame(data["prices"], columns=["timestamp", "price"])
df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
df = df.set_index("date")
df_month = df["price"].resample("M").last()
print(df_month)
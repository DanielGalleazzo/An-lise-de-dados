import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import polars as pl
moeda = "bitcoin"
url = "https://api.coingecko.com/api/v3/coins/"+moeda+"/market_chart"

params = {
    "vs_currency": "brl",
    "days": "150 "
}

response = requests.get(url, params=params)
data = response.json()
df = pd.DataFrame(data["prices"], columns=["timestamp", "price"])
df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
df = df.set_index("date")

df_month = df["price"].resample("M").last()


print(df_month)


plt.title(moeda+" 2025-2026")
plt.xlabel("Mês")
plt.ylabel("Valor em USD")
plt.stem(df_month.index, df_month.values)
plt.show()
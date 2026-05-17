import requests
import pandas as pd
import matplotlib.pyplot as plt

def moedaConsulta () :
    moeda1 = "solana"
    moeda2 = "ethereum"
    url1 = "https://api.coingecko.com/api/v3/coins/" + moeda1 + "/market_chart"
    params1 = {
        "vs_currency": "usd",
        "days": "60"
    }
    url2 = "https://api.coingecko.com/api/v3/coins/" + moeda2 + "/market_chart"
    params2 = {
        "vs_currency": "usd",
        "days": "60"
    }
    response1 = requests.get(url1, params=params1)
    response2 = requests.get(url2, params=params2)
    data1 = response1.json()
    data2 = response2.json()
    df1 = pd.DataFrame(data1["prices"], columns=["timestamp", "price"])
    df2 = pd.DataFrame(data2["prices"], columns=["timestamp","price"])
    df1["date"] = pd.to_datetime(df1["timestamp"], unit="ms")
    df2["date"] = pd.to_datetime(df2["timestamp"], unit="ms")
    df1 = df1.set_index("date")
    df2 = df2.set_index("date")
    df_date1 = df1["price"].resample("W").last()
    df_date2 = df2["price"].resample("W").last()
    print(df_date1)
    print(df_date2)
    plt.title(moeda1 + " and " + moeda2 + " 2025-2026")
    plt.xlabel("Mês")
    plt.ylabel("Valor em USD")
    x = df_date1.index
    plt.bar(x - pd.Timedelta(days=2), df_date1.values, 
    width=3, color="red", label=moeda1)
    plt.bar(x + pd.Timedelta(days=2), df_date2.values, 
    width=3, color="blue", label=moeda2)
    plt.show()
    return



moedaConsulta1 = moedaConsulta()
print(moedaConsulta1)



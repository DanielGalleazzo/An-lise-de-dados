import requests
import pandas as pd
import matplotlib.pyplot as plt

def moedaConsulta () :
    moeda1 = "bitcoin"
    url1 = "https://api.coingecko.com/api/v3/coins/" + moeda1 + "/market_chart"
    params1 = {
        "vs_currency": "usd",
        "days": "365"
    }
    response1 = requests.get(url1, params=params1)
    data1 = response1.json()
    df1 = pd.DataFrame(data1["prices"], columns=["timestamp", "price"])
    df1["date"] = pd.to_datetime(df1["timestamp"], unit="ms")
    df1 = df1.set_index("date")
    df_date1 = df1["price"].resample("ME").last()
    print(df_date1)    
    plt.title(moeda1 +" 2025-2026")
    plt.xlabel("Mês")
    plt.ylabel("Valor em USD")
    x = df_date1.index
    plt.bar(x - pd.Timedelta(days=2), df_date1.values, 
    width=3, color="red", label=moeda1)
    plt.show()
    return



moedaConsulta1 = moedaConsulta()
print(moedaConsulta1)



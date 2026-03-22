import requests
import pandas as pd
import matplotlib.pyplot as plt
 
df = pd.read_csv(
    'Dolar_10_anos.csv',
    sep=',',
    encoding='latin1',
    low_memory=False
)
print(df.head())
print(df.columns)
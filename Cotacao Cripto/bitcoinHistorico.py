import requests
import pandas as pd
import matplotlib.pyplot as plt
import os

pd.set_option('display.max_columns', 100)
df = pd.read_csv("C:/Users/Usuario/Documents/GitHub/An-lise-de-dados/Bitcoin_Historico.csv",
sep=';',
encoding='latin1'
)
#print(df.head())
print(df.columns)
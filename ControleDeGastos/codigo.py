import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('teste.csv',)

colunas = df.head()
print(colunas)
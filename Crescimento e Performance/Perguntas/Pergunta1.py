import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(
    'db.csv',
    sep = ',',
    encoding='utf-8-sig'
)

print(df.columns.tolist())

df['Dia'] = pd.to_datetime(df['Dia'])
print(df.head())


MetaPedidos = df["Meta_Pedidos"].sum()
ActualPedidos = df["Pedidos"].sum()
beatPedidos = ActualPedidos/MetaPedidos

print(f"{MetaPedidos:,}")
print(f"{ActualPedidos:,}")
print(f"{beatPedidos:%}")


##

df['Dia'] = pd.to_datetime(df['Dia'])
df['mes'] = df['Dia'].dt.to_period('M')

PedidosAnoActual = df.groupby('mes')['Pedidos'].sum().reset_index()
PedidosAnoPlan = df.groupby('mes')['Meta_Pedidos'].sum().reset_index()
print(PedidosAnoActual)

eixoX = PedidosAnoActual['mes'].astype(str)
plt.plot(eixoX, PedidosAnoActual['Pedidos'],marker='o')
plt.plot(eixoX,PedidosAnoPlan['Meta_Pedidos'],marker = 's')

plt.show()


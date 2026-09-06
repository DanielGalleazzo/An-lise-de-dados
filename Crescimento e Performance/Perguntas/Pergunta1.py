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



"""
conclusão pergunta 1: sim, a operação atingiu a meta do ano de 2025, a maior parte dos pedidos do ano estâo concentrados de janeiro-julho, de agosto para frente mostraram uma
queda porém ainda acima do planejado, em dezembro mostra um indicio de recuperação com o começo do ano. Curiosos é que o planejado em todos os meses cerca de 200k abaixo do actual 
"""
"""
O aumento das horas operacionais está gerando aumento proporcional nos pedidos?
Como a produtividade (pedidos/hora) evoluiu ao longo do ano?
Qual cidade/operação consegue gerar mais pedidos utilizando menos horas?
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(
    "db.csv",
    sep = ",",
    encoding='utf-8-sig'
)


df['Dia'] = pd.to_datetime(df['Dia'])
df['mes'] = df['Dia'].dt.to_period('M')

HorasOperacionaisM = df.groupby('mes')['Horas_Operacionais'].sum().reset_index()
PedidosM = df.groupby('mes')['Pedidos_Por_Hora'].sum().reset_index()

print(HorasOperacionaisM)
print(PedidosM)

eixoX = HorasOperacionaisM['mes'].astype(str)

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(eixoX,HorasOperacionaisM['Horas_Operacionais'],color = 'green', label = "Horas Operacionais")
ax2.plot(eixoX,PedidosM['Pedidos_Por_Hora'],color = 'blue', label = "Pedidos")
ax2.set_ylabel("Pedidos")
ax1.set_ylabel("Horas")
plt.show()





"""
O aumento das horas operacionais está gerando aumento proporcional nos pedidos?
Sim, esse comportamento está muito nítido no segundo semestre, no primeiro semestre parece que temos algo releacionado com a sazonalidade do produto,
dado o fato que as horas operacionais durante o ano não mostram muitas curvas (exceto em fevereiro), porém é nitido que quanto mais horas operacionais, temos mais pedidos,receita, etc

Como a produtividade (pedidos/hora) evoluiu ao longo do ano?
Apresenta uma curva normal de acordo com a empresa, quanto mais horas operacionas trabalhadas, mais pedidos e mais receitas. Porém no final do ano não acontece o mesmo,
temos uma queda muito grande em relação ao H1

Qual cidade/operação consegue gerar mais pedidos utilizando menos horas?

"""
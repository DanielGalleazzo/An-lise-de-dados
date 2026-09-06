import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(
    'db.csv',
    sep = ',',
    encoding='utf-8-sig'
)


df['Dia'] = pd.to_datetime(df['Dia'])
PedidosCidade = df.groupby('Cidade')['Pedidos'].sum().reset_index()
ReceitaCidade = df.groupby('Cidade')['Receita'].sum().reset_index()
df['Receita / Pedidos_Por_Hora'] = df['Receita'] / df['Pedidos_Por_Hora']
ProdutividadeCidade = df.groupby('Cidade')[['Pedidos_Por_Hora','Receita','Receita / Pedidos_Por_Hora']].mean().reset_index()
print(ProdutividadeCidade)
#print(Ordenado)


#plt.bar(PedidosCidade['Cidade'], PedidosCidade['Pedidos'].sort_values())
#plt.bar(ReceitaCidade['Cidade'], ReceitaCidade['Receita'].sort_values())
plt.scatter(ProdutividadeCidade['Cidade'], ProdutividadeCidade['Pedidos_Por_Hora'])
plt.show()


"""
Qual cidade teve maior quantidade de pedidos?
São Paulo

Qual cidade teve maior receita?
São Paulo

Qual cidade apresentou melhor produtividade em pedidos por hora?
BH

Existe alguma cidade que possui muita receita, mas baixa produtividade?
São Paulo e Rio de Janeiro, ambas cidades possuem uma receita maior que 55M e seus pedidos por Hora não mostram tanta diferença quanto Curitba, que possui cerca de 10M a menos
que Rio e quase 20M a menos que SP. Belo Horizonte é a cidade que tem totalmente o contrário, a maior em pedidos por Hora mas a sua receita é a segunda pior, apenas atrás de campinas que é a cidade
com menor pedidos por hora
"""
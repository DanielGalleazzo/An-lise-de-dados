"""
3. Comparação entre operações
Qual operação apresentou melhor desempenho?
Qual operação teve maior atingimento da meta?
Qual operação teve maior taxa de cancelamento?
Existe alguma operação consistentemente abaixo da meta?
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv(
    'db.csv',
    sep= ',',
     encoding='utf-8-sig'
)

OperacaoReceita = df.groupby('Operacao')[['Receita','Pedidos']].sum().reset_index()


OperacaoPedidos = (df.groupby("Operacao")[["Pedidos", "Meta_Pedidos","Pedidos_Cancelados"]].sum().reset_index())

OperacaoPedidos["% Cancelamento"] = (OperacaoPedidos["Pedidos"]/OperacaoPedidos["Pedidos_Cancelados"]) - 1
OperacaoPedidos["Beat or Miss"] = (OperacaoPedidos["Pedidos"] / OperacaoPedidos["Meta_Pedidos"]) - 1

print(OperacaoReceita)
print('--')
print(OperacaoPedidos)



"""
3. Comparação entre operações
Qual operação apresentou melhor desempenho?
Operação A, trouxe a maior receita e a maior quantia de Pedidos em relação a demais, não teve um crescimento muito grande em relação a meta
Qual operação teve maior atingimento da meta?
Operação B, Beat de 3.5% em relação a meta, enquanto a A mostrou o menor atingimento
Qual operação teve maior taxa de cancelamento?
Operação C, mas não foi muito fora da curva em relação as demais
Existe alguma operação consistentemente abaixo da meta?
Não, todas performaram conforme o esperado
"""
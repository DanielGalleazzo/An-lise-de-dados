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
OperacaoPedidos = df.groupby('Operacao')[['Pedidos','Meta_Pedidos']].sum().reset_index()
print(OperacaoReceita)
print(OperacaoPedidos)

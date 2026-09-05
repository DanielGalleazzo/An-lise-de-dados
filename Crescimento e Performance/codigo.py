"""1. Performance geral

A operação atingiu a meta de pedidos ao longo de 2025?
Como a quantidade de pedidos evoluiu durante o ano?
Quais foram os meses de maior e menor volume?

2. Comparação entre cidades

Qual cidade teve maior quantidade de pedidos?
Qual cidade teve maior receita?
Qual cidade apresentou melhor produtividade em pedidos por hora?
Existe alguma cidade que possui muita receita, mas baixa produtividade?

3. Comparação entre operações

Qual operação apresentou melhor desempenho?
Qual operação teve maior atingimento da meta?
Qual operação teve maior taxa de cancelamento?
Existe alguma operação consistentemente abaixo da meta?

4. Eficiência operacional

O aumento das horas operacionais está gerando aumento proporcional nos pedidos?
Como a produtividade (pedidos/hora) evoluiu ao longo do ano?
Qual cidade/operação consegue gerar mais pedidos utilizando menos horas?

5. Receita 💰

Qual cidade gera mais receita?
Qual operação gera mais receita?
Como a receita evoluiu ao longo do ano?
Qual é a receita média por hora?
Existe relação entre produtividade e receita?

6. Cancelamentos ❌

Qual cidade apresenta maior taxa de cancelamento?
Qual operação apresenta maior taxa de cancelamento?
Em quais períodos os cancelamentos aumentaram?
Quando a taxa de cancelamento ficou significativamente acima do normal?
🚨 7. A parte mais interessante: anomalias

Aqui quero que você investigue:

Existe algum período em que a operação apresentou um comportamento anormal?

Tente descobrir:

Quando aconteceu?
Qual cidade foi afetada?
Qual operação foi afetada?
O que aconteceu com os pedidos?
O que aconteceu com as horas trabalhadas?
O que aconteceu com a produtividade?
O que aconteceu com os cancelamentos?
A operação ficou abaixo da meta?

E principalmente:

Você consegue encontrar uma possível explicação para a queda de performance olhando apenas para os dados?

📊 8. Pergunta final

Depois de toda a análise:

Se você fosse responsável pela operação, quais 3 ações tomaria para melhorar os resultados?

Essa última parte é importante porque transforma o projeto de:


Novamente pedi para o GPT me passar um problema e eu quebrar a cabeça com ele, dessa vez é algo mais puxado para o lado de análise de dados e performance, diferente do outro projeto que era algo de
entender a biblioteca e afins, acredito que com o conhecimento daquela documentação eu já consiga ter uma boa base de código em PY

"""


import pandas as pd
import matplotlib as mt
import numpy as np

df = pd.read_csv(
    'operations_performance_analytics.csv',
    sep = ',',
   encoding= 'latin1',
    low_memory= False
)


print(df.head())
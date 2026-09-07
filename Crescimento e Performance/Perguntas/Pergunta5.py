"""

5. Receita 💰
Qual cidade gera mais receita?
SP
Qual operação gera mais receita?
A
Como a receita evoluiu ao longo do ano?

Qual é a receita média por hora?
Existe relação entre produtividade e receita?

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(
    "db.csv",
    sep = ",",
    encoding='utf-8-sig'
)

df['Dia'] = pd.to_datetime(df['Dia'])
df['mes'] = df['Dia'].dt.to_period('M')

ReceitaCidade = df.groupby('Cidade')['Receita'].sum().reset_index()
ReceitaOperacao = df.groupby('Operacao')['Receita'].sum().reset_index()
print(ReceitaCidade)
print(ReceitaOperacao)


ReceitaAno = df.groupby('mes')['Receita'].sum().reset_index()
ReceitaAno['mes'] = ReceitaAno['mes'].astype(str)


print(ReceitaAno)




## to reparando que eu respondi essas perguntas ao decorrer dos exercicios passados, nao vou responder pergunta repetida 
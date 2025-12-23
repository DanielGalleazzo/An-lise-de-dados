import pandas as pd
import numpy as np
import polars as pl
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 100)
#df = pd.read_csv('MICRODADOS_ENEM_ESCOLA.csv') da erro por conta da tabela
df = pd.read_csv(
    'MICRODADOS_ENEM_ESCOLA.csv',
    sep=';',
    encoding='latin1',
    low_memory=False
)
#print("PRIMEIRAS LINHAS:")
#print(df.head())
#print("LINHAS E COLUNAS:")
#print(df.shape)

totalEscolas = df['CO_ESCOLA_EDUCACENSO'].nunique()
#print('Total escolas: ' + str(totalEscolas))
totalEstados = df['SG_UF_ESCOLA'].nunique()
#print('Total estados: ' + str(totalEstados))


print('-----')
escolas_por_uf = (
   df.groupby('SG_UF_ESCOLA')['CO_ESCOLA_EDUCACENSO']
      .nunique()
)

print(escolas_por_uf)
plt.bar(escolas_por_uf.index, escolas_por_uf.values, color="red")
plt.title('Número de Escolas por UF')
plt.xlabel('Sigla da UF (Unidade Federativa)')
plt.ylabel('Número de Escolas')
plt.xticks(rotation=45, ha='right')
plt.show()




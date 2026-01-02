import pandas as pd
import numpy as np
import polars as pl
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 100)
#df = pd.read_csv('MICRODADOS_ENEM_ESCOLA.csv') da erro por conta da tabela
df = pd.read_csv(
    'Microdados_enem_modificado.csv',
    sep=',',
    encoding='latin1',
    low_memory=False
)

#print(df.columns)
#print(df[(df["NU_ANO"] == 2015) & (df["media"] >= 630)] \
  #.groupby("SG_UF_ESCOLA") \
  #.size())  escolas que tiveram uma media maior ou igual a 630 em 2015, somando todas as escolas e agrupando por estado


total2010 = df[(df["NU_ANO"] == 2010) & (df["media"] >= 630)].shape[0] # soma todas a quantidade de escolas que tiveram uma media maior ou igual a 630 em x ano
print(total2010)
total2011 = df[(df["NU_ANO"] == 2011) & (df["media"] >= 630)].shape[0]
print(total2011)
total2012 = df[(df["NU_ANO"] == 2012) & (df["media"] >= 630)].shape[0]
print(total2012)
total2013 = df[(df["NU_ANO"] == 2013) & (df["media"] >= 630)].shape[0]
print(total2013)
total2014 = df[(df["NU_ANO"] == 2014) & (df["media"] >= 630)].shape[0]
print(total2014)
total2015 = df[(df["NU_ANO"] == 2015) & (df["media"] >= 630)].shape[0]
print(total2015)

anos = ('2010', '2011', '2012', '2013', '2014', '2015')
total = (total2010,
         total2011,
         total2012,
         total2013,
         total2014,
         total2015)

plt.title('Escolas com média maior ou igual a 630 pontos')
plt.bar(anos,total) #color = ["grey"])
plt.ylabel('Quantidade de escolas')
plt.xlabel('Ano')
plt.show()








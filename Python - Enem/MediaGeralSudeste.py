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


ano = 2015
sp = "SP"
mg = "MG"
es = "ES"
rj = "RJ"


mediaEscolaSP =df[(df["NU_ANO"] == ano) & (df["SG_UF_ESCOLA"] == sp)]
mediaSP2015 = mediaEscolaSP["media"].mean() # duas formas de fazer, particularmente eu gostei mais da de baixo, utlizando a funcao query()
mediaEscolaMG = df[(df["NU_ANO"] == ano) & (df["SG_UF_ESCOLA"]== mg)]
mediaMG2015 = mediaEscolaMG["media"].mean()


mediaEscolaRJ = (df.query("NU_ANO ==  2015 and SG_UF_ESCOLA == 'RJ'" )["media"].mean())
mediaEscolaES = (df.query("NU_ANO == 2015 and SG_UF_ESCOLA == 'ES'")["media"].mean())


sudeste = (
    mediaSP2015,
    mediaMG2015,
    mediaEscolaRJ,
    mediaEscolaES
)
estados = (sp,mg,rj,es)



plt.title("Média do sudeste em 2015")
plt.ylabel("Média")
plt.xlabel("Estados")
plt.bar(estados,sudeste, color = "grey")
plt.show()


#objetivo desse arquivo: entender como funciona a funcao query e a .mean() O próximo arquivo eu irei fazer comparando todas as regi~poes
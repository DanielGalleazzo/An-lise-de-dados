import pandas as pd
import numpy as np
import polars as pl
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 100)
#df = pd.read_csv('MICRODADOS_ENEM_ESCOLA.csv') da erro por conta da tabela
df = pd.read_csv(
    'Microdados_enem_modificado.csv',
    sep=';',
    encoding='latin1',
    low_memory=False
)
estadosSudeste = df.query("SG_UF_ESCOLA in ('SP', 'RJ', 'ES', 'MG')")
estadosNorte = df.query("SG_UF_ESCOLA in ('AC', 'AM', 'AP', 'RO','RR','TO')")
estadosNordeste = df.query("SG_UF_ESCOLA in ('AL', 'BA', 'CE', 'MA','PB','PE','PI','RN','SE')")
estadosCentroOeste = df.query("SG_UF_ESCOLA in ('GO', 'MT', 'MS', 'DF')")
estadosSul = df.query("SG_UF_ESCOLA in ('RS', 'SC', 'PR')")

escolasSudeste = estadosSudeste['CO_ESCOLA_EDUCACENSO'].nunique()
escolasNorte = estadosNorte['CO_ESCOLA_EDUCACENSO'].nunique()
escolasNordeste = estadosNordeste['CO_ESCOLA_EDUCACENSO'].nunique()
escolasCentroOeste = estadosCentroOeste['CO_ESCOLA_EDUCACENSO'].nunique()
escolasSul = estadosSul['CO_ESCOLA_EDUCACENSO'].nunique()


regioes = ('Sudeste', 'Norte', 'Nordeste', 'Centro-Oeste', 'Sul')
quantidades = (
    escolasSudeste,
    escolasNorte,
    escolasNordeste,
    escolasCentroOeste,
    escolasSul
)

plt.bar(regioes, quantidades, color=['grey','black','red','orange','purple'])
plt.ylabel('Quantidade de escolas')
plt.title('Número de escolas por região')
plt.show()

print('Sudeste: ' + str(escolasSudeste))
print('Norte: ' + str(escolasNorte))
print('Nordeste: ' + str(escolasNordeste))
print('Centro-Oeste:' + str(escolasCentroOeste))
print('Sul: ' + str(escolasSul))

#Para o daniel do futuro: fazer um código que mostre os estados que tiveram a média maior ou igual a 630 (somar as 5 materias lp,mt,cn,ch,rd e dividir por cinco)
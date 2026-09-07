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

#regiaoSudeste = ('SP', 'RJ', 'ES', 'MG')
totalspGrupo1 = df[(df["SG_UF_ESCOLA"] == "SP" ) & (df["INSE"] == "Grupo 1")].shape[0]
totalspGrupo2 = df[(df["SG_UF_ESCOLA"] == "SP" ) & (df["INSE"] == "Grupo 2")].shape[0]
totalspGrupo3 = df[(df["SG_UF_ESCOLA"] == "SP" ) & (df["INSE"] == "Grupo 3")].shape[0]
totalspGrupo4 = df[(df["SG_UF_ESCOLA"] == "SP" ) & (df["INSE"] == "Grupo 4")].shape[0]
totalspGrupo5 = df[(df["SG_UF_ESCOLA"] == "SP" ) & (df["INSE"] == "Grupo 5")].shape[0]
totalspGrupo6 = df[(df["SG_UF_ESCOLA"] == "SP" ) & (df["INSE"] == "Grupo 6")].shape[0]

print("Total de escolas do grupo 1 em São Paulo: " + str(totalspGrupo1))
print("Total de escolas do grupo 2 em São Paulo: " + str(totalspGrupo2))
print("Total de escolas do grupo 3 em São Paulo: " + str(totalspGrupo3))
print("Total de escolas do grupo 4 em São Paulo: " + str(totalspGrupo4))
print("Total de escolas do grupo 5 em São Paulo: " + str(totalspGrupo5))
print("Total de escolas do grupo 6 em São Paulo: " + str(totalspGrupo6))
total = totalspGrupo1 + totalspGrupo2 + totalspGrupo3 + totalspGrupo4 + totalspGrupo5 + totalspGrupo6
print(total)


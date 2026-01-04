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


totalspGrupo1 = df[(df["SG_UF_ESCOLA"] == "SP" ) & (df["INSE"] == "Grupo 1")] ["media"].mean()
totalspGrupo2 = df[(df["SG_UF_ESCOLA"] == "SP" ) & (df["INSE"] == "Grupo 2")] ["media"].mean()
totalspGrupo3 = df[(df["SG_UF_ESCOLA"] == "SP" ) & (df["INSE"] == "Grupo 3")] ["media"].mean()
totalspGrupo4 = df[(df["SG_UF_ESCOLA"] == "SP" ) & (df["INSE"] == "Grupo 4")] ["media"].mean()
totalspGrupo5 = df[(df["SG_UF_ESCOLA"] == "SP" ) & (df["INSE"] == "Grupo 5")] ["media"].mean()
totalspGrupo6 = df[(df["SG_UF_ESCOLA"] == "SP" ) & (df["INSE"] == "Grupo 6")] ["media"].mean()

print(totalspGrupo1)
print(totalspGrupo2)
print(totalspGrupo3)
print(totalspGrupo4)
print(totalspGrupo5)
print(totalspGrupo6)

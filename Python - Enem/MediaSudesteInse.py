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
totalrjGrupo1 = df[(df["SG_UF_ESCOLA"] == "RJ" ) & (df["INSE"] == "Grupo 1")] ["media"].mean()
totalrjGrupo2 = df[(df["SG_UF_ESCOLA"] == "RJ" ) & (df["INSE"] == "Grupo 2")] ["media"].mean()
totalrjGrupo3 = df[(df["SG_UF_ESCOLA"] == "RJ" ) & (df["INSE"] == "Grupo 3")] ["media"].mean()
totalrjGrupo4 = df[(df["SG_UF_ESCOLA"] == "RJ" ) & (df["INSE"] == "Grupo 4")] ["media"].mean()
totalrjGrupo5 = df[(df["SG_UF_ESCOLA"] == "RJ" ) & (df["INSE"] == "Grupo 5")] ["media"].mean()
totalrjGrupo6 = df[(df["SG_UF_ESCOLA"] == "RJ" ) & (df["INSE"] == "Grupo 6")] ["media"].mean()




SaoPaulo = (( totalspGrupo1 +
            totalspGrupo2 +
            totalspGrupo3 +
            totalspGrupo4 +
            totalspGrupo5 +
            totalspGrupo6 ) /6 )
RioJaneiro = ((totalrjGrupo1+
               totalrjGrupo2+
               totalrjGrupo3+
               totalrjGrupo4+
               totalrjGrupo5+
               totalrjGrupo6) / 6)

print(SaoPaulo)
print(RioJaneiro)
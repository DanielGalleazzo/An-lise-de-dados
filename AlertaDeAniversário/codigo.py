import pandas as pd
import numpy as np
import csv as csv
from datetime import datetime as date

df = pd.read_csv (
    'ListaAniversario.csv',
    sep=',',
    encoding= 'latin1',
    low_memory= False
)
hoje = date.now().strftime("%d/%m")

for valor in df['Aniversario']:
    print(valor)

if str(valor) == hoje:
    aniversariante = df.loc[df['Aniversario']== hoje, 'Nome']
    print("Feliz aniversario para: " + aniversariante.iloc[0])
else:
    print("Nao tem aniversariante hoje :(")  #vasco ref uber

  
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
print(hoje)

for valor in df['Aniversario']:
    print(valor)

    if str(hoje) in valor:
        print("Temos um aniversariante")

  
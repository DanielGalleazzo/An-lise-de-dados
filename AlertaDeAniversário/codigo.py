import pandas as pd
import numpy as np
import csv as csv
import datetime as date

df = pd.read_csv (
    'ListaAniversario.csv',
    sep=',',
    encoding= 'latin1',
    low_memory= False
)
print(df.head())
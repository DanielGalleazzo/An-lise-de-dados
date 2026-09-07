import pandas as pd
import matplotlib as plot
import numpy as np


df = pd.read_csv (
    'PibDosMunicipios.csv',
    sep =';',
    encoding='latin-1'
)

print(df.tail())

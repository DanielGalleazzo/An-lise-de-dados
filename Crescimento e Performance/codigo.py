import pandas as pd
import matplotlib as mt
import numpy as np

df = pd.read_csv(
    'operations_performance_analytics.csv',
    sep = ',',
   encoding= 'latin1',
    low_memory= False
)


print(df.head())
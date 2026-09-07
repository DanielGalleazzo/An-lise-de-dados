"""
6. Cancelamentos ❌
Qual cidade apresenta maior taxa de cancelamento?
SP
Qual operação apresenta maior taxa de cancelamento?
B
Em quais períodos os cancelamentos aumentaram?
Maio e Outubro
Quando a taxa de cancelamento ficou significativamente acima do normal?
Maio, outubro e novembro
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(
    "db.csv",
    sep = ",",
    encoding='utf-8-sig'
)

df['Dia'] = pd.to_datetime(df['Dia'])
df['mes'] = df['Dia'].dt.to_period('M')

TaxaCancelamento = df.groupby('mes')['Taxa_Cancelamento_Pct'].mean().reset_index()
TaxaCancelamento['mes'] = TaxaCancelamento['mes'].astype(str)

plt.plot(TaxaCancelamento['mes'],TaxaCancelamento['Taxa_Cancelamento_Pct'])
plt.show()
print(TaxaCancelamento)
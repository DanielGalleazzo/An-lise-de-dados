import requests
import pandas as pd
import matplotlib.pyplot as plt
 
dados = pd.read_csv(
    'Cotacao Cripto/NovoArquivoConvertidoTeste2.csv',
    sep=',',
    encoding='latin1',
    low_memory=False
)
print(dados.head)




df = pd.DataFrame(dados)
df['Data'] = pd.to_datetime(df['Data'])
df_mensal = df.groupby(df['Data'].dt.to_period('M'))['Maxima'].mean().reset_index()
print(df_mensal)


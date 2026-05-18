import requests
import pandas as pd
import matplotlib.pyplot as plt
 
dados = pd.read_csv(
    'Dolar 2013-2019 - USD_BRL Dados Históricos (4) (1).csv',
    sep=',',
    encoding='latin1',
    low_memory=False
)



dados['Data'] = pd.to_datetime(
    dados['Data'],
    format = '%d/%m/%Y'
)

dados['Data'] = dados ['Data'].dt.strftime('%m/%d/%Y')

dados.to_csv('NovoArquivoConvertidoTeste2.csv',index=False)
 

#df = pd.DataFrame(dados)
#df['Data'] = pd.to_datetime(df['Data'])
#df_mensal = df.groupby(df['Data'].dt.to_period('M'))

#print(df_mensal)
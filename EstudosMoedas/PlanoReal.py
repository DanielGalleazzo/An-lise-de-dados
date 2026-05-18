import pandas as pd
import matplotlib.pyplot as plt
 

df = pd.read_csv(
    'NovoArquivoConvertidoTeste111 - NovoArquivoConvertidoTeste111.csv',
    sep=',',
    encoding='latin1',
    low_memory=False
)


df['Data'] = pd.to_datetime(df['Data'])
df.set_index('Data', inplace=True)


columns_to_convert = ['Abertura', 'Maxima', 'Minima', 'Ultimo']
for col in columns_to_convert:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace('.', '', regex=False)
        .str.replace(',', '.', regex=False)
        .astype(float)
    )


df_mes = pd.DataFrame({
    'Ultimo': df.resample('M')['Ultimo'].mean(),
    'Abertura': df.resample('M')['Abertura'].mean(),
    'Maxima': df.resample('M')['Maxima'].mean(),
    'Minima': df.resample('M')['Minima'].mean()
})

df_mes.dropna(inplace=True)


plt.figure(figsize=(12, 6))

plt.plot(df_mes.index, df_mes['Ultimo'], color='black', label='Média de Fechamento')
plt.plot(df_mes.index, df_mes['Maxima'], color='red', alpha=0.5, linestyle='--', label='Média de Máximas')
plt.plot(df_mes.index, df_mes['Minima'], color='blue', alpha=0.5, linestyle='--', label='Média de Mínimas')
plt.plot(df_mes.index, df_mes['Abertura'], color='green', alpha=0.5, linestyle='--', label='Média de Aberturas')

plt.title('Média mensal do dólar')
plt.xlabel('Mês')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)
plt.show()

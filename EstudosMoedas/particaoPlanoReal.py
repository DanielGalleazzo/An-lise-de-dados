#https://docs.google.com/presentation/d/17LccGTbcWm21jAqUT2d8AQ5lceju32Dg9lGQKJ4vyIU/edit?slide=id.p#slide=id.p

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


dataInicial = '2018-01-01' 
dataFinal = '2022-01-01' 

filtro = (df.index >= dataInicial) & (df.index <= dataFinal)
df_filtrado = df[filtro]

df_mes = pd.DataFrame({
    'Ultimo': df_filtrado.resample('ME')['Ultimo'].mean()
})

df_mes.dropna(inplace=True)


plt.figure(figsize=(12, 6))

plt.plot(df_mes.index, df_mes['Ultimo'], color='black')

plt.title('Média mensal do dólar')
plt.xlabel('Mês')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)
plt.show()


#https://docs.google.com/presentation/d/17LccGTbcWm21jAqUT2d8AQ5lceju32Dg9lGQKJ4vyIU/edit?slide=id.g3f1b5cc0a1c_1_18#slide=id.g3f1b5cc0a1c_1_18
#apresentação
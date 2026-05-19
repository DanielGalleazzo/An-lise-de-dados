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


df_mes = pd.DataFrame({
    'Ultimo': df.resample('ME')['Ultimo'].mean()
})

df_mes.dropna(inplace=True)


plt.figure(figsize=(12, 6))

plt.plot(df_mes.index, df_mes['Ultimo'], color='black')


plt.axvspan(
    pd.Timestamp('1994-07-01'),
    pd.Timestamp('1995-01-01'),
    color='cyan',
    alpha=0.2,
    label='Governo Itamar'
)
plt.axvspan(
    pd.Timestamp('1995-01-02'),
    pd.Timestamp('2003-01-01'),
    color='gray',
    alpha=0.2,
    label='Governo FHC'
)

plt.axvspan(
    pd.Timestamp('2003-01-02'),
    pd.Timestamp('2010-12-31'),
    color='darkred',
    alpha=0.2,
    label='Primeiro Governo Lula'
)
plt.axvspan(
    pd.Timestamp('2011-01-01'),
    pd.Timestamp('2016-08-31'),
    color='pink',
    alpha=0.2,
    label='Mandato da Dilma'
)

plt.axvspan(
    pd.Timestamp('2016-08-31'),
    pd.Timestamp('2018-12-31'),
    color='blue',
    alpha=0.2,
    label='Mandato do Temer'
)

plt.axvspan(
    pd.Timestamp('2019-01-01'),
    pd.Timestamp('2022-12-31'),
    color='green',
    alpha=0.2,
    label='Mandato do Bolsonaro'
)



plt.axvspan(
    pd.Timestamp('2014-06-12'),
    pd.Timestamp('2014-07-13'),
    color='yellow',
    alpha=0.2,
    label='Copa do Mundo de 2014'
)

plt.axvspan(
    pd.Timestamp('2023-01-01'),
    pd.Timestamp('2026-12-31'),
    color='darkred',
    alpha=0.2,
    label='Segundo Governo Lula'
)





plt.title('Média mensal do dólar')
plt.xlabel('Mês')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)
plt.show()

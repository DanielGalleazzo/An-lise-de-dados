import pandas as pd
import numpy as np
import polars as pl
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 100)
#df = pd.read_csv('MICRODADOS_ENEM_ESCOLA.csv') da erro por conta da tabela
df = pd.read_csv(
    'Microdados_enem_modificado.csv',
    sep=',',
    encoding='latin1',
    low_memory=False
)

ano = 2015
ac = "AC"
al = "AL"
ap = "AP"
am = "AM"
ba = "BA"
ce = "CE"
DF = "DF" # esse daqui é o unico que está em letra maiúscula pq ja teve uma variavel declarada com o nome df antes
es = "ES"
go = "GO"
ma = "MA"
mt = "MT"
ms = "MS"
mg = "MG"
pa = "PA"
pb = "PB"
pr = "PR"
pe = "PE"
pi = "PI"
rj = "RJ"
rn = "RN"
rs = "RS"
ro = "RO"
rr = "RR"
sc = "SC"
sp = "SP"
se = "SE"
to = "TO"



mediaEscolaSP = (df.query("NU_ANO == 2015 and SG_UF_ESCOLA == 'SP'")["media"].mean())
mediaEscolaMG = (df.query("NU_ANO == 2015 and SG_UF_ESCOLA == 'MG'")["media"].mean())
mediaEscolaRJ = (df.query("NU_ANO == 2015 and SG_UF_ESCOLA == 'RJ'")["media"].mean())
mediaEscolaES = (df.query("NU_ANO == 2015 and SG_UF_ESCOLA == 'ES'")["media"].mean())

sudeste = (
    (mediaEscolaSP +
    mediaEscolaMG +
    mediaEscolaRJ +
    mediaEscolaES) / 4
)
estadosSudeste = (sp,mg,rj,es)


#--


mediaEscolaSC = (df.query("NU_ANO == 2015 and SG_UF_ESCOLA == 'SC'")["media"].mean())
mediaEscolaRS = (df.query("NU_ANO == 2015 and SG_UF_ESCOLA == 'RS'")["media"].mean())
mediaEscolaPR = (df.query("NU_ANO == 2015 and SG_UF_ESCOLA == 'PR'")["media"].mean())

sul = (
    (mediaEscolaSC +
    mediaEscolaRS +
    mediaEscolaPR ) / 3
)
estadosSul = (sc,rs,pr)

#--

mediaEscolaGO = (df.query("NU_ANO == 2015 and SG_UF_ESCOLA == 'GO'")["media"].mean())
mediaEscolaMT = (df.query("NU_ANO == 2015 and SG_UF_ESCOLA == 'MT'")["media"].mean())
mediaEscolaMS = (df.query("NU_ANO == 2015 and SG_UF_ESCOLA == 'MS'")["media"].mean())
mediaEscolaDF = (df.query("NU_ANO == 2015 and SG_UF_ESCOLA == 'DF'")["media"].mean())

centroOeste = (
     (mediaEscolaGO +
    mediaEscolaMT + 
    mediaEscolaMS +
    mediaEscolaDF ) / 4
)
estadosCentroOeste = (go,mt,ms,DF)

#--

mediaEscolaAC = (df.query("NU_ANO == 2015 and SG_UF_ESCOLA == 'AC'")["media"].mean())
mediaEscolaAP = (df.query("NU_ANO == 2015 and SG_UF_ESCOLA == 'AP'")["media"].mean())
mediaEscolaAM = (df.query("NU_ANO == 2015 and SG_UF_ESCOLA == 'AM'")["media"].mean())
mediaEscolaPA = (df.query("NU_ANO == 2015 and SG_UF_ESCOLA == 'PA'")["media"].mean())
mediaEscolaRO = (df.query("NU_ANO == 2015 and SG_UF_ESCOLA == 'RO'")["media"].mean())
mediaEscolaRR = (df.query("NU_ANO == 2015 and SG_UF_ESCOLA == 'RR'")["media"].mean())
mediaEscolaTO = (df.query("NU_ANO == 2015 and SG_UF_ESCOLA == 'TO'")["media"].mean())

norte =  ( (mediaEscolaAC + 
       mediaEscolaAP +
       mediaEscolaAM +
       mediaEscolaPA +
       mediaEscolaRO +
       mediaEscolaRR +
       mediaEscolaTO ) / 7)

estadosNorte = (ac,ap,am,pa,ro,rr,to)
#----

mediaEscolaAL = (df.query("NU_ANO == 2015 and SG_UF_ESCOLA == 'AL'")["media"].mean())
mediaEscolaBA = (df.query("NU_ANO == 2015 and SG_UF_ESCOLA == 'BA'")["media"].mean())
mediaEscolaMA = (df.query("NU_ANO == 2015 and SG_UF_ESCOLA == 'CE'")["media"].mean())
mediaEscolaPB = (df.query("NU_ANO == 2015 and SG_UF_ESCOLA == 'PB'")["media"].mean())
mediaEscolaPE = (df.query("NU_ANO == 2015 and SG_UF_ESCOLA == 'PE'")["media"].mean())
mediaEscolaPI = (df.query("NU_ANO == 2015 and SG_UF_ESCOLA == 'PI'")["media"].mean())
mediaEscolaRN = (df.query("NU_ANO == 2015 and SG_UF_ESCOLA == 'RN'")["media"].mean())
mediaEscolaSE = (df.query("NU_ANO == 2015 and SG_UF_ESCOLA == 'SE'")["media"].mean())

nordeste = ( (mediaEscolaAL +
            mediaEscolaBA +
            mediaEscolaMA +
            mediaEscolaPB + 
            mediaEscolaPE +
            mediaEscolaPI +
            mediaEscolaRN +
            mediaEscolaSE) / 8  )
estadosNordeste = (al,ba,ma,pb,pe,pi,rn,se)

print (sudeste, sul,centroOeste,norte,nordeste)

regioes = sudeste,centroOeste,sul,norte,nordeste
regioesNomes = 'Sudeste' , 'Sul', 'Centro-Oeste', 'Norte' , 'Nordeste'


plt.title("Média por região")
plt.xlabel("Região")
plt.ylabel("Média")
plt.bar(regioesNomes, regioes)
plt.show()
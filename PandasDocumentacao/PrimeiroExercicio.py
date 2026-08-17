"""

Claro. Como você acabou de ler o “10 minutes to pandas”, eu faria um exercício de estágio que simula uma tarefa real de tratamento/análise de dados, sem exigir coisas que ainda não aparecem nessa documentação. A documentação cobre criação de DataFrame, inspeção, seleção com loc/iloc, filtros booleanos, isin, operações, ordenação e estatísticas básicas.

🧑‍💻 Exercício — Análise de vendas

Você entrou como estagiário/júnior de dados em uma empresa de e-commerce.

O time comercial te entregou os seguintes dados:

import pandas as pd


dados = {
    "produto": [
        "Notebook", "Mouse", "Teclado", "Monitor",
        "Notebook", "Mouse", "Headset", "Monitor",
        "Teclado", "Notebook"
    ],
    "categoria": [
        "Eletrônicos", "Acessórios", "Acessórios", "Eletrônicos",
        "Eletrônicos", "Acessórios", "Acessórios", "Eletrônicos",
        "Acessórios", "Eletrônicos"
    ],
    "preco": [
        3500, 80, 150, 1200,
        3500, 80, 300, 1200,
        150, 3500
    ],
    "quantidade": [
        2, 10, 5, 3,
        1, 20, 4, 2,
        8, 3
    ],
    "vendedor": [
        "Ana", "Carlos", "Ana", "Bruno",
        "Carlos", "Ana", "Bruno", "Carlos",
        "Ana", "Bruno"
    ]
}


df = pd.DataFrame(dados)
🎯 Tarefa

Seu gerente pediu um pequeno relatório exploratório sobre essas vendas.

1. Inspeção inicial

Mostre:

as 5 primeiras linhas;
as 3 últimas linhas;
o nome das colunas;
os tipos (dtypes);

2. Criação de coluna

Crie uma coluna chamada faturamento:

faturamento = preco × quantidade

Exemplo:

Notebook → 3500 × 2 = 7000

3. Filtro de vendas

Mostre somente as vendas onde:

faturamento > 3000

Depois, mostre somente as colunas:

produto
vendedor
faturamento

4. Filtro por categoria

Mostre todas as vendas das categorias:

"Eletrônicos"
"Headset"? 

⚠️ Aqui quero que você pense: Headset é produto ou categoria?

Use isin() para fazer o filtro.

5. Ordenação

Ordene o DataFrame pelo faturamento, do maior para o menor.

Depois responda:

Qual foi a venda de maior faturamento?

6. Seleção com loc e iloc

Agora pratique os dois:

usando loc, obtenha o produto, vendedor e faturamento da venda de maior faturamento;
usando iloc, obtenha as 3 primeiras linhas e as 3 primeiras colunas.

7. Estatística

Utilize as operações do pandas para descobrir:

faturamento total;
quantidade total de produtos vendidos;
preço médio dos produtos;
maior faturamento de uma venda;
menor faturamento de uma venda.
🧠 Desafio de estágio

O gerente fala:

"Ana parece ser a melhor vendedora. Quero saber quais vendas dela geraram mais de R$ 1.000."
#Faça um filtro que retorne somente vendas da Ana com faturamento superior a R$ 1.000, mostrando:
#produto
#preco
#quantidade
#faturamento

E ordene pelo faturamento decrescente.

🚫 Regra importante

Tente resolver sem pesquisar código na internet.

Você pode consultar a documentação que acabou de estudar — inclusive é exatamente o tipo de comportamento esperado no trabalho.

Eu evitaria, neste exercício, usar groupby, merge, pivot_table etc. O objetivo é testar se você realmente absorveu a parte básica do 10min to pandas, principalmente DataFrame → seleção → filtros → criação de colunas → ordenação → análise.

Nível: 🟢 Estagiário/Júnior iniciante → 🟡 estagiário/júnior intermediário
Tempo esperado: ~40–60 min

Se quiser fazer como uma entrevista técnica, me mande somente seu código quando terminar. Eu corrijo como se fosse seu líder técnico, apontando o que está bom, o que está ruim e como eu esperaria que um estagiário/júnior escrevesse isso em produção.

#Fiz o seguinte prompt: chat, acabei de ler o https://pandas.pydata.org/docs/user_guide/10min.html me passe um exercicio de estagiario/junior em base do conhecimento dessa documentacao

140 linhas de comentário kkkkk, só pra dar um contexto caso algúem leia isso daqui algum dia(duvido mt)
"""

import pandas as pd
import numpy as np

dados = pd.DataFrame (
    {
        'Produto' : ["Notebook", "Mouse", "Teclado", "Monitor",
                    "Notebook", "Mouse", "Headset", "Monitor",
                    "Teclado", "Notebook"],

        'Categoria': ["Eletrônicos", "Acessórios", "Acessórios", "Eletrônicos",
                     "Eletrônicos", "Acessórios", "Acessórios", "Eletrônicos",
                     "Acessórios", "Eletrônicos"],

        'Preco':     [3500, 80, 150, 1200,
                     3500, 80, 300, 1200,
                     150, 3500],

        'Quantidade':[2, 10, 5, 3,
                    1, 20, 4, 2,
                    8, 3],

        'Vendedor': ["Ana", "Carlos", "Ana", "Bruno",
                    "Carlos", "Ana", "Bruno", "Carlos",
                    "Ana", "Bruno"]
    }

)





#inspeção inicial

#print(dados.head())
#print("---")
#print(dados.tail())
#print("---")
#print(dados.columns) #pensei que .columns fosse uma função
#print(dados.dtypes)

#Criação de coluna

dados['faturamento'] = dados['Preco'] * dados['Quantidade']
#print(dados)

#Filtro
#filtro3000 =  dados[dados["faturamento"] > 3000]
#print(filtro3000)

#filtroHeadset = dados[dados["Produto"] == "Headset"]
#print(filtroHeadset)

#Sort = dados.sort_values(by = 'faturamento', ascending= False)
#print(Sort)

#Loc = dados.loc[dados["faturamento"].idxmax(), ['Produto','Vendedor','faturamento']]
#print(Loc)

#iloc = dados.iloc[0:3,0:3]
#print(iloc)



#estatistica

#preço médio dos produtos;
#maior faturamento de uma venda;
#menor faturamento de uma venda.

#faturamentoTotal = dados['faturamento'].sum() 
#quantidadeProdutos = dados['Quantidade'].sum()
#precoMedio = dados['Preco'].mean()
#maiorValor = dados['faturamento'].max()
#menorValor = dados['faturamento'].min()
#print(dados)
#print("Faturamento total: " , faturamentoTotal)
#print("Quantidade vendida:" , quantidadeProdutos)
#print("Preco médio" , precoMedio)
#print("Maior faturamento" , maiorValor)
#print("Menor faturamento" , menorValor)

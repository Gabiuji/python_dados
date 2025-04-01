#Passo 1 - Trazer a base de dados para o Python
import pandas as pd

tabela = pd.read_excel('Vendas.xlsx')

#Passo 2 - Pegar um panorama geral da base de dados
faturamento_total = tabela['Valor Final'].sum()
print(faturamento_total)

#Passo 3 - Começar a análise Top-Down (verificar qual loja vendeu mais)
#faturamento_por_loja
ft_loja = tabela[['ID Loja', 'Valor Final']].groupby("ID Loja").sum() #2 colchetes porque queremos pegar mais de uma coluna. Groupy é para agrupar os dados, e o sum() é para somar os valores
print(ft_loja) #mostra o faturamento por loja

#Passo 4 - verificar o produto que mais vendeu
ft_produto = tabela[['ID Loja','Produto', 'Valor Final']].groupby(['ID Loja', 'Produto']).sum() #2 colchetes porque queremos pegar mais de uma coluna. Groupy é para agrupar os dados, e o sum() é para somar os valores
print(ft_produto) #mostra o faturamento por loja e produto
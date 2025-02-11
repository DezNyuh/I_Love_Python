Produtos = {
'Gasolina Comum':{ 
    'Preço': 6.59,
    'Quantidade em (L)': 14000,
},
'Etanol': {
    'Preço': 4.99,
    'Quantidade em (L)': 27000,
},
'Diesel':{
    'Preço': 6.29,
    'Quantidade em (L)': 11000,
},
'Gasolina Aditivada':{
    'Preço': 6.79,
    'Quantidade em (L)': 9000,
},
}
#Adicionando novo produto no estoque!
Produtos['Gasolina Podium'] = {
    'Preço': 8.19,
    'Quantidade em (L)': 4000,
}
#Pesquisando o produto!
def Pesquisar_Produto(nome_produto, estoque):
    nome_produto = nome_produto.title()
    if nome_produto in estoque:
        print(f'O combustível {nome_produto} está custando: R$ {estoque[nome_produto]["Preço"]}')
        print(f'O estoque do {nome_produto} está em {estoque[nome_produto]["Quantidade em (L)"]}L')
    else:
        print(f'Combustível {nome_produto} não encontrado.')

Pesquisar_Produto('dIeSeL', Produtos)

#Calculando o valor do estoque!
def Valor_Estoque(valor, litros):
    preço = litros[valor]['Preço']
    quantidade = litros[valor]['Quantidade em (L)']
    total = preço * quantidade
    return f'R$ {total:,.2f}'.replace(",","X").replace(".",",").replace("X",".")

total = Valor_Estoque('Diesel', Produtos)
print(f'Valor total do estoque de Diesel: {total}')
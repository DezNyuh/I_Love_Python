# Exemplo de dicionário aninhado
estoque = {
    'produto1': {'nome': 'Notebook', 'preco': 2500.00, 'quantidade': 10},
    'produto2': {'nome': 'Mouse', 'preco': 50.00, 'quantidade': 100},
    'produto3': {'nome': 'Teclado', 'preco': 150.00, 'quantidade': 50}
}

# Acessando valores em dicionários aninhados
print(estoque['produto1']['nome'])  # Saída: Notebook
print(estoque['produto2']['preco'])  # Saída: 50.0
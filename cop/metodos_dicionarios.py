# Exemplo de uso de métodos de dicionários
produto = {'nome': 'Notebook', 'preco': 2500.00, 'quantidade': 10}

print(produto.keys())   # Saída: dict_keys(['nome', 'preco', 'quantidade'])
print(produto.values()) # Saída: dict_values(['Notebook', 2500.0, 10])
print(produto.items())  # Saída: dict_items([('nome', 'Notebook'), ('preco', 2500.0), ('quantidade', 10)])
print(produto.get('preco', 0))  # Saída: 2500.0
print(produto.get('desconto', 0))  # Saída: 0 (pois 'desconto' não existe no dicionário)
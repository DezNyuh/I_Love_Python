import csv
from collections import defaultdict

# 1. Leitura do CSV
vendas = []
with open (r'E:\Biblioteca\VisualCode\GitHub\files\vendas.csv', mode = 'r', newline='', encoding='utf-8') as file:
    leitor = csv.DictReader(file)
    for linha in leitor:
        vendas.append(linha)

# 2. Cálculo do total de vendas
total_vendas = sum(float(venda['Total']) for venda in vendas)
print(f'O total de vendas foi de R$ {total_vendas:.2f}')

# 3. Produto mais vendido
produto = defaultdict(int)
for venda in vendas:
    produto[venda['Produto']] += int(venda['Quantidade'])
produto_mais_vendido = max(produto, key=produto.get)
print(f'O produto mais vendido foi {produto_mais_vendido}')

# 4. Produto menos vendido
produto_menos_vendido = min(produto, key=produto.get)
print(f'O produto menos vendido foi {produto_menos_vendido}')

# 5. Média de vendas por dia
vendas_por_dia = defaultdict(list)
for venda in vendas:
    vendas_por_dia[venda['Data']].append(float(venda['Total']))
media_por_dia = {data: sum(totais) / len(totais) for data, totais in vendas_por_dia.items()}
for data, media in media_por_dia.items():
    print(f'A média de vendas para o dia {data} foi de R$ {media:.2f}')

# 6. Criação de um novo CSV
with open(r'GitHub\files\resumo_de_vendas.csv', mode ='w', newline='', encoding='utf-8') as file:
    campos = ['Data', 'Total de vendas', 'Produto mais vendido',]
    escritor = csv.DictWriter(file, fieldnames=campos)
    escritor.writeheader()
    for data, totais in vendas_por_dia.items():
        total_vendas_dia = sum(totais)
        produtos_dia = [venda['Produto'] for venda in vendas if venda['Data'] == data]
        produto_mais_vendido_dia = max(set(produtos_dia), key=produtos_dia.count)
        escritor.writerow({
            'Data': data,
            'Total de vendas': total_vendas_dia,
            'Produto mais vendido': produto_mais_vendido_dia
        })

print('Resumo de vendas criado com sucesso!')

# O que esses códigos fazem?
# DictReader: Lê um arquivo CSV e cria um dicionário para cada linha, onde as chaves são os cabeçalhos e os valores são os dados.
# defaultdict: Cria um dicionário que aceita valores padrão para chaves que não existem.
# writerow: Escreve uma linha no arquivo CSV.
# writeheader: Escreve o cabeçalho no arquivo CSV.
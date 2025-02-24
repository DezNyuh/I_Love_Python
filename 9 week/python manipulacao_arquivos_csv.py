import csv
import os

# Dados para escrever no arquivo CSV
dados = [
    ['Nome', 'Idade', 'Cidade'],
    ['Alice', '30', 'São Paulo'],
    ['Bob', '25', 'Rio de Janeiro'],
    ['Charlie', '35', 'Belo Horizonte']
]

# Caminho onde o arquivo CSV será criado inicialmente
caminho_arquivo = 'dados.csv'

# Criar e escrever no arquivo CSV
with open(caminho_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
    escritor_csv = csv.writer(arquivo)
    escritor_csv.writerows(dados)

print(f"Arquivo CSV criado: {caminho_arquivo}")

# Caminho da pasta de destino
pasta_destino = os.path.join('files')

# Verificar se a pasta de destino existe, se não, criar a pasta
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

# Caminho completo do arquivo de destino
caminho_destino = os.path.join(pasta_destino, caminho_arquivo)

# Mover o arquivo para a pasta de destino
os.replace(caminho_arquivo, caminho_destino)

print(f"Arquivo movido para: {caminho_destino}")
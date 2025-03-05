matriz = [[1,2,3], [4,5,6], [7,8,9]]
matriz[0][0] = 10 # Modifica a linha 0 e a coluna 0

for linha in matriz:
    print(linha)

valor_total = 0 # Número inicial

for linha in matriz: # Pecorre em cada linha
    for elemento in linha: #Percorre cada número da linha
        valor_total += elemento #Soma os valores
    
print(valor_total)
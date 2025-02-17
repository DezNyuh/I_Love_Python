five = [0, 1, 6, 3, 4]
five.append(5) #Adicionar no final da lista
five.remove(0) #Remove o primeiro número
five.reverse() #Inverter a ordem
five.sort() #Organiza na ordem crescente

lista = [] #Cria uma lista vazia
for ten in range(11): #Contar de 0 a 10
    lista.append(ten) #Lista vazia + Guardar o valor em lista

pares = [] #Cria uma lista vazia
for p in range(50): #Conta de 0 a 50
    if p % 2 == 0: #Se a sobra de p for igual a 0
        pares.append(p) #Guarda o valor em pares

greater = []
for g in range(25):
    if g > 5: #Se g for maior que 5
        greater.append(g)

print(greater)
print(pares)
print(lista)
print(five)
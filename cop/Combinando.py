# Criando uma lista, uma tupla e um conjunto com os mesmos elementos
lista = [1, 2, 3, 4, 5, 5]
tupla = (1, 2, 3, 4, 5, 5)
conjunto = {1, 2, 3, 4, 5, 5} #A segunda repetição de 5 é ignorada
conjunto2 = {3, 1, 4, 2}


# Convertendo a lista em tupla e conjunto
tupla_de_lista = tuple(lista)
conjunto_de_lista = set(lista) #Número 5 repetido, some

# Convertendo a tupla em lista e conjunto
lista_de_tupla = list(tupla)
conjunto_de_tupla = set(tupla) #Número 5 repetido, some

# Convertendo o conjunto em lista e tupla
lista_de_conjunto = list(conjunto) 
tupla_de_conjunto = tuple(conjunto)
lista_de_conjunto2 = list(conjunto2)
tupla_de_conjunto2 = tuple(conjunto2)

# Exibindo os resultados
print("Lista original:", lista)
print("Tupla original:", tupla)
print("Conjunto original:", conjunto)
print("Lista convertida para tupla:", tupla_de_lista)
print("Lista convertida para conjunto:", conjunto_de_lista)
print("Tupla convertida para lista:", lista_de_tupla)
print("Tupla convertida para conjunto:", conjunto_de_tupla)
print("Conjunto convertido para lista:", lista_de_conjunto)
print("Conjunto convertido para tupla:", tupla_de_conjunto)
print('Conjunto2 convertido para lista:', lista_de_conjunto2)
print('Conjunto2 convertido para tupla:', tupla_de_conjunto2)
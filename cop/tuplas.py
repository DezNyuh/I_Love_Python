#Criação e Acesso de Tuplas
pessoa = (('Rafa', 25, 'Recife'), ('João', 32, 'Jaboatão'), ('Felipe', 18, 'Abreu e Lima'))

print(pessoa[0])  # Acessa a primeira tupla
print(pessoa[1][2])  # Acessa o terceiro valor da segunda tupla
print(pessoa[2][1])  # Acessa o segundo valor da terceira tupla

# Tentando modificar um elemento de uma tupla (causará erro)
# pessoa[1][0] = 'Raquel'  # Erro: Tupla não pode ser modificada

print(pessoa[1])


#Desempacotando tuplas

coordenadas = ((15, 33, 45), (22, 82, 33), (92, 85, 215))

# Desempacotando a tupla de coordenadas em três variáveis
x = (coordenadas[0][0], coordenadas[1][0], coordenadas[2][0])
y = (coordenadas[0][1], coordenadas[1][1], coordenadas[2][1])
z = (coordenadas[0][2], coordenadas[1][2], coordenadas[2][2])

print(sum(x))
print(sum(y))
print(sum(z))

print(sum(x) + sum(y) + sum(z))


#Dicionário com tuplas como chaves

coordenada = {(10, 20): 'Mesa', (15, 30): 'Geladeira', (20, 40): 'Pia'}

# Modificando o valor associado à chave (10, 20)
coordenada[(10, 20)] = 'Cadeira'

print(coordenada)



#Comparação de tuplas
a = (10, 15, 20)
b = (3, 6, 9)
c = (20, 40, 60)

# Comparando as tuplas
if a > b:
    print('a é maior que b')
else: 
    print('a não é maior que b')

if c == b:
    print('c é igual a b')
else: 
    print('c é diferente de b')

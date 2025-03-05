#Criando e manipulando conjuntos
conjunto = {1,2,3,4,5}

conjunto.add(6) #Adiciona o 6
conjunto.remove(3) #Remove o 3

if 3 not in conjunto: #Verifica se o 3 não está no conjunto
    print('O 3 foi removido')
else:
    print('3 ainda está no conjunto.')

print(conjunto)

#Operações com conjuntos

valor1 = {10, 20, 30, 40}
valor2 = {15, 20, 35, 45}

# União de dois conjuntos (elementos presentes em qualquer um dos conjuntos)
união = valor1 | valor2  # Alternativamente, você pode usar valor1.union(valor2)
# Interseção de dois conjuntos (elementos presentes em ambos os conjuntos)
interseção = valor1 & valor2  # Alternativamente, valor1.intersection(valor2)
# Diferença entre os conjuntos (elementos que estão em valor1 mas não em valor2)
diferença = valor1 - valor2  # Alternativamente, valor1.difference(valor2)

print("União:", união)
print("Interseção:", interseção)
print("Diferença:", diferença)

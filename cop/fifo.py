# Implementação de uma fila usando listas
from collections import deque

fila = deque()

# Adicionando elementos à fila
fila.append(1)
fila.append(2)
fila.append(3)

print(fila)  # Saída: deque([1, 2, 3])

# Removendo elementos da fila
print(fila.popleft())  # Saída: 1
print(fila.popleft())  # Saída: 2
print(fila)  # Saída: deque([3])
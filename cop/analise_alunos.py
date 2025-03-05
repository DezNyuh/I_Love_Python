# Lista de tuplas com nomes e notas dos alunos
alunos_notas = [
    ("Alice", 85),
    ("Bob", 90),
    ("Carla", 78),
    ("David", 92),
    ("Alice", 85),  # Duplicado
    ("Eva", 88),
    ("Bob", 90),    # Duplicado
]

# Encontrar alunos únicos usando conjuntos
alunos_unicos = set(aluno[0] for aluno in alunos_notas)
print("Alunos únicos:", alunos_unicos)

# Calcular a média das notas usando listas
notas = [aluno[1] for aluno in alunos_notas]
media = sum(notas) / len(notas)
print(f"Média das notas: {media:.1f}")
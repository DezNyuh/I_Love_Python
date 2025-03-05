# Conjunto de palavras secretas
palavras_secretas = {"python", "programacao", "desafio", "algoritmo", "openai"}

# Lista para armazenar as tentativas do jogador
tentativas = []

print("Bem-vindo ao Jogo de Adivinhação!")
print("Tente adivinhar uma das palavras secretas.")

while True:
    # Solicita uma tentativa ao jogador
    tentativa = input("\nDigite sua tentativa: ").strip().lower()

    # Adiciona a tentativa à lista de tentativas
    tentativas.append(tentativa)

    # Verifica se a tentativa está no conjunto de palavras secretas
    if tentativa in palavras_secretas:
        print(f"Parabéns! Você acertou a palavra secreta: '{tentativa}'.")
        break
    else:
        print("Tentativa incorreta. Tente novamente!")

# Exibe todas as tentativas do jogador
print("\nTentativas realizadas:")
for idx, tentativa in enumerate(tentativas, 1):
    print(f"Tentativa {idx}: {tentativa}")
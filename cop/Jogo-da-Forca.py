import random
from unidecode import unidecode

estado_aleatorio = ("ACRE", "ALAGOAS", "AMAPÁ", "AMAZONAS", "BAHIA", "CEARÁ", "DISTRITO FEDERAL", "ESPÍRITO SANTO", "GOIÁS", "MARANHÃO", "MATO GROSSO", "MATO GROSSO DO SUL", "MINAS GERAIS", "PARÁ", "PARAÍBA", "PARANÁ", "PERNAMBUCO", "PIAUÍ", "RIO DE JANEIRO", "RIO GRANDE DO NORTE", "RIO GRANDE DO SUL", "RONDÔNIA", "RORAIMA", "SANTA CATARINA", "SÃO PAULO", "SERGIPE", "TOCANTINS")

while True:
    estado_escolhido = random.choice(estado_aleatorio).upper()
    noacentos = unidecode(estado_escolhido)
    chute = []
    chances = 7
    ganhou = False

    while True:
        for letra in estado_escolhido:
            if unidecode(letra) in chute:
                print(letra, end=" ")
            else:
                print("_", end=" ")
        print("")

        if all(letra in chute or unidecode(letra) in chute for letra in estado_escolhido if letra.isalpha()):
            ganhou = True
            break
        
        tentativa = input('Escolha uma letra para adivinhar: ').upper() 
        tentativa_normalizada = unidecode(tentativa)

        if tentativa_normalizada in chute:
            print("Você já tentou essa letra!")
            continue

        chute.append(tentativa_normalizada)
        if tentativa_normalizada not in noacentos:
            chances -= 1
            print(f"Errado você têm {chances} restantes!")

        if chances == 0:
            break

    if ganhou:
        print(f"Parabéns! Você acertou a palavra era: {estado_escolhido}")
    else:
        print(f"Você perdeu. A palavra era: {estado_escolhido}")

    continuar = input("Deseja jogar novamente? (S/N): ").upper()
    if continuar != "S":
        print("Encerrando o jogo. Obrigado por jogar!")
        break
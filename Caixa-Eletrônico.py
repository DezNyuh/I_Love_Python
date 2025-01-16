print("\n=== Bem-vindo(a) ao Caixa Eletrônico ===")

LIMITE_MAXIMO = 10000 

while True:
    try:
        valor = int(input("Digite o valor que deseja sacar (em reais): "))
        if valor <= 0:
            print("Por favor, insira um valor maior que zero.") 
        elif valor < 10:
            print("O valor mínimo para saque é R$10. Por favor, insira um valor maior.")
        elif valor > LIMITE_MAXIMO:
            print(f"O valor máximo permitido é R${LIMITE_MAXIMO}.")
        else:
            break
    except ValueError:
        print("Entrada inválida! Insira um número inteiro.")

if valor % 10 != 0:
    print(f"O valor {valor} não é múltiplo de 10. Ele será ajustado para {valor // 10 * 10}.")
    valor = valor // 10 * 10

cedulas = [200, 100, 50, 20, 10]
resultado = {}

for cedula in cedulas:
    qtd_cedulas = valor // cedula
    if qtd_cedulas > 0:
        resultado[cedula] = qtd_cedulas
        valor -= qtd_cedulas * cedula

print("Você receberá:")
for cedula, qtd in resultado.items():
    print(f"{qtd} cédula(s) de R${cedula}")

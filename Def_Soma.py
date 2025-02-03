def asoma(n1,n2,n3): 
    return n1 + n2 + n3


while True:
    try:
        numero1 = int(input('Escolha um número: '))
        numero2 = int(input('Escolha um número: '))
        numero3 = int(input('Escolha um número: '))
        break 
    except ValueError:
        print('!! DIGITE UMA ENTRADA VÁLIDA !!')

total = asoma(numero1, numero2, numero3)
print(total)
def media(a,b,c):
    return (a + b + c) / 3

while True:
    try:
        numero1 = int(input('Escolha um número: '))
        numero2 = int(input('Escolha um número: '))
        numero3 = int(input('Escolha um número: '))
        break
    except ValueError:
        print("!!!  DIGITE UMA ENTRAVA VÁLIDA    !!!")

mediareal = media(numero1, numero2, numero3)
print(mediareal)
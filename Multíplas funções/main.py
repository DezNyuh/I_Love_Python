from matematica import asoma, somatudo, media
from strings import saudacao

print('A soma de todos os numerais é:', somatudo(2, 45, 89, 47, 25, 36))
print('A soma entre os 3 numerais é:', asoma(2, 5, 8))
print('A média entre esses números é:', media(10, 25, 89))

seu_nome = input('Digite o seu nome: ')
if not seu_nome:
    seu_nome = None

while True:
    try:
        sua_idade = int(input('Qual a sua idade? '))
        break
    except ValueError:
        print("!! INSIRA UMA ENTRADA VÁLIDA !!")

if seu_nome is None:
    print(saudacao(sua_idade))
else:
    print(saudacao(sua_idade, seu_nome))
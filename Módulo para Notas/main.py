from calculo import notas

print('Olá!')

aluno = input('Qual é o seu nome?')
print(f'Seja bem-vindo(a) {aluno}!')

notatotal = sum(notas())
nota = (notatotal / 4)

if nota > 7:
    print('Você foi aprovado!')
else:
    print('Você foi reprovado!')

print(f'A sua média foi {nota}')
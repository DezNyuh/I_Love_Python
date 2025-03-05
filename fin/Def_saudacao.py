def saudacao(idade, nome='Visitante'):
    return f'Olá, {nome}! Você têm {idade} anos!'

seu_nome = input('Qual seu nome? ')
if not seu_nome:
    seu_nome = None

sua_idade = int(input('Qual sua idade? '))

if seu_nome is None:
    mensagem = saudacao(sua_idade)
else:
    mensagem = saudacao(sua_idade, seu_nome)

print(mensagem)

def saudacao(nome, idade):
    return f'Olá, {nome}! Você têm {idade} anos!'

seu_nome = input('Qual seu nome? ')
sua_idade = int(input('Qual sua idade? '))
mensagem = saudacao(seu_nome, sua_idade)
print(mensagem)

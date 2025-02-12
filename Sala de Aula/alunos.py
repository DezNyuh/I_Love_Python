#Pesquisa o nome do aluno.
def pesquisar_aluno(nome, aluno):
    if nome in aluno:
        print(f'Nome: {nome}!')
        print(f'Nota: {aluno[nome] ["Nota"]}')
        print(f'Status: {aluno[nome] ["Status"]}')
    else:
        print(f'O aluno {nome} não foi encontrado.')

#Adicionar um novo aluno no dicionário
def adicionar_aluno(alunos):

    #Coletar o nome do aluno
    nome = input('Digite o nome do aluno: ').title()

    #Coletar a nota do aluno
    try:
        nota = float(input('Digite a nota do aluno (0 a 10):  '))
        if 0 <= nota <= 10:

        #Determinar o status
            status = 'Aprovado' if nota >= 6 else 'Reprovado'

        #Adicionar o aluno ao dicionário
            alunos[nome] = {'Nota': nota, 'Status': status}
            print(f'Aluno {nome} adicionado com sucesso!')
        else:
            print('Nota inválida! A nota deve estar entre 0 e 10')
    except ValueError:
        print('Erro: A nota deve ser um número válido')

def todos_alunos(lista):
    if not lista:
        print('Nenhum aluno cadastrado')
        return
    
    print('Lista de alunos: ')
    for nome, info in lista.items():
        print(f'\n Nome: {nome}')
        for chave, valor in info.items():
            print(f'{chave}: {valor}')

def atualizar_dados(nome_aluno, chave, novo_valor):
    if nome_aluno in Sala1:
        if chave in Sala1[nome_aluno]:
            Sala1[nome_aluno][chave] = novo_valor
            print(f'{chave} de {nome_aluno} foi atualizada para {novo_valor}')
        else:
            print(f'Erro! A chave "{chave}" não existe para {nome_aluno}')
    else:
        print(f'Erro! O Aluno "{nome_aluno}" não foi encontrado!')
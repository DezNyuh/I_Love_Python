from dados import Sala1

#Pesquisar aluno
def pesquisar_aluno():
    nome = input('Digite o nome do aluno: ').title()
    if nome in Sala1:
        print(f'Estudante {nome} teve a nota de {Sala1[nome]['Nota']} e foi {Sala1[nome]['Status']}!')
    else:
        print(f'Erro: Estudante {nome} não encontrado!')

#Adicionar um novo aluno no dicionário
def adicionar_aluno():

    #Coletar o nome do aluno
    nome = input('Digite o nome do aluno: ').title()

    #Coletar a nota do aluno
    try:
        nota = float(input('Digite a nota do aluno (0 a 10):  '))
        if 0 <= nota <= 10:

        #Determinar o status
            status = 'Aprovado' if nota >= 6 else 'Reprovado'

        #Adicionar o aluno ao dicionário
            Sala1[nome] = {'Nota': nota, 'Status': status}
            print(f'Aluno {nome} adicionado com sucesso!')
            #Atualiza a Lista
            print('\nAlunos atualizados:')
            for nome, dados in Sala1.items():
                print(f'{nome} - Nota: {dados['Nota']} - Status: {dados['Status']}!')
        else:
            print('Erro: Nota inválida! A nota deve estar entre 0 e 10')
    except ValueError:
        print('Erro: A nota deve ser um número válido')
        
#Lista de todos os alunos
def todos_alunos():
    for nome, info in Sala1.items():
        print(f'Nome: {nome} - Nota: {info['Nota']} - Status: {info['Status']}')

#Atualizar dados
def atualizar_dados():
    nome = input('Digite o nome do aluno: ').title()
    if nome in Sala1:
        try:
            nova_nota = float(input('Digite a nova nota do aluno: '))
            if 0 <= nova_nota <= 10:
                Sala1[nome]['Nota'] = nova_nota
                Sala1[nome]['Status'] = 'Aprovado' if nova_nota >= 6 else 'Reprovado'
                print(f'Nota de {nome} atualizada com sucesso!')
            else:
                print('Erro: Nota inválida! A nota deve ser entre 0 e 10!')
        except ValueError:
            print('Erro: Entrada inválida!')
    else:
        print(f'Erro: Aluno {nome} não encontrado!')

#Remover aluno
def remover_aluno():
    nome = input('Digite o nome do aluno a ser removido: ').title()
    if nome in Sala1:
        del Sala1[nome]
        print(f'Aluno {nome} removido com sucesso!')
    else:
        print(f'Erro: Aluno {nome} não encontrado!')

#Calcular média
def calcular_media():
    if not Sala1:
        print('Nenhum aluno encontrado')

    total_notas = sum(info['Nota'] for info in Sala1.values()) 
    media = total_notas / len(Sala1)
    print(f'A média da sala é {media:.2f}')

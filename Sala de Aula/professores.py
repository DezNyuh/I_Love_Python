from dados import professoress1

def adicionar_professor():
    nome = input('Digite o nome do professor: ').title()
    disciplina = input('Digite a disciplina: ').title()
    turma = input('Digite a turma do professor: ')

    professoress1[nome] = {'Disciplina': disciplina,'Turma': turma}
    print(f'Professor {nome} adicionado com sucesso!')

def pesquisar_professor():
    nome = input('Digite o nome do professor:').title()
    if nome in professoress1:
        print(f'Nome: {nome} - Disciplina: {professoress1[nome]["Disciplina"]} - Turma: {professoress1[nome]["Turma"]} ')
    else:
        print('Professor não encontrado')

def remover_professor():
    nome = input('Digite o nome do professor: ').title()
    if nome in professoress1:
        del professoress1[nome]
        print(f'Professor {nome} removido com sucesso!')
    else:
        print('Erro: Professor não encontrado!')

def todos_professores():
    for nome, info in professoress1.items():
        print(f'Professor {nome} - Disciplina: {info["Disciplina"]} - Turma: {info['Turma']}')


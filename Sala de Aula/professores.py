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

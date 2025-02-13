from alunos import pesquisar_aluno, adicionar_aluno, todos_alunos, atualizar_dados
def menu():
    print('\n --- MENU --- ')
    print('1. Pesquisar um aluno')
    print('2. Adicionar um aluno')
    print('3. Lista de alunos')
    print('4. Atualizar nota de um aluno')
    return input('Escolha uma opção:')

while True:
    opcao = menu()

    if opcao == '1':
        pesquisar_aluno()
    elif opcao == '2':
        adicionar_aluno()
    elif opcao =='3':
        todos_alunos()
    elif opcao =='4':
        atualizar_dados()
        break


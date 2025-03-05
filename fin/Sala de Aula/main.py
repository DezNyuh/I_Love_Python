from alunos import pesquisar_aluno, adicionar_aluno, todos_alunos, atualizar_dados, remover_aluno, calcular_media
from professores import pesquisar_professor, adicionar_professor, remover_professor, todos_professores
def menu():
    print('\n --- MENU --- ')
    print('1. Pesquisar um aluno')
    print('2. Adicionar um aluno')
    print('3. Lista de alunos')
    print('4. Atualizar nota de um aluno')
    print('5. Remover um aluno')
    print('6. Média da sala')
    print('7. Pesquisar professor')
    print('8. Adicionar professor')
    print('9. Remover professor')
    print('10. Lista de professores')
    print('11. Sair.')
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
    elif opcao =='5':
        remover_aluno()
    elif opcao=='6':
        calcular_media()
    elif opcao=='7':
        pesquisar_professor()
    elif opcao=='8':
        adicionar_professor()
    elif opcao=='9':
        remover_professor()
    elif opcao=='10':
        todos_professores()
    elif opcao =='11':
        print('Saindo...')
        break
    else:
        print('Erro: Opção inválida.')


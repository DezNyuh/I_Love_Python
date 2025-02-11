Sala1 = {
    'Miguel Souza': {
'Nota': 6.5,
'Status': 'Reprovado'
    },
    'Rafaela Silva': {
'Nota' : 8.5,
'Status' : 'Aprovado'
    },

    'Thayná Maria': {
'Nota' : 9.0,
'Status' : 'Aprovado'
    }
}

def pesquisar_aluno(nome, aluno):
    if nome in aluno:
        print(f'Nome: {nome}!')
        print(f'Nota: {aluno[nome] ["Nota"]}')
        print(f'Status: {aluno[nome] ["Status"]}')
    else:
        print(f'O aluno {nome} não foi encontrado.')

pesquisar_aluno('Rafaela Silva', Sala1)
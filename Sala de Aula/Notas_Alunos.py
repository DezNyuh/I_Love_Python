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

todos_alunos(Sala1)


atualizar_dados('Rafaela Silva', 'Nota', 10)

print('\nAlunos atualizados:')
for nome, info in Sala1.items():
    print(f"{nome}, {info}")
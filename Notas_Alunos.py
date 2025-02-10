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

#Verificar o aluno aprovado
for nome, info in Sala1.items():
    if info['Status'] == 'Aprovado':
        print(f'O aluno {nome} foi {info['Status']}')

#Verificar o aluno reprovado
for nome, info in Sala1.items():
    if info['Status'] == 'Reprovado':
        print(f'O aluno {nome} foi {info['Status']}')
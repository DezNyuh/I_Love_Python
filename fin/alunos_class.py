alunos = []

class Aluno:
    def __init__ (self, aluno, nota, status):
        self.aluno = aluno
        self.nota = nota
        self.status = status

    def cadastro_aluno (self):
        nome = input('Digite o seu nome: ')

        try:
            nota = int(input('Digite sua nota: '))
            if 0 <= nota <= 10:
                status = 'Aprovado' if nota >= 6 else 'Reprovado'
                print(f'{nome}, você foi {status}.')
            else:
                print('Erro: Nota Inválida, a nota deve estar entre 0 e 10.')
        except ValueError:
            print('Erro: Entrada Inválida.')

cadastar_aluno = Aluno('aluno', 'nota', 'status')
cadastar_aluno.cadastro_aluno()

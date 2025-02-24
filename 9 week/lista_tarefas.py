import os

class Tarefa:
    def __init__(self, arquivo):
        self.pasta_destino = os.path.join('files')
        if not os.path.exists(self.pasta_destino):
            os.makedirs(self.pasta_destino)
        self.arquivo = os.path.join(self.pasta_destino, arquivo)


    def adicionar_tarefa(self, tarefa, data):
         # Abrir o arquivo com 'a' faz com que o conteúdo seja adicionado no final do arquivo, se não existir o arquivo ele será criado.
        with open(self.arquivo, 'a') as file:
            file.write(f'Tarefa: {tarefa}, Data: {data} \n')
        print(f'Tarefa: {tarefa} adicionada!')

    def visualizar_tarefas(self, ):
        try:
            with open(self.arquivo, 'r') as file:
                tarefas = file.readlines()
                if tarefas:
                    print('Lista de Tarefas:')
                    for linha in tarefas:
                        print(linha.strip())
                else:
                    print('Nenhuma tarefa encontrada!')
        except FileExistsError:
            print('Arquivo não encontrado. Crie uma tarefa primeiro.')

afazer = Tarefa('Tarefas.txt')
afazer.adicionar_tarefa('Ser Expert na programação', '24-02-2025')
afazer.adicionar_tarefa('Escutar música', '24-02-2025')
afazer.visualizar_tarefas()

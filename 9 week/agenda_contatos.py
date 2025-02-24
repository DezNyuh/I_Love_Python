import os 

class Agenda:
    def __init__(self, arquivo):
        #Definir pasta destino
        self.pasta_destino = os.path.join('files')

        #Verificar se a pasta de destino existe, se não, criar a pasta
        if not os.path.exists(self.pasta_destino):
            os.makedirs(self.pasta_destino)

            #Caminho completo do arquivo de destino
        self.arquivo = os.path.join(self.pasta_destino, arquivo)
    
    def adicionar_contato(self, nome, telefone):
        """Adiciona um contato ao arquivo."""
        with open(self.arquivo, 'a') as file:
            file.write(f'{nome},{telefone}\n')
        print(f'Contato {nome} adicionado!')
    
    def listar_contatos(self, ):
        """Lê e exibe os contatos armazenados."""
        try:
            with open(self.arquivo, 'r') as file:
                contatos = file.readlines()
                if contatos:
                    print('Agenda de Contatos:')
                    for linha in contatos:
                        nome, telefone = linha.strip().split(',')
                        print(f'Nome: {nome}, Telefone: {telefone}')
                else:
                    print('A agenda está vazia.')
        except FileNotFoundError:
            print('Nenhum contato salvo ainda.')

# Exemplo de uso
agenda = Agenda('agenda.txt')
agenda.adicionar_contato('Alice', '9999-8888')
agenda.adicionar_contato('Bob', '8888-7777')
agenda.listar_contatos()
agenda.adicionar_contato('Rafael', '7777-5855')
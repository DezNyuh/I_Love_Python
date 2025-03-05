class FilaAtendimento:
    def __init__(self):
        self.fila = []
    
    def entrar_na_fila(self, cliente):
        """Adiciona um cliente ao final da fila."""
        self.fila.append(cliente)
        print(f'{cliente} entrou na fila.')
    
    def atender_cliente(self):
        """Remove e retorna o primeiro cliente da fila."""
        if self.fila:
            cliente_atendido = self.fila.pop(0) #Cliente atendido removendo o primeiro a entrar na fila
            print(f'Atendendo {cliente_atendido}.')
            return cliente_atendido
        else:
            print('A fila está vazia.')
            return None
    
    def mostrar_fila(self):
        """Exibe a fila atual."""
        print(f'Fila atual: {self.fila}')

# Exemplo de uso:
fila = FilaAtendimento()
fila.entrar_na_fila("Alice")
fila.entrar_na_fila("Bob")
fila.entrar_na_fila("Carol")
fila.mostrar_fila()
fila.atender_cliente()
fila.mostrar_fila()

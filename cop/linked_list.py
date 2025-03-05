# Implementação de uma lista ligada simples
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaLigada:
    def __init__(self):
        self.cabeca = None

    def adicionar(self, valor):
        novo_no = No(valor)
        if self.cabeca is None:
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no

    def exibir(self):
        atual = self.cabeca
        while atual:
            print(atual.valor, end=" -> ")
            atual = atual.proximo
        print("None")

# Exemplo de uso
lista = ListaLigada()
lista.adicionar(1)
lista.adicionar(2)
lista.adicionar(3)
lista.exibir()  # Saída: 1 -> 2 -> 3 -> None
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo da instância
        self.idade = idade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

# Criando um objeto (instância da classe)
pessoa1 = Pessoa("João", 30)

# Acessando atributos
print(pessoa1.nome)  # Saída: João
print(pessoa1.idade)  # Saída: 30

# Chamando um método
print(pessoa1.apresentar())  # Saída: Olá, meu nome é João e tenho 30 anos.

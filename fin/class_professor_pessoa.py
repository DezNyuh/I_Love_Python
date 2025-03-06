class Pessoa:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def falar (self):
        print(f'{self.nome} está falando.')

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        # Chama o construtor da classe pai (Pessoa)
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def ensinar(self):
        print(f"{self.nome} está ensinando {self.disciplina}.")

# Cria uma instância de Pessoa
Pessoa1 = Pessoa('João', 30)
Pessoa1.falar()

# Cria uma instância de Professor usando os atributos de Pessoa1
Professor1 = Professor(Pessoa1.nome, Pessoa1.idade, 'Redação')
Professor1.ensinar()

# Como Professor herda de Pessoa, ele também pode usar o método falar
Professor1.falar()

Professor2 = Professor('Maria', 40, 'Matemática')
Professor2.falar()
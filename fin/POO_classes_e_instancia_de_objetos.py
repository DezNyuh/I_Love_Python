from datetime import datetime

class Carro:
    def __init__(self, marca, modelo, ano,):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.idade = self.calcular_idade()

    def exibir_informações(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Idade: {self.idade}")

    def calcular_idade(self):
        ano_atual = datetime.now().year
        return ano_atual - self.ano 

carro1 = Carro("Chevrolet"  , "Onix" , 2019)
carro2 = Carro("Volkswagen" , "Gol"  , 2015)

carro1.exibir_informações()
carro2.exibir_informações()
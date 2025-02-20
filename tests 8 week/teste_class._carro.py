class Carro:
    def __init__(self, marca, modelo, ano, quilometragem):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = quilometragem

    def apresentar(self):
        return f'Marca: {self.marca} - Modelo: {self.modelo} - Ano: {self.ano} - Km: {self.quilometragem}'

carro1 = Carro('Fiat', 'Pulse', 2024, 1000)

print(carro1.apresentar())
class ContaBancaria:
    def __init__(self,titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def informar_saldo(self):
        return f''

saldo = 0

def depositar():
    deposito = int(input('Qual valor você quer depositar? '))
    saldo += deposito

def sacar():
    saque = int(input('Qual valor a ser sacado? '))
    ,  
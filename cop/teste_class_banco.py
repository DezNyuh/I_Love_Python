# Dicionário para armazenar os titulares e seus saldos
titulares = {'Rafael': {'Saldo': 150}, 'Ana': {'Saldo': 200}}

# Função para depositar dinheiro
def depositar(titular):
    if titular in titulares:
        deposito = int(input('Qual valor você quer depositar? '))
        titulares[titular]['Saldo'] += deposito
        print(f'Depósito realizado! Novo saldo: {titulares[titular]["Saldo"]}')
    else:
        print('Titular não encontrado!')

# Função para sacar dinheiro
def sacar(titular):
    if titular in titulares:
        saldo = titulares[titular]['Saldo']
        valor_saque = int(input(f'Quanto deseja sacar? Seu saldo é: {saldo} '))
        if valor_saque > saldo:
            print('Valor insuficiente!')
        else:
            titulares[titular]['Saldo'] -= valor_saque
            print(f'Valor sacado! Novo saldo: {titulares[titular]["Saldo"]}')
    else:
        print('Titular não encontrado!')

# Classe ContaBancaria
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def informar_saldo(self):
        return f'Saldo atual: {self.saldo}'

# Exemplo de uso
# Adicionando um novo titular ao dicionário
titulares['Carlos'] = {'Saldo': 300}

# Realizando operações
depositar('Rafael')  # Depositar dinheiro para Rafael
sacar('Ana')  # Sacar dinheiro de Ana

# Criando uma instância da classe ContaBancaria
conta_carlos = ContaBancaria('Carlos', titulares['Carlos']['Saldo'])
print(conta_carlos.informar_saldo())  # Informar saldo de Carlos
fila = ['Bob', 'Alice', 'Ana', 'Raquel', 'Vitória']

def adicionar_cliente():
    ultimo = input('Qual seu nome? ').strip().title()
    if ultimo not in fila:
        fila.append(ultimo)
        print(f'{ultimo} adicionado à fila.')
    else:
        print('Esse cliente já está na fila.')
        
fila = []

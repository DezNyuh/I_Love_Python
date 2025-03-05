def prova(x):
    return float(input(f'Qual foi sua nota na {x} prova? '))

def notas():
    lista_notas = []
    for fase_prova in ['primeira', 'segunda', 'terceira', 'quarta']:
        lista_notas.append(prova(fase_prova))
    return lista_notas
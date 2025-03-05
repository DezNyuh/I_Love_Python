contatos = [('Alice','55515165'),('Rafael','65565151'),('Bianca','86488485')]
nome_unico = set(nome for nome, telefone in contatos)

def addc():
    nome = input('nome').strip().title()
    telefone = input('numero').strip()
    if nome in nome_unico:
        print('existe')
    else:
        contatos.append(nome, telefone)
        nome_unico.add(nome)
        print(f'{nome} adicionado')

def bsc():
    nome = input('nome').strip().title()
    for contato in contatos:
        if contato[0] == nome:
            print(f'{contato[0]} e {contato[1]}')
            return
    print('não existe')

bsc()
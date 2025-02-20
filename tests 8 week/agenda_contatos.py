# Lista de tuplas para armazenar contatos (nome, telefone)
contatos = [("Alice", "1234-5678"), ("Bob", "8765-4321"), ("Carla", "5555-5555")]

# Conjunto para armazenar nomes únicos e evitar duplicatas
nomes_unicos = set(nome for nome, telefone in contatos)

def adicionar_contato():
    """Adiciona um novo contato à lista de contatos."""
    nome = input("Digite o nome do contato: ").strip().title()
    telefone = input("Digite o telefone do contato: ").strip()

    if nome in nomes_unicos:
        print("Erro: Este contato já existe na agenda.")
    else:
        contatos.append((nome, telefone))
        nomes_unicos.add(nome)
        print(f"Contato '{nome}' adicionado com sucesso!")

def buscar_contato():
    """Busca um contato pelo nome."""
    nome = input("Digite o nome do contato para buscar: ").strip().title()

    for contato in contatos:
        if contato[0] == nome:
            print(f"Contato encontrado: {contato[0]} - {contato[1]}")
            return
    print("Contato não encontrado.")

def remover_contato():
    """Remove um contato pelo nome."""
    nome = input("Digite o nome do contato para remover: ").strip().title()

    for i, contato in enumerate(contatos):
        if contato[0] == nome:
            contatos.pop(i)
            nomes_unicos.remove(nome)
            print(f"Contato '{nome}' removido com sucesso!")
            return
    print("Contato não encontrado.")

def listar_contatos():
    """Lista todos os contatos da agenda."""
    if not contatos:
        print("A agenda de contatos está vazia.")
    else:
        print("\nLista de contatos:")
        for idx, (nome, telefone) in enumerate(contatos, 1):
            print(f"{idx}. {nome} - {telefone}")

def menu():
    """Exibe o menu de opções."""
    print("\n--- Agenda de Contatos ---")
    print("1. Adicionar contato")
    print("2. Buscar contato")
    print("3. Remover contato")
    print("4. Listar contatos")
    print("5. Sair")

# Loop principal do programa
while True:
    menu()
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        adicionar_contato()
    elif opcao == "2":
        buscar_contato()
    elif opcao == "3":
        remover_contato()
    elif opcao == "4":
        listar_contatos()
    elif opcao == "5":
        print("Saindo da agenda de contatos. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
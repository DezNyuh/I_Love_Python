import json

# Função para salvar os contatos em um arquivo JSON
def salvar_contatos(contatos, arquivo):
    with open(arquivo, 'w') as f:
        json.dump(contatos, f, indent=4) # o parâmetro dump é responsável por escrever o conteúdo no arquivo.
        #já o indent=4 é responsável por formatar o arquivo JSON com 4 espaços de indentação.

# Função para carregar os contatos de um arquivo JSON
def carregar_contatos(arquivo):
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Função para adicionar um novo contato
def adicionar_contato(contatos):
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }
    
    contatos.append(contato)
    print("Contato adicionado com sucesso!")

# Função para listar todos os contatos
def listar_contatos(contatos):
    for i, contato in enumerate(contatos, start=1): # a função enumerate() é responsável por retornar um objeto enumerado.
        # Objeto enumerado é uma coleção de tuplas que contém o índice e o valor de cada item da coleção.
        # O parâmetro start=1 é responsável por iniciar a contagem a partir do número 1.
        print(f"{i}. Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")

# Função principal
def main():
    arquivo = r"E:\Biblioteca\VisualCode\GitHub\files\agenda.json"
    contatos = carregar_contatos(arquivo)
    
    while True:
        print("\n--- Agenda de Contatos ---")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_contato(contatos)
            salvar_contatos(contatos, arquivo)
        elif opcao == "2":
            listar_contatos(contatos)
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
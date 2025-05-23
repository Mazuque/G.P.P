agenda = {}

def inserir_contato():
    nome = input("Digite o nome do contato: ").strip()
    telefone = input("Digite o telefone: ").strip()
    email = input("Digite o email: ").strip()
    agenda[nome.lower()] = {'telefone': telefone, 'email': email}
    print("Contato adicionado com sucesso!")

def buscar_contato():
    nome = input("Digite o nome do contato a buscar: ").strip().lower()
    if nome in agenda:
        print(f"\nNome: {nome.title()}")
        print(f"Telefone: {agenda[nome]['telefone']}")
        print(f"Email: {agenda[nome]['email']}")
    else:
        print("Contato não encontrado.")

def deletar_contato():
    nome = input("Digite o nome do contato a deletar: ").strip().lower()
    if nome in agenda:
        del agenda[nome]
        print("Contato deletado com sucesso.")
    else:
        print("Contato não encontrado.")

def listar_contatos():
    if agenda:
        print("\nContatos registrados:")
        for nome, info in agenda.items():
            print(f"- {nome.title()} | Telefone: {info['telefone']} | Email: {info['email']}")
    else:
        print("A agenda está vazia.")

def menu():
    while True:
        print("\nAgenda Digital")
        print("1. Inserir contato")
        print("2. Buscar contato")
        print("3. Deletar contato")
        print("4. Listar todos os contatos")
        print("5. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            inserir_contato()
        elif opcao == '2':
            buscar_contato()
        elif opcao == '3':
            deletar_contato()
        elif opcao == '4':
            listar_contatos()
        elif opcao == '5':
            print("Encerrando agenda.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()

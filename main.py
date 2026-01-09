def menu():
    print("=== Controle Administrativo ===")
    print("1 - Cadastrar item")
    print("2 - Listar itens")
    print("3 - Sair")

itens = []

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do item: ")
        itens.append(nome)
        print("Item cadastrado com sucesso!\n")

    elif opcao == "2":
        print("Itens cadastrados:")
        for item in itens:
            print(f"- {item}")
        print()

    elif opcao == "3":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!\n")

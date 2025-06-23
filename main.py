from cliente import Cliente

def menu():
    cliente = Cliente()
    while True:
        print("\n Menu Crud - Clientes")
        print("1 - Adiconar Cliente")
        print("2 - Listar Clientes")
        print("3 - Atualizar Clientes")
        print("4 - Deletar Cliente")
        print("5 - Buscar Cliente por ID")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            cliente.adicionar_cliente(nome, email)

        elif opcao == "2":
            cliente.listar_clientes()
        
        elif opcao == "3":
            id_cliente = int(input("ID do Cliente: "))
            novo_nome = input("Novo nome: ")
            novo_email = input("Novo email: ")
            cliente.atualizar_cliente(id_cliente, novo_nome, novo_email)
        
        elif opcao == "4":
            id_cliente = int(input("ID do Cliente: "))
            cliente.deletar_cliente(id_cliente)

        elif opcao == "5":
            id_cliente = int(input("ID do Cliente: "))
            cliente.buscar_cliente_por_id(id_cliente)
        
        
        elif opcao == "0":
            print("Encerrando sistema!")
            cliente.db.close()
            break

        else:
            print("Opção invalida!")

if __name__ == '__main__':
    menu()
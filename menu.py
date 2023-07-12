import users
import utils


def menu(n):
    usuarios = {}
    while n:
        print("1 - Criar Usuário\n" +
              "2 - Editar Usuário\n" +
              "3 - Excluir Usuário\n" +
              "4 - Listar Usuários\n" +
              "5 - Adicionar dinheiro na carteira\n"
              "6 - Oferecer Carona\n" +
              "7 - Procurar Carona\n" +
              "8 - Sugerir  Carona\n" +
              "9 - Histórico de Caronas\n" +
              "10 - Avaliação de perfil\n" +
              "11 - Valor Extra\n" +
              "12 - Painel DEBUG\n" +  # Para Debug
              "0 - Sair")

        option = int(input())
        if option == 0:
            n = 0
        elif option == 1:
            print("Criação de Usuário")
            users.create(usuarios)

        elif option == 2:
            print("Edição de Usuário")
            users.edit(usuarios)

        elif option == 3:
            print("Exclusão de Usuário")
            users.delete(usuarios)

        elif option == 4:
            print("Listagem de usuários:")
            users.list_users(usuarios)
        elif option == 5:
            print("Adicionar dinheiro na carteira")
            users.wallet(usuarios)

        elif option == 6:
            print("Procurar/sugerir  Carona")

        elif option == 7:
            print("Oferecer carona")

        elif option == 8:
            print("Adicionar relacionamento")

        elif option == 9:
            print("Histórico de viagens")

        elif option == 10:
            print("Sistema de avaliação de perfil")

        elif option == 11:
            print("Valor Extra")

        elif option == 12:
            print("PAINEL DEBUG")
            utils.adm(usuarios)

        else:
            print("Escolha um opção válida")

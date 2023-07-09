import users
import utils


def menu(n):
    usuarios = {}
    while n:
        print("1 - Criar Usuário\n" +
              "2 - Editar Usuário\n" +
              "3 - Excluir Usuário\n" +
              "4 - Listar Usuários\n" +
              "5 - Oferecer Carona\n" +
              "6 - Procurar Carona\n" +
              "7 - Sugerir  Carona\n" +
              "8 - Histórico de Caronas\n" +
              "9 - Avaliação de perfil\n" +
              "10 - Valor Extra\n" +
              "11 - Painel DEBUG\n" +  # Para Debug
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
            print("Procurar/sugerir  Carona")

        elif option == 6:
            print("Oferecer carona")

        elif option == 7:
            print("Adicionar relacionamento")

        elif option == 8:
            print("Histórico de viagens")

        elif option == 9:
            print("Sistema de avaliação de perfil")

        elif option == 10:
            print("Valor Extra")

        elif option == 11:
            print("PAINEL DEBUG")
            utils.adm(usuarios)

        else:
            print("Escolha um opção válida")

import rides
import users
import utils


def menu(n):
    usuarios = {}
    caronas = {}
    while n:
        print('01 - Criar Usuário',
              '02 - Editar Usuário',
              '03 - Excluir Usuário',
              '04 - Listar Usuários',
              '05 - Adicionar dinheiro na carteira',
              '06 - Oferecer Carona',
              '07 - Procurar Carona',
              '08 - Sugerir  Carona',
              '09 - Histórico de Caronas',
              '10 - Avaliação de perfil',
              '11 - Valor Extra',
              '12 - Painel DEBUG',  # Debug
              '00 - Sair', sep='\n')

        option = int(input())

        if option == 0:
            n = False
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
            users.add_money(usuarios)

        elif option == 6:
            print("Oferecer carona")
            rides.offer_ride(caronas, usuarios)

        elif option == 7:
            print("Procurar  Carona")
            rides.search_ride(caronas)

        elif option == 8:
            print("Sugerir  Carona")

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

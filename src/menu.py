import rides
import users
import utils


def menu(n):
    usuarios = {}
    caronas = {}
    caronas_sugeridas = {}
    id_carona = 0
    quant_avaliacao = 0
    quant_usuarios = 0
    while n:
        print('1 - Criar Usuário',
              '2 - Editar Usuário',
              '3 - Excluir Usuário',
              '4 - Listar Usuários',
              '5 - Adicionar dinheiro na carteira',
              '6 - Oferecer Carona',
              '7 - Procurar Carona',
              '8 - Sugerir  Carona',
              '9 - Histórico de Caronas',
              '10 - Avaliação das caronas',
              '11 - Valor Extra',
              '12 - Painel DEBUG',  # Debug
              '0 - Sair', sep='\n')

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
            confirm = input("Gostaria de ver as caronas sugeridas?[S/N] ")
            confirm = confirm.lower()

            if confirm == 's':
                rides.confirm_ride(caronas_sugeridas, caronas, usuarios)
            elif confirm == 'n':
                print("Continue oferencedo a carona")
                id_carona += 1
                rides.offer_ride(caronas, usuarios, id_carona, quant_avaliacao, quant_usuarios)
            else:
                option = -1
        elif option == 7:
            print("Procurar  Carona")
            rides.search_ride(caronas, usuarios)

        elif option == 8:
            print("Sugerir  Carona")
            id_carona += 1
            rides.suggested_ride(caronas_sugeridas, id_carona)

        elif option == 9:
            print("Histórico de viagens")
            users.get_rides(usuarios)
        elif option == 10:
            print("Avaliação de caronas")
            quant_avaliacao += 1
            rides.rate_ride(usuarios, quant_avaliacao, caronas)
        elif option == 11:
            print("Enviar valor extra pela carteira")
            users.tip_user(caronas, usuarios)
        elif option == 12:
            print("PAINEL DEBUG")
            utils.adm(usuarios)

        else:
            print("Escolha um opção válida")

import uuid
import getpass
caronas = {}
usuarios = {}

def create(usuarios):
    email = input("Informe um email: ")
    cpf = input("Informe um cpf: ")
    name = input("Defina um nome de usuário: ")
    password = getpass.getpass("Defina uma senha de usuário: ")
    confirmation = input("Deseja adicionar dinheiro a carteira? [S/N] ")
    confirmation.lower()

    if confirmation == "s":
        money = float(input("Quanto gostaria de adicionar? "))
    else:
        money = 0

    option = input("Gostaria de adicionar um carro? [S/N]")
    option.lower()

    if option == "s":
        car_model = input("Modelo do carro: ")
        color = input("Cor: ")
        plate = input("Placa: ")
    else:
        car_model = None
        color = None
        plate = None

    novo_usuario = {"cpf": cpf,
                    "email": email,
                    "nome": name,
                    "senha": password,
                    "carteira": money,
                    "historico": {},
                    "carro": {
                        "modelo": car_model,
                        "cor": color,
                        "placa": plate
                    }
                    }
    usuarios[cpf] = novo_usuario
    msg = 'CONTA CRIADA COM SUCESSO!'
    print("-" * len(msg))
    print(msg)
    print("-" * len(msg))
    menu(cpf)
    


def edit(usuarios, cpf):
    print(f'CPF: {cpf}\n')
    print("Dados do usuário:")
    print("E-mail: " + usuarios[cpf]["email"])
    print("Nome: " + usuarios[cpf]["nome"])
    print("Carro: " + str(usuarios[cpf]["carro"]))
    print("Para alterar a senha, digite 'senha'")

    option = input("Qual dado gostaria de alterar? ")
    option.lower()
    if option == "carro":
        model = input("Digite o novo modelo: ")
        color = input("Digite a nova cor:")
        plate = input("Digite a nova placa:")
        new_value = {
            "modelo": model,
            "cor": color,
            "placa": plate
        }
    else:
        new_value = input("Digite o novo " + option + ":")
    confirm = input("O " + option + " será alterado para " + str(new_value) + "\nTem certeza? [S/N]")
    confirm.lower()
    if confirm == "s":
        usuarios[cpf][option] = new_value
        print("Dado alterado com sucesso!")
    else:
        print("Operação cancelada!")


def get_rides(usuarios, cpf):
    try:
        print(usuarios[cpf]['historico'])
    except KeyError:
        print("Este usuário não possui nenhuma corrida realizada!")


def add_money(usuarios, cpf):
    
    print(f'CPF: {cpf}\n')
    print("Dados do usuário:")
    print("E-mail: " + usuarios[cpf]["email"])
    print("Nome: " + usuarios[cpf]["nome"])

    value = input("Quanto dinheiro gostaria de adicionar? ")
    confirm = input(
        value + " reais será adicionado na carteira do(a) " + str(usuarios[cpf]["nome"]) + "\nTem certeza? [S/N]")
    confirm.lower()

    if confirm == "s":
        usuarios[cpf]["carteira"] += float(value)
        print("Dinheiro adicionado com sucesso!")
    else:
        print("Operação cancelada!")


def tip_user(caronas, usuarios, cpf):

    id_ultima_carona = max(usuarios[cpf]['historico'].keys())

    print("Última carona: ")
    print(usuarios[cpf]['historico'][id_ultima_carona])

    gorjeta = input("Gostaria de enviar um valor extra ao motorista? [S/N]")

    gorjeta.lower()

    if gorjeta == 'n':
        print("Certo, abortando operação...")
        return
    elif gorjeta == 's':
        valor = float(input("Insira o valor extra a ser enviado da sua carteira: "))

        if usuarios[cpf]['carteira'] >= valor:
            print("Enviando valor para o motorista...")
            usuarios[cpf]['carteira'] -= valor
            usuarios[caronas[id_ultima_carona]['cpf']]['carteira'] += valor
        else:
            print("Valor na carteira insuficiente! Adicione mais fundos e tente novamente!")
            return


def delete(usuarios, cpf):
    try:
        
        print("CPF: " + usuarios[cpf]["cpf"] +
              "Nome: " + usuarios[cpf]["nome"])
        print("Tem certeza que deseja remover? ")
        option = input()
        option.lower()
        if option == "s":
            usuarios.pop(cpf)
            print("Usuário removido com sucesso!")
        else:
            print("Operação cancelada!")
    except KeyError:
        print("CPF inválido!")


def list_users(usuarios):
    for key in usuarios.keys():
        print(f'CPF: {key}\n')
        print("Dados do usuário:")
        for element in usuarios[key]:
            if element == "senha":
                continue
            print(element + ": " + str(usuarios[key][element]) + "\n")


def offer_ride(caronas, usuarios, id_carona, cpf):
    origem = input('Digite a origem: ')
    destino = input('Digite o destino: ')
    vagas = int(input("Digite o número de vagas disponíveis: "))
    valor = input("Digite o valor necessário de contribuição para gasolina: ")

    try:
        nova_carona = {
            'id': id_carona,
            'origem': origem,
            'destino': destino,
            'cpf': usuarios[cpf]['cpf'],
            'nome': usuarios[cpf]['nome'],
            'carro': usuarios[cpf]['carro'],
            'vagas': vagas,
            'valor': float(valor),
            'avaliacao' : 0
            
            
        }
    except KeyError:
        print("CPF não encontrado! Tente de novo ou cadastre-se!")
        return

    caronas[id_carona] = nova_carona
    print('Corrida cadastrada com sucesso!\n')


def search_ride(caronas, usuarios, cpf):
    origem = input('Digite a origem: ')
    destino = input('Digite o destino: ')
    vagas = int(input("Quantas vagas você precisa? "))
    caronas_encontradas = []

    for carona in caronas:
        if caronas[carona]['origem'] == origem and caronas[carona]['destino'] == destino and caronas[carona]['vagas'] \
                >= vagas:
            caronas_encontradas.append(carona)

    if len(caronas_encontradas) == 0:
        print('Nenhuma carona compatível encontrada.')
        return
    else:
        j = 1
        print('Caronas encontradas: ')
        for carona in caronas_encontradas:
            print(f'{j}- {caronas[carona]}')
            j += 1

    opcao = int(input('Qual carona deseja? '))

    if caronas_encontradas[opcao - 1] == 0:
        print('Opção inválida!')
        return

    else:
        id_carona = caronas_encontradas[opcao - 1]
        opcao_pagamento = int(input("Qual o método de pagamento da contribuição?\n"
                                    + "1 - Carteira\n" + "2 - Outros (Dinheiro, cartão, pix)\n"))
        if opcao_pagamento == 1:
            if usuarios[cpf]['carteira'] >= caronas[id_carona]['valor'] * vagas:
                usuarios[cpf]['carteira'] -= caronas[id_carona]['valor'] * vagas
                usuarios[caronas[id_carona]['cpf']]['carteira'] += caronas[id_carona]['valor'] * vagas
            else:
                print("Valor na carteira insuficiente! Alterando para outras formas de pagamento...")

        usuarios[cpf]['historico'][id_carona] = caronas[id_carona]

        if vagas == caronas[id_carona]['vagas']:
            caronas.pop(id_carona)
            print("Carona totalmente preenchida! Acerte os detalhes com o motorista!")
        else:
            caronas[id_carona]['vagas'] -= vagas
            print("Esse carona ainda tem vagas, verifique com o motorista se ele vai aguardar ou já irá iniciar!")

        print('Pedido de carona concluído!\n')


def rate_ride(usuarios, cpf):
    caronas_encontradas = []

    for carona in usuarios[cpf]['historico']:
        if usuarios[cpf]['historico'][carona]['avaliacao'] == 0:
            caronas_encontradas.append(carona)

    if len(caronas_encontradas) == 0:
        print('Nenhuma carona sem avaliação encontrada.')
        return
    else:
        j = 1
        print('Caronas sem avaliação: ')
        for carona in caronas_encontradas:
            print(f'{j}- {usuarios[cpf]["historico"][carona]}')
            j += 1

    opcao = int(input('Qual carona deseja avaliar? '))

    if caronas_encontradas[opcao - 1] == 0:
        print('Opção inválida!')
        return
    else:
        id_carona = caronas_encontradas[opcao - 1]

        nota = int(input("Digite a nota para essa carona, de 1 a 5: "))

        usuarios[cpf]['historico'][id_carona] = nota

        print("Avaliação registrada com sucesso!")



def login():
     
     print("1. Fazer Login")
     print("2. Criar Login")
     print("0. Encerrar App")

     option = input('Qual opção deseja? ')

     while True:
         
         if option == '1':
             
             cpf = input("Digite o CPF: ")
             password = getpass.getpass("Digite a senha: ")

             if cpf in usuarios and usuarios[cpf]["senha"] == password:
                 print(f"Login bem-sucedido! bem vindo {usuarios[cpf]['nome']}!")
                 menu(cpf)
                 break
             else:                  
                  print("CPF ou senha incorretos. Tente novamente.") 
                  login()
                  break  
                 
         elif option == '2':
             create(usuarios)
             break
             
         elif option == '0':    
             break
            
       

def menu(cpf):
    while True:
        print("\n----- MENU PRINCIPAL -----")
        print("1. Editar sua conta")
        print("2. Ver histórico de caronas")
        print("3. Adicionar dinheiro à carteira")
        print("4. Dar gorjeta ao motorista")
        print("5. Excluir sua conta")
        print("6. Listar todos os usuários")
        print("7. Oferecer uma carona")
        print("8. Pesquisar por caronas")
        print("9. Avaliar uma carona")
        print("0. Sair")

        choice = input("Digite o número da opção desejada: ")

        
        if choice == "1":
            edit(usuarios, cpf)
        elif choice == "2":
            get_rides(usuarios, cpf)
        elif choice == "3":
            add_money(usuarios, cpf)
        elif choice == "4":
            tip_user(caronas, usuarios, cpf)
        elif choice == "5":
            delete(usuarios, cpf)
        elif choice == "6":
            list_users(usuarios)
        elif choice == "7":
            offer_ride(caronas, usuarios, str(uuid.uuid4()), cpf)
        elif choice == "8":
            search_ride(caronas, usuarios, cpf)
        elif choice == "9":
            rate_ride(usuarios, cpf)
        elif choice == "0":
            print("Obrigado por utilizar nosso sistema de caronas. Até logo!")
            login()
            break
        else:
            print("Opção inválida. Por favor, digite um número válido de opção.")


login()            


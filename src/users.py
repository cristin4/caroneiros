import getpass


def create(usuarios):
    email = input("Informe um email: ")
    cpf = input("Informe um cpf: ")
    name = input("Defina um nome de usuário: ")
    password = input("Defina uma senha de usuário: ")
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


def edit(usuarios):
    print("Informe o CPF da conta a ser editado: ")
    cpf = input()
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


def wallet(usuarios):
    print("Informe o CPF da conta  que deseja que seja adicionado dinheiro a carteira: ")
    cpf = input()
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


def delete(usuarios):
    try:
        print("Informe o CPF da conta a ser removida: ")
        cpf = input()
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

""" alguns testes """


import pickle
import re # corrigir

from os import path, makedirs
from getpass import getpass
from modules.menu import Menu, dye  # corrigir
from modules.users import User, Regular, Admin, users # corrigir
from modules.carpools import Carpool, carpools, Any, Union # corrigir

# ########################################################################### variáveis globais
...



def show_carpools(keys: set) -> bool:
    """Mostrar caronas"""
    total = len(keys)

    for key in keys:
        carpools[key].view()

    if total == 0:
        print(dye("Não há caronas disponíveis!", "red"))
        return False

    if total == 1:
        print(dye(f"{total} carona disponível!", "red"))
    else:
        dye(f"{total} caronas disponíveis!", "red")

    return True

def create_carpool():
    """6| Oferecer carona"""
    raise NotImplementedError
    # ride_date = input('Quando será a viagem?\n  ~> ') # corrigir
    origin = input("Qual o local de partida?\n  ~> ")
    destination = input("Qual o local de destino?\n  ~> ")

    match input(
        "Deseja ofertar ou demandar esta carona? " + dye("[o/d]", "red") + "\n  ~> "
    ).lower():
        case "o":
            driver_username = active_user.username
            seats_provided = int(input("Quantas vagas deseja disponibilizar?\n  ~> "))
            status = "offered"
            role = "driver"
            passenger_username = None
        case "d":
            driver_username = None
            seats_provided = None
            status = "demanded"
            role = "passenger"
            passenger_username = active_user.username
        case _:
            print(dye("Opção inválida!", "red"))
            return

    carpool = Carpool(destination, origin, driver_username, status)
    carpool.seats_provided = seats_provided  # tratar int
    carpool.add_passenger(passenger_username)

    carpool.view()
    if (
        input("Digite 'ok' para confirmar a carona " + status + "*.\n  ~> ").lower()
        == "ok"
    ):
        identifier = carpool.identifier
        carpools[identifier] = carpool
        active_user.rides_history.update({identifier: role})
        print(dye("Carona " + status + "* com sucesso!", "green"))
    else:
        print(dye("Carona não " + status + "*!", "red"))

def hitch_a_carpool(user, carpool_key: str):
    """¿?"""
    raise NotImplementedError
    carpool: Carpool = carpools[carpool_key]
    if (
        not carpool.has_driver()
        and input(
            dye("Sapoha ainda não tem motorista!", "red")
            + "\n"
            + "Digite 'm' para se tornar o motorista.\n  ~> "
        ).lower()
        == "m"
    ):
        seats_provided = int(input("Quantas vagas deseja disponibilizar?\n  ~> "))
        if seats_provided < len(carpool.passengers_usernames):
            print(
                dye(
                    "Quantidade insuficiente para a demanda! (mín.: "
                    + str(len(carpool.passengers_usernames))
                    + " vagas)",
                    "red",
                )
            )
            return
        status = "offered"
        if (
            input("Digite 'ok' para confirmar a carona " + status + "*.\n  ~> ").lower()
            == "ok"
        ):
            carpool.driver_username = active_user.username
            carpool.status = status
            carpool.seats_provided = seats_provided
            active_user.rides_history.update({carpool_key: "driver"})
            carpool.view()
            print(dye("Carona " + status + "* com sucesso!", "green"))
            return

    if carpool.driver_is(active_user.username):
        print(dye("Você é o motorista da carona!", "red"))
        return

    if active_user.username in carpool.passengers_usernames:
        print(dye("Você já é passageiro da carona!", "red"))
        return

    if not carpool.has_seats_available():
        print(dye("Não há vagas!", "red"))
        return

    if input("Digite 'ok' para tomar a carona.\n  ~> ").lower() == "ok":
        carpool.passengers_usernames.append(user.username)
        role = "passenger"
        active_user.rides_history.update({carpool_key: role})
        print(dye("Carona tomada com sucesso!", "green"))
    else:
        print(dye("Carona não tomada!", "red"))

def find_ride() -> None:
    """7| Procurar carona"""
    raise NotImplementedError
    match input(
        "Vizualizar caronas ofertadas ou demandadas? "
        + dye("[o/d]*", "red")
        + "\n  ~> "
    ).lower():
        case "o":
            status = "offered"
        case "d":
            status = "demanded"
        case "*":
            status = None
        case _:
            print(dye("Opção inválida!", "red"))
            return

    keys = carpools_by_status(status)

    if not show_carpools(keys):
        return

    key = input(
        "Digite o imenso identificador da carona para pegá-la."
        + dye(" Obs.: ≠ para retornar.", "red")
        + "\n  ~> "
    )

    key = re.sub(
        r"[\W]", "", key
    )  # tentativa de filtro para manter apenas letras e números

    if key in keys:
        hitch_a_carpool(active_user, key)

# def profile() -> None:
#     return profile_menu.run_in_loop()

def rate_profile():
    """10| Avaliar perfil"""

    driver_user = input("Qual o ID do usuário a ser avaliado?\n  ~> ")
    profile_rating_score = input("Qual sua nota, de 0 a 5, para o usuário <?>?\n  ~> ")

    print(dye("Perfil avaliado com sucesso!", "green"))

def contribute():
    """11| Valor extra"""

    driver_user = input("Qual o ID do destinatário da contribuição?\n  ~> ")
    profile_rating_score = input("Qual o valor da contribuição, em BRL?\n  ~> ")
    raise NotImplementedError
    print(dye("Contribuição destinada a <?> com sucesso!", "green"))


# ######################################################################### funcões: principais
def sign_up(*args) -> bool:
    # users: dict[str, Any] = args[0]

    username = input("Defina um nome de usuário.\n  ~> ")
    
    if users.get(username, False):
        print(dye("Nome de usuário já cadastrado!", "red"))
    else:
        password = getpass("Defina uma senha de acesso.\n  ~> ")
        user = Regular(username, password)
        if Menu.confirm("Confirmar o cadastro deste usuário?"):
            users.update({user.username: user})
            print(dye("Usuário cadastrado com sucesso!", "green"))
            user.access_user_menu()
        else:
            print(dye("Cadastro cancelado!", "red"))
    
    return True

def sign_in(*args) -> bool:
    # users: dict[str, Any] = args[0]

    username: str = input("Nome de usuário.\n  ~> ")

    user = users.get(username, False) 
    if user:
        password = getpass("Senha de acesso.\n  ~> ")
        if user.password_is(password):
            print(dye(f"Olá, {username}!", "red"))
            user.access_user_menu()
        else:
            print(dye("Senha inválida!", "red"))
    else:
        print(dye("Usuário não cadastrado!", "red"))

    return True

def unsign(*args) -> bool:
    # users: dict[str, Any] = args[0]

    username: str = input("Nome de usuário.\n  ~> ")

    user = users.get(username, False) 
    
    if type(user) is Admin:
        print(dye(f'Administradores não podem ser removidos.', 'red'))
        return True
    
    if user:
        password = getpass("Senha de acesso.\n  ~> ")
        if user.password_is(password):
            if Menu.confirm("Confirmar o descadastro deste usuário?"):
                del users[user.username]
                print(dye("Usuário descadastrado com sucesso!", "green"))
            else:
                print(dye("Descadastro cancelado!", "red"))
        else:
            print(dye("Senha inválida!", "red"))
    else:
        print(dye("Usuário não cadastrado!", "red"))

    return True

# ######################################################################## funcões: temporárias
def debug(*args) -> bool:
    """¿?"""
    debug_menu.run_in_loop()
    return True

def print_all_users(*args) -> bool:
    """¿?"""
    User.print_from(users)
    print(dye(f"{len(users)}", "red"))
    return True

def print_all_carpools(*args) -> bool:
    """¿?"""
    Carpool.print_from(carpools)
    print(dye(f"{len(carpools)}", "red"))
    return True

def carpools_by_status(status: str | None = None) -> set:
    """filtra burramente as caronas pelo status"""
    keys: set = set()
    if status is None:
        for key, carpool in carpools.items():
            keys.add(key)
    else:
        for key, carpool in carpools.items():
            if carpool.status == status:
                keys.add(key)
    return keys


# ########################### funcões: p/ ler/serializar e desserializar/escrever de/em arquivo
def try_write_pkl_dict(dictionary: dict[str, User|Regular|Admin], path: str) -> None:
    """ Tentar serializar e escrever dicionário, em arquivo """
    exception_msg = None
    try:
        with open(path, "wb") as pickle_file:
            print(dye(f"Tentando serializar objeto ({type(dictionary)})…", "yellow"))
            pickle.dump(dictionary, pickle_file)
        print(dye(f"Tentando escrever em {path}…", "yellow"))
    except FileNotFoundError:
        exception_msg = f"{path} não foi encontrado."
    except (IOError, OSError) as error:
        exception_msg = f"Erro de E/S ao escrever em {path}: {error}."
    except pickle.PicklingError as error:
        exception_msg = f"Erro ao serializar objeto ({type(dictionary)}): {error}."
    except MemoryError:
        exception_msg = f"Erro de falta de memória ao escrever em {path}."
    except Exception as error:
        exception_msg = f"Erro desconhecido: {error}."
    else:
        print(dye(f"Objeto ({type(dictionary)}) serializado e escrito com sucesso em {path}!", "green"))
    finally:
        if exception_msg is not None:
            print(dye(exception_msg, 'red'))

def try_read_pkl_dict(path: str) -> dict[str, User|Regular|Admin]:
    """ Tentar ler e desserializar dicionário, de arquivo """
    exception_msg = None
    dictionary: dict[str, User|Regular|Admin] = {}
    try:
        print(dye(f"Tentando ler de {path}…", "yellow"))
        with open(path, "rb") as pickle_file:
            print(dye(f"Tentando desserializar objeto ({type(dictionary)})…", "yellow"))
            dictionary = pickle.load(pickle_file)
    except FileNotFoundError:
        exception_msg = f"{path} não foi encontrado."
    except EOFError:
        exception_msg = f"Erro de fim de arquivo ao ler de {path}."
    except pickle.UnpicklingError as error:
        exception_msg = f"Erro ao desserializar objeto ({type(dictionary)}): {error}."
    except Exception as error:
        exception_msg = f"Erro desconhecido: {error}."
    else:
        print(dye(f"Objeto ({type(dictionary)}) lido e desserializado com sucesso de {path}!", "green"))
    finally:
        if exception_msg is not None:
            print(dye(exception_msg, 'red'))
        return dictionary


# ########################################################################## instanciando menus
sign_menu = Menu(
    title="Menu: Início",
    options=[
        ("Inscrever-se", sign_up, users),
        ("Entrar", sign_in, users),
        (dye("DEBUG", 'red'), debug, None),
        ("Desinscrever-se", unsign, users),
        ("Encerrar", "Encerrando…", None)
    ], invalid_selection_text="Seleção inválida!")

debug_menu = Menu(
    title="Menu: DEBUG",
    options=[
        ("print all users", print_all_users, None),
        #  ('write dict users', write_dict_users, None),
        #  ('read dict users', read_dict_users, None),
        ("print all carpools", print_all_carpools, None),
        #  ('write dict carpools', write_dict_carpools, None),
        #  ('read dict carpools', read_dict_carpools, None),
        ("↩", "see you soon…")
    ], invalid_selection_text="Seleção inválida!")


# ##################################################################################### rodando

if __name__ == "__main__":
    BOOL = True

    if BOOL:
        users.update(try_read_pkl_dict('io/users.pkl'))
        carpools.update(try_read_pkl_dict('io/carpools.pkl'))

        if not len(users):
            built_in_user = Admin('admin', 'admin')
            users.update({built_in_user.username: built_in_user})

        if not len(carpools):
            # carpools.update()
            ...

    sign_menu.run_in_loop()

    if BOOL:
        if not path.exists("io"):
            makedirs("io")

        try_write_pkl_dict(users, 'io/users.pkl')
        try_write_pkl_dict(carpools, 'io/carpools.pkl')

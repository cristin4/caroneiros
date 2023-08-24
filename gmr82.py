''' alguns testes '''

import pickle
import re

from modules.menu import Menu, dye  # corrigir
from modules.user import User  # corrigir
from modules.carpool import Carpool  # corrigir


def create_user(username):
    '''1| Criar usuário'''
    user = User(username)
    user.password = input('Defina uma senha de acesso.\n  ~> ')

    print(dye('Usuário cadastrado com sucesso!', 'red'))
    return user


def change_username():
    '''¿?'''
    new_username = input('Defina o novo nome de usuário*.\n  ~> ')

    if new_username == active_user.username:
        print(dye('Nome de usuário alterado!', 'red'))
        return

    if users.get(new_username):
        print(dye('Nome já utilizado por outro usuário!'))
        return

    users.pop(active_user.username)
    active_user.change_username(new_username)
    users[active_user.username] = active_user
    print(dye('Nome de usuário alterado!'))


def change_password():
    '''¿?'''
    new_password = input('Defina a nova senha.\n  ~> ')
    active_user.change_password(new_password)
    print(dye('Senha alterada!', 'red'))


def edit_profile_attribute():
    '''¿?'''
    key = input('Insira a chave do atributo.\n  ~> ')
    value = input('Defina o valor do atributo. ' +
                  dye(" Obs.: '' para remover.", 'red') + '\n  ~> ')

    if value == '':
        value = None
    msg = active_user.profile.edit_attribute(key, value)
    print(dye('Atributo ' + msg + '!'))


def edit_user():
    '''2| Editar perfil do usuário'''
    # show_profile()
    edit_user_menu.run_in_loop()


def show_profile():
    '''Mostrar perfil'''
    active_user.show_profile()


def show_carpool(carpool_identifier):
    '''¿?'''
    carpools[carpool_identifier].show_me()


def show_carpools(keys):
    '''¿?'''
    total = len(keys)

    for key in keys:
        show_carpool(key)

    if total == 0:
        print(dye('Não há caronas disponíveis!', 'red'))
        return False

    if total == 1:
        print(
            dye(f'{total} carona disponível!', 'red'))
    else:
        dye(f'{total} caronas disponíveis!', 'red')

    return True


def create_carpool():
    '''6| Oferecer carona'''
    # ride_date = input('Quando será a viagem?\n  ~> ') # corrigir
    origin = input('Qual o local de partida?\n  ~> ')
    destination = input('Qual o local de destino?\n  ~> ')

    match input('Deseja \'o\' ofertar ou \'s\' solicitar esta carona?\n  ~> ').lower():
        case 'o':
            driver_username = active_user.username
            seats_available = int(input('Quantas vagas disponíveis?\n  ~> '))
            status = 'offered'
            role = 'driver'
            passengers_usernames = []
        case 's':
            driver_username = None
            seats_available = int(-1)
            status = 'demanded'
            role = 'passenger'
            passengers_usernames = [active_user.username]
        case _:
            print(dye('Opção inválida!', 'red'))
            return

    carpool = Carpool(destination, origin, driver_username)
    carpool.status = status
    carpool.seats_available = int(seats_available)  # tratar int
    carpool.passengers_usernames = passengers_usernames

    if input('Digite \'ok\' para confirmar a carona ' + status + '*.\n  ~> ').lower() == 'ok':
        identifier = carpool.identifier
        carpools[identifier] = carpool
        active_user.rides_history.update({identifier: role})
        print(
            dye('Carona ' + status + '* com sucesso!'))
    else:
        print(
            dye('Carona não ' + status + '*!'))


def give_this_carpool():
    '''¿?'''
    response = input('Será o motorista?' +
                     dye(' Obs.: ≠ para sair.', 'red') + '\n  ~> ')

    print(re.fullmatch(r'([S-s][I-i]*[M-m]*)+', response))


def hitch_a_carpool(user, carpool_key):
    '''¿?'''
    if carpools[carpool_key].driver is None:
        print(dye('sapoha ainda nao tem motorista, deseja dirigir?', 'red') + '\n  ~> ')
        give_this_carpool()
        return

    # solicitar ao motorista?

    else:
        pass  # acicionar como motor
    print(user.tuple_attributes(), carpool_key)


def find_ride():
    '''7| Procurar carona'''
    match input(
            'Vizualizar caronas ofertadas ou solicitas? ' + dye('[o/s]', 'red') + '\n  ~> ').lower():
        case 'o':
            status = 'offered'
        case 's':
            status = 'demanded'
        case 'all':
            status = None
        case _:
            print(dye('Opção inválida!', 'red'))
            return

    keys = carpools_by_status(status)

    if not show_carpools(keys):
        return

    key = input('Digite o imenso identificador da carona para pegá-la.' +
                dye(' Obs.: ≠ para sair.') + '\n  ~> ')

    key = re.sub(r'[\D]+', '', key)

    if key in keys:
        hitch_a_carpool(active_user, key)


def rate_profile():
    '''10| Avaliar perfil'''

    driver_user = input('Qual o ID do usuário a ser avaliado?\n  ~> ')
    profile_rating_score = input(
        'Qual sua nota, de 0 a 5, para o usuário <?>?\n  ~> ')

    print(
        dye('Perfil avaliado com sucesso!', 'red'))


def contribute():
    '''11| Valor extra'''

    driver_user = input('Qual o ID do destinatário da contribuição?\n  ~> ')
    profile_rating_score = input(
        'Qual o valor da contribuição, em BRL?\n  ~> ')

    print(
        dye('Contribuição destinada a <?> com sucesso!', 'red'))


def sign_up():
    '''¿?'''

    username = input('Defina um nome de usuário*.\n  ~> ')
    if users.get(username):
        print(dye('Usuário já cadastrado!', 'red'))
        return

    global active_user  # corrigir
    active_user = create_user(username)
    users[active_user.username] = active_user
    access(active_user)


def unsign():
    '''¿?'''
    response = input('Confirma a desinscrição do usuário? ' + dye('[s]', 'red') + '\n  ~> ')
    if response[0].lower() == 's':
        # delete_user(active_user)
        del users[active_user.username]
        return True
    return None


def access(user):
    '''¿?'''

    print(dye(f'Olá, {user.username}!', 'red'))
    print(user.tuple_attributes())
    user_menu.run_in_loop()


def sign_in():
    '''¿?'''
    username = input('Nome de usuário.\n  ~> ')

    if username in users:
        password = input('Senha de acesso.\n  ~> ')
        global active_user  # corrigir
        if users[username].password == password:
            active_user = users[username]
            access(active_user)
        else:
            print(dye('Senha inválida!', 'red'))
    else:
        print(dye('Usuário não cadastrado!', 'red'))


def debug():
    '''¿?'''
    debug_menu.run_in_loop()


def list_all_users():
    '''¿?'''
    User.list_users_in(users)
    print(dye(f'{len(users)}', 'red'))


def list_all_carpools():
    '''¿?'''
    Carpool.list_carpools_in(carpools)
    print(dye(f'{len(carpools)}', 'red'))


def carpools_by_status(status=None):
    '''filtra burramente as caronas pelo status'''
    keys = set(())
    if status is None:
        for key, carpool in carpools.items():
            keys.add(key)
    else:
        for key, carpool in carpools.items():
            if carpool.status == status:
                keys.add(key)
    return keys


def write_pkl_users():
    '''¿?'''
    with open('io/users.pkl', 'wb') as pickle_file:
        pickle.dump(users, pickle_file)


def read_pkl_users():
    '''¿?'''
    global users  # corrigir
    with open('io/users.pkl',  'rb') as pickle_file:
        users = pickle.load(pickle_file)


def write_pkl_carpools():
    '''¿?'''
    with open('io/carpools.pkl', 'wb') as pickle_file:
        pickle.dump(carpools, pickle_file)


def read_pkl_carpools():
    '''¿?'''
    global carpools  # corrigir
    with open('io/carpools.pkl', 'rb') as pickle_file:
        carpools = pickle.load(pickle_file)


# ###############################################################
# import gmr82 as gmr

active_user: User
users = {}
carpools = {}


sign_menu = Menu('sign_menu',
                 {
                     'Inscrever-se': sign_up,
                     'Entrar': sign_in,
                     'DEBUG': debug,
                     'Encerrar': 'Encerrando…'
                 })

debug_menu = Menu('DEBUG_menu',
                  {
                      'list all users': list_all_users,
                      #   'write dict users': write_dict_users,
                      #   'read dict users': read_dict_users,
                      'list all carpools': list_all_carpools,
                      #   'write dict carpools': write_dict_carpools,
                      #   'read dict carpools': read_dict_carpools,
                      '↩': 'see you soon…'
                  })

user_menu = Menu('user_menu',
                 {
                     'Ver/Editar meu perfil': edit_user,
                     'Adicionar carona*': create_carpool,
                     'Procurar carona': find_ride,
                     #  'Sugerir carona': suggest_ride,
                     #  'Histórico de caronas': past_rides,
                     #  'Avaliar perfil': rate_profile,
                     #  'Valor extra': contribute,
                     'Sair': 'Saindo…'
                 })

edit_user_menu = Menu('edit_user_menu',
                      {
                          'Mostrar perfil': show_profile,
                          'Alterar nome de usuário': change_username,
                          'Alterar senha': change_password,
                          'Editar atributo': edit_profile_attribute,
                          'Desinscrever-se*': unsign,
                          'Retornar': 'Retornando…'
                      })


if __name__ == '__main__':

    BOOL = True
    if BOOL:
        try:
            read_pkl_users()
            print(dye('Carregando usuários…', 'blue'))
            read_pkl_carpools()
            print(dye('Carregando caronas…', 'blue'))
        except FileNotFoundError:
            pass

    sign_menu.run_in_loop()

    if BOOL:
        try:
            write_pkl_users()
            print(dye('Salvando usuários…', 'blue'))
            write_pkl_carpools()
            print(dye('Salvando caronas…', 'blue'))
        except FileNotFoundError:
            pass

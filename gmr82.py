''' alguns testes '''
import json
import re
# import datetime
# ═║╔╗╚╝╠╣╦╩╬
# ─│┌┐└┘├┤┬┴┼
# ─║╓╖╙╜╟╢╥╨╫


def red(string):
    '''colore a string'''
    return '\033[31m' + string + '\033[0;0m'


class Menu:
    '''rascunho de menu'''

    def __init__(self, header='menu', options=None, start=1):
        self.header = header
        self.options = options
        self.start = start
        self.longest_string_len = len(self.header)
        self.void_menu = self.options is None

        if not self.void_menu:
            self.longest_string_len = len(
                max(list(self.options.keys()), key=len))
            if len(self.header) > self.longest_string_len:
                self.longest_string_len = len(self.header)
            self.longest_string_len += 5

    def show(self):
        '''mostra opcões'''
        width = self.longest_string_len
        print(f'┌{"":─^{width}}┐',
              f'│{self.header: ^{width}}│',
              f'├{"":─^{width}}┤', sep='\n')

        if self.void_menu:
            print(f'│{"∅":^{width}}│')
            print(f'└{"":═^{width}}┘')
        else:
            for index, option in enumerate(self.options, start=self.start):
                print(f'│{f" {index: 2} {option} ":<{width}}│')

            print(f'└{"":─^{width}}┘')

    def run(self):
        '''roda menu'''
        self.show()

        if self.void_menu:
            return

        sel = input('  ~> ')

        if sel.isdigit():
            sel = int(sel)

            # Encerra o loop
            if sel == self.start + len(self.options)-1:
                print(red(
                    f'{list(self.options.items())[sel-self.start][1]: >{self.longest_string_len}}'))
                return

            # Chama uma função do menu
            if self.start <= sel < self.start + len(self.options):
                list(self.options.items())[sel-self.start][1]()
                self.run()
                return

        print(
            red(f'{"Seleção inválida!": >{self.longest_string_len}}'))
        self.run()


def create_user(username):
    '''1| Criar usuário'''
    password = input('Defina uma senha de acesso.\n  ~> ')
    attributes = {}
    history = {}

    user = {
        'password': password,
        'attributes': attributes,
        'history': history
    }

    users[username] = user
    print(red('Usuário cadastrado com sucesso!'))

    return username


def change_username():
    '''¿?'''
    global active_username

    new_username = input('Defina o novo nome de usuário*.\n  ~> ')

    if new_username == active_username:
        print(red('Nome de usuário alterado!'))
        return

    if users.get(new_username):
        print(red('Nome já utilizado por outro usuário!'))
        return

    user = users.pop(active_username)
    users[new_username] = user
    active_username = new_username
    print(red('Nome de usuário alterado!'))


def change_password():
    '''¿?'''
    new_password = input('Defina a nova senha.\n  ~> ')
    users[active_username]['password'] = new_password
    print(red('Senha alterada!'))


def edit_profile_attribute():
    '''¿?'''
    key = input('Insira a chave do atributo.\n  ~> ')
    value = input('Defina o valor do atributo. ' +
                  red(" Obs.: '' para remover.") + '\n  ~> ')
    if value != '':
        users[active_username]['attributes'].update({key: value})
    else:
        try:
            users[active_username]['attributes'].pop(key)
            print(red('Atributo removido!'))
        except KeyError:
            print(red('Atributo inexistente!'))


def edit_user():
    '''2| Editar perfil do usuário'''
    edit_user_menu.run()


def show_profile():
    '''Mostrar perfil'''
    width = 30
    user = users[active_username]
    print(f'╔{"":═^{width}}╗',
          f'║{"Perfil de #" + active_username:^{width}}║',
          f'╠{"": ^{width}}╣', sep='\n')

    for key, value in user['attributes'].items():
        print(f'║{f" {key}: {value} ":<{width}}║')
    print(f'╚{"":═^{width}}╝')


def show_carpool(carpool_key):
    '''¿?'''
    width = 30
    carpool = carpools[carpool_key]

    print(f'╓{"":─^{width}}╖',
          f'║{"Carona #" + carpool_key:^{width}}║',
          f'╟{"":─^{width}}╢', sep='\n')

    for key, value in carpool.items():
        print(f'║{f" {key}: {value} ":<{width}}║')
    print(f'╙{"":─^{width}}╜')


def show_carpools(keys):
    '''¿?'''
    total = len(keys)

    for key in keys:
        show_carpool(key)

    if total == 0:
        print(red('Não há caronas disponíveis!'))
    elif total == 1:
        print(
            red(f'{total} carona disponível!'))
    else:
        print(
            red(f'{total} caronas disponíveis!'))


def create_ride():
    '''6| Oferecer carona'''
    ride_date = input('Quando será a viagem?\n  ~> ')
    origin = input('Qual o local de partida?\n  ~> ')
    destination = input('Qual o local de destino?\n  ~> ')

    sel = input(
        'Deseja \'o\' ofertar ou \'p\' pedir esta carona?\n  ~> ').lower()
    if sel == 'o':
        driver_user = active_username
        seats_available = input('Quantas vagas disponíveis?\n  ~> ')
        passengers = []
        status = 'offered'
        role = 'driver'
    elif sel == 'p':
        driver_user = None
        seats_available = '-1'
        passengers = [active_username]
        status = 'demanded'
        role = 'passenger'
    else:
        print(
            red('Opção inválida!'))
        return

    carpool = {
        'ride_date': ride_date,
        'origin': origin,
        'destination': destination,
        'driver_user': driver_user,
        'seats_available': seats_available,
        'passengers': passengers,
        'status': status
    }

    if input('Digite \'ok\' para confirmar a carona ' + status + '*.\n  ~> ').lower() == 'ok':
        key = str(id(carpool))
        carpools[key] = carpool
        add_history(active_username, key, role)
        print(
            red('Carona ofertada com sucesso!'))
    else:
        print(
            red('Carona não ofertada!'))


def add_history(username, carpool_key, role):
    '''¿?'''
    print('fail')
    users[username]['history'].update({carpool_key: role})


def hitch_a_ride(username, carpool_key, driver = False):
    '''¿?'''
    print(username, carpool_key, driver)



def find_ride():
    '''7| Procurar carona'''
    match input(
        'Vizualizar caronas ofertadas ou solicitas? ' + red('[o/s]') + '\n  ~> ').lower():
        case 'o':
            status = 'offered'
        case 's':
            status = 'demanded'
        case _:
            print(red('Opção inválida!'))
            return

    keys = carpools_by_status(status)

    show_carpools(keys)

    key = input('Digite o imenso identificador da carona para pegá-la.' +
                red(' Obs.: ≠ para sair.') + '\n  ~> ')

    key = re.sub(r'[\D]+', '', key)

    if key in keys:
        hitch_a_ride(active_username, key, )


def suggest_ride():
    '''8| Sugerir carona'''
    ride_date = input('Quando será a viagem?\n  ~> ')
    origin = input('Qual o local de partida?\n  ~> ')
    destination = input('Qual o local de destino?\n  ~> ')
    driver_user = input('Qual o ID do usuário sugeridor?\n  ~> ')
    seats_available = input('Quantas vagas requisitadas?\n  ~> ')

    # criar classe, posteriormente
    carpool = {
        'ride_date': ride_date,
        'origin': origin,
        'destination': destination,
        'driver_user': driver_user,
        'seats_available': seats_available}

    suggested_carpools.append(carpool)
    print(
        red('Carona sugerida com sucesso!'))


def past_rides():
    '''9| Histórico de caronas'''
    # driver_user = input('Qual o ID do usuário a ter o histórico pesquisado?\n  ~> ')
    # pesquisar usuário por id
    # mostrar histórico de caronas [tomadas e ofertadas]

    print('past_rides')


def rate_profile():
    '''10| Avaliar perfil'''

    driver_user = input('Qual o ID do usuário a ser avaliado?\n  ~> ')
    profile_rating_score = input(
        'Qual sua nota, de 0 a 5, para o usuário <?>?\n  ~> ')

    print(
        red('Perfil avaliado com sucesso!'))


def contribute():
    '''11| Valor extra'''

    driver_user = input('Qual o ID do destinatário da contribuição?\n  ~> ')
    profile_rating_score = input(
        'Qual o valor da contribuição, em BRL?\n  ~> ')

    print(
        red('Contribuição destinada a <?> com sucesso!'))


def sign_up():
    '''¿?'''
    global active_username

    username = input('Defina um nome de usuário*.\n  ~> ')
    if users.get(username):
        print(red('Usuário já cadastrado!'))
        return

    active_username = create_user(username)
    access()


def access():
    '''¿?'''
    print(red(f'Olá, {active_username}!'))
    user_menu.run()


def sign_in():
    '''¿?'''
    global active_username
    username = input('Nome de usuário.\n  ~> ')
    password = input('Senha de acesso.\n  ~> ')

    try:
        if password == users[username]['password']:
            active_username = username
            access()
        else:
            print(red('Senha inválida!'))
    except KeyError:
        print(red('Usuário não cadastrado!'))


def debug():
    '''¿?'''
    debug_menu.run()


def list_all_users():
    '''¿?'''
    for key, value in users.items():
        print(key, value)
    print(red(f'{len(users)}'))


def list_all_carpools():
    '''¿?'''
    for key, value in carpools.items():
        print(key, value)
    print(red(f'{len(carpools)}'))


def carpools_by_status(status):
    '''filtra burramente as caronas pelo status'''
    keys = set(())
    for key, carpool in carpools.items():
        if carpool['status'] == status:
            keys.add(key)
    return keys


def write_dict_users():
    '''¿?'''
    with open('users.json', 'w', encoding="utf-8") as json_file:
        json.dump(users, json_file, indent=4)


def read_dict_users():
    '''¿?'''
    global users
    with open('users.json',  encoding="utf-8") as json_file:
        users = json.load(json_file)


def write_dict_carpools():
    '''¿?'''
    with open('carpools.json', 'w', encoding="utf-8") as json_file:
        json.dump(carpools, json_file, indent=4)


def read_dict_carpools():
    '''¿?'''
    global carpools
    with open('carpools.json',  encoding="utf-8") as json_file:
        carpools = json.load(json_file)


# ###############################################################
# import gmr82 as gmr


active_username = ''
users = {}
carpools = {}
suggested_carpools = {}


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
                      'write dict users': write_dict_users,
                      'read dict users': read_dict_users,
                      'list all carpools': list_all_carpools,
                      'write dict carpools': write_dict_carpools,
                      'read dict carpools': read_dict_carpools,
                      '↩': 'see you soon…'
                  })

user_menu = Menu('user_menu',
                 {
                     'Ver/Editar meu perfil': edit_user,
                     'Adicionar carona*': create_ride,
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
                          'Retornar': 'Retornando…'
                      })


if __name__ == '__main__':

    if True:
        try:
            read_dict_users()
            print(red('Carregando usuários…'))
            read_dict_carpools()
            print(red('Carregando caronas…'))
        except FileNotFoundError:
            pass

    sign_menu.run()

    if True:
        try:
            write_dict_users()
            print(red('Salvando usuários…'))
            write_dict_carpools()
            print(red('Salvando caronas…'))
        except FileNotFoundError:
            pass

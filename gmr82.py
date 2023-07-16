''' alguns testes '''
# import datetime


class Menu:
    '''rascunho de menu'''

    def __init__(self, header='menu', options=None, start=1):
        self.header = header
        self.options = options
        self.start = start

    def run(self):
        '''roda menu: mostra opcões e chama funcões, em loop'''

        if self.options is None:
            longest_string_len = len(self.header)
        else:
            options = list(self.options.keys())
            options.append('Retornar/Sair')
            longest_string_len = len(max(options, key=len))
            if len(self.header) > longest_string_len:
                longest_string_len = self.header
            longest_string_len += 5

        while True:
            print(f'╔{"":═^{longest_string_len}}╗',
                  f'║{self.header: ^{longest_string_len}}║',
                  f'╠{"":═^{longest_string_len}}╣', sep='\n')

            if self.options is None:
                print(f'║{"∅":^{longest_string_len}}║')
                print(f'╚{"":═^{longest_string_len}}╝')
                break
            else:
                for i, option in enumerate(options, start=self.start):
                    print(f'║{f" {i: 2} {option} ":<{longest_string_len}}║')

                print(f'╚{"":═^{longest_string_len}}╝')

            sel = input('  ~> ')

            if sel.isdigit():
                sel = int(sel)

                # Encerra o loop
                if sel == self.start + len(options)-1:
                    print(
                        red(f'{"Retornando/Saindo…": >{longest_string_len}}'))
                    break

                # Chama uma função do menu
                if self.start <= sel < self.start + len(options):
                    list(self.options.items())[sel-self.start][1]()
                    continue

            print(
                red(f'{"Seleção inválida!": >{longest_string_len}}'))


def red(string):
    '''colore a string'''
    return '\033[31m' + string + '\033[0;0m'


offered_carpools = []
suggested_carpools = []


def offer_ride():
    '''6| Oferecer carona'''
    ride_date = input('Quando será a viagem?\n  ~> ')
    origin = input('Qual o local de partida?\n  ~> ')
    destination = input('Qual o local de destino?\n  ~> ')
    driver_user = input('Qual o ID do usuário ofertante?\n  ~> ')
    seats_available = input('Quantas vagas disponíveis?\n  ~> ')

    # criar classe posteriormente
    carpool = {
        'ride_date': ride_date,
        'origin': origin,
        'destination': destination,
        'driver_user': driver_user,
        'seats_available': seats_available}

    offered_carpools.append(carpool)
    print(
        red('Carona ofertada com sucesso!'))


def find_ride():
    '''7| Procurar carona'''
    total_rides = len(offered_carpools)

    for ride in offered_carpools:
        print(ride)

    if total_rides == 0:
        print(red('Não há caronas disponíveis!'))
    elif total_rides == 1:
        print(
            red(f'{total_rides} carona disponível!'))
    else:
        print(
            red(f'{total_rides} caronas disponíveis!'))


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


# ###############################################################
# import gmr82 as gmr


if __name__ == '__main__':

    initial_menu = Menu('initial_menu',
                        {
                            'Oferecer carona': offer_ride,
                            'Procurar carona': find_ride,
                            'Sugerir carona': suggest_ride,
                            'Histórico de caronas': past_rides,
                            'Avaliar perfil': rate_profile,
                            'Valor extra': contribute
                        }, 1)  # 6)

    initial_menu.run()

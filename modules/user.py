'''módulo de usuário'''

from modules.profile import Profile


class User:
    '''rascunho da classe usuário'''

    def __init__(self, username, password=None):
        self.username: str = username
        self.password = password
        self.profile = Profile()
        self.rides_history = {}


    @staticmethod
    def list_users_in(users_dictionary):
        '''¿?'''
        for key, value in users_dictionary.items():
            print(key, value.tuple_attributes())

    def is_in(self, users):
        '''¿?'''
        return self.username in users


    def change_username(self, username):
        '''¿?'''
        self.username = username

    def change_password(self, password):
        '''¿?'''
        self.password = password

    def show_profile(self):
        '''¿?'''
        width = 30

        print(f'╔{"":═^{width}}╗',
              f'║{"Perfil de #" + self.username:^{width}}║',
              f'╠{"": ^{width}}╣', sep='\n')

        for key, value in self.profile.get_attributes():
            print(f'║{f" {key}: {value} ":<{width}}║')
        print(f'╚{"":═^{width}}╝')

    def tuple_attributes(self):
        '''¿?'''
        return self.username, self.password, self.profile.attributes, self.rides_history

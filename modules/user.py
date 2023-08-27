'''módulo de usuário'''

from modules.profile import Profile


class User:
    '''rascunho da classe usuário'''

    def __init__(self, username: str, password: str | None = None) -> None:
        self._username: str = username
        self._password: str | None = password # verificar
        self.profile: Profile = Profile()
        self.rides_history: dict = {}

    def draft(self, username: str, name: str, password: str | None = None) -> None:
        '''adapatar polimorfismo'''
        # self.__init__(username, name, password)
        raise NotImplementedError

    def __repr__(self) -> str:
        string = f'User(username={self.username}, '
        string += f'password={self.password}, '
        string += f'profile={self.profile}, '
        string += f'rides_history={self.rides_history})'
        return string

    @property
    def username(self) -> str:
        '''nome de usuário'''
        return self._username
    
    @property
    def password(self) -> str|None:
        '''senha'''
        return self._password

    @staticmethod
    def list_users_in(users_dictionary: dict) -> None:
        '''imprime usuários da lista'''
        for key, value in users_dictionary.items():
            print(key, value)

    def is_in(self, users: dict) -> bool:
        '''verifica se a instancia pertence ao dicionário'''
        return self.username in users

    def change_username(self, username: str) -> None:
        '''altera o username'''
        self._username = username

    def change_password(self, password: str) -> None:
        '''altera a senha'''
        self._password = password

    def show_profile(self) -> None:
        '''mostrar porcamente o perfil'''
        width = 30

        print(f'╔{"":═^{width}}╗',
              f'║{"Perfil de #" + self.username:^{width}}║',
              f'╠{"": ^{width}}╣', sep='\n')

        for key, value in self.profile.attributes.items():
            print(f'║{f" {key}: {value} ":<{width}}║')
        print(f'╚{"":═^{width}}╝')

    def clear_rides_history(self):
        self.rides_history.clear()
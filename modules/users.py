"""módulo de usuário"""

from modules.profile import Profile
from modules.interfaces import DraftInterface
from modules.menu import Menu
from modules.carpool import Carpool, carpools


class User(DraftInterface):
    """rascunho de usuário"""

    def __init__(self, username: str, password: str | None = None) -> None:
        self._username: str = username
        self._password: str | None # criar classe p/ senha
        self.change_password(password)

    def __repr__(self) -> str:
        """
        retorna uma representação printável do objeto
        """
        # raise NotImplementedError
        string = str()
        string += f"User(username={self.username}, "
        string += f"password={self.password}, "
        return string
    
    @property
    def username(self) -> str:
        return self._username

    @property
    def password(self) -> str | None:
        return self._password

    def is_in(self, users: list | dict) -> bool:
        return self.username in users

    @staticmethod
    def print_from(users: list | dict) -> None:

        if type(users) is list:
            for user in users:
                print(user)
        elif type(users) is dict:
            for user in users.values():
                print(user)

    def change_username(self, username: str) -> None:
        self._username = username

    def change_password(self, password: str | None = None) -> None:
        password = None if password == '' else password
        self._password = password

    def password_is(self, input: str | None = None) -> bool:
        input = None if input == '' else input
        return input == self.password
    

    def add_carpool(self, *args) -> None:
        """
        adicionar carona
        """
        if not args[0] is dict[str, Carpool]:
            raise NotImplementedError('coleção não passada')
        _carpools: dict[str, Carpool] = args[0]

        print(_carpools)
        print(carpools)    

    def find_carpool(self):
        """
        encontrar carona
        """
        raise NotImplementedError



    def set_user_menu(self) -> tuple[str, list, str]:
        """
        configurar menu de usuário
        """
        title = "Menu: Usuário"
        invalid_selection_text = "Seleção inválida!"

        options = list() # ¿mudar p/ tupla?
        options.append(("Adicionar carona", self.add_carpool, True, (carpools)))
        options.append(("Procurar carona", self.find_carpool, True))
        # options.append(('Sugerir carona', suggest_ride, None))
        # options.append(('Histórico de caronas', past_rides, None))
        # options.append(('Avaliar perfil', rate_profile, None))
        # options.append(('Valor extra', contribute, None))
        # options.append(("Perfil", profile, True))
        # options.append(("Conta", account, True))
        options.append(("Sair", "Saindo…", None))

        return title, options, invalid_selection_text
            


class Admin(User):
    """administrador"""

    def __init__(self, username: str, password: str | None = None) -> None:
        super().__init__(username, password)

    def __repr__(self) -> str:
        return super().__repr__()


class Regular(User):
    """regular"""
    
    def __init__(self, username: str, password: str | None = None) -> None:
        super().__init__(username, password)
        self.profile: Profile = Profile(username)
        self.rides_history: dict = dict()



    def __repr__(self) -> str:
        string = super().__repr__()
        string += f"profile={self.profile}, "
        string += f"rides_history={self.rides_history})"
        return string

    def clear_rides_history(self):
        """
        limpar histórico de corridas
        """

        self.rides_history.clear()


# ############################################################### variáveis globais
users: dict[str, Regular] = {}
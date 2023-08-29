"""módulo de usuário"""

from modules.profile import Profile
from modules.interfaces import DraftInterface


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

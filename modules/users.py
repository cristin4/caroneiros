"""módulo de usuário"""

from modules.profile import Profile
from modules.interfaces import DraftInterface, abstractmethod
from modules.menu import Menu, dye
from modules.carpools import Carpool, carpools
from getpass import getpass


class User(DraftInterface):
    """rascunho de usuário"""

    def __init__(self, username: str, password: str | None = None) -> None:
        self._username: str = username
        self._password: str | None  # criar classe p/ senha
        self.change_password(password)

        self._user_menu: Menu = self.set_user_menu()
        self._account_menu: Menu = self.set_account_menu()

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

    @property
    def user_menu(self) -> Menu:
        return self._user_menu

    @property
    def account_menu(self) -> Menu:
        return self._account_menu

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
        password = None if password == "" else password
        self._password = password

    def password_is(self, input: str | None = None) -> bool:
        input = None if input == "" else input
        return input == self.password

    @abstractmethod
    def set_user_menu(self) -> Menu:
        """
        configurar menu de usuário
        """
        title = "Menu: Usuário"
        invalid_selection_text = "Seleção inválida!"

        options = list()  # ¿mudar p/ tupla?
        # options.append(("Adicionar carona", self.add_carpool, carpools))
        # options.append(("Procurar carona", self.find_carpool, carpools))
        # options.append(('Sugerir carona', suggest_ride, None))
        # options.append(('Histórico de caronas', past_rides, None))
        # options.append(('Avaliar perfil', rate_profile, None))
        # options.append(('Valor extra', contribute, None))
        options.append(("Conta", self.access_account_menu, None))
        # options.append(("Sair", "Saindo…", None))

        return Menu(title=title, options=options, invalid_selection_text=invalid_selection_text)

    def access_user_menu(self) -> None:
        return self.user_menu.run_in_loop()

    @abstractmethod
    def set_account_menu(self) -> Menu:
        """
        configurar menu de conta
        """
        title = "Menu: Conta"
        invalid_selection_text = "Seleção inválida!"

        options = list()  # ¿mudar p/ tupla?
        options.append(("Alterar username", self.access_change_username, None))
        options.append(("Alterar senha", self.access_change_password, None))
        # options.append(("Limpar histórico", clear_history, None))
        # options.append(("Desinscrever-se*", unsign, None))
        # options.append(("Retornar", "Retornando…", None))

        return Menu(
            title=title, options=options, invalid_selection_text=invalid_selection_text
        )

    def access_account_menu(self, *args) -> None:
        return self.account_menu.run_in_loop()

    def access_change_username(self, *args) -> bool | None:
        new_username: str = input("Defina o novo nome de usuário*.\n  ~> ")

        if new_username == self.username:
            print(dye("Nome de usuário mantido!", "yellow"))
            return

        if users.get(new_username):
            print(dye("Nome já utilizado por outro usuário!", "red"))
            return True

        if Menu.confirm("Tem certeza disso?"):
            users.pop(self.username)
            self.change_username(new_username)
            users[self.username] = self
            print(dye("Nome de usuário alterado com sucesso!", "green"))
        else:
            print(dye("Nome de usuário não alterado!", "red"))
        return

    def access_change_password(self, *args) -> bool | None:
        new_password: str = getpass("Defina a nova senha.\n  ~> ")

        if Menu.confirm("Tem certeza disso?"):
            self.change_password(new_password)
            print(dye("Senha alterada com sucesso!", "green"))
        else:
            print(dye("Senha não alterada!", "red"))
        return

    @abstractmethod
    def add_carpool(self, *args) -> bool:
        if not type(args[0]) is dict:
            raise NotImplementedError("coleção não passada")
        return True

    @abstractmethod
    def find_carpool(self) -> bool:
        raise NotImplementedError



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

    def set_user_menu(self) -> Menu:
        menu = super().set_user_menu()
        menu.options.append(("*profile*", self.profile.access_profile_menu, None)) # dudu
        # print(self.profile)
        menu.options.append(("Sair", "Saindo…"))
        menu.update_longest_string_len()
        return menu

    def set_account_menu(self) -> Menu:
        menu = super().set_account_menu()
        # menu.options.append(("*print(self)*", self.profile.access_profile_menu, None))
        menu.options.append(("Retornar", "Retornando…"))
        return menu

    def add_carpool(self, *args) -> bool:
        """if not type(args[0]) is dict:
        raise NotImplementedError('coleção não passada')"""

        origin = input("Qual o local de partida?\n  ~> ")
        destination = input("Qual o local de destino?\n  ~> ")

        match input(
            "Deseja ofertar ou demandar esta carona? " + dye("[o/d]", "red") + "\n  ~> "
        ).lower():
            case "o":
                driver_username = self.username
                seats_provided = int(
                    input("Quantos assentos deseja disponibilizar?\n  ~> ")
                )
                status = "offered"
                role = "driver"
                passenger_username = None
            case "d":
                driver_username = None
                seats_provided = None
                status = "demanded"
                role = "passenger"
                passenger_username = self.username
            case _:
                print(dye("Opção inválida!", "red"))
                return True

        carpool = Carpool(destination, origin, driver_username, status)
        carpool.seats_provided = seats_provided  # tratar int
        carpool.add_passenger(passenger_username)

        carpool.show_me()
        if Menu.confirm("Confirmar a adição desta carona?"):
            identifier = carpool.identifier
            carpools[identifier] = carpool
            self.rides_history.update({identifier: carpool})
            print(dye("Carona " + status + "* com sucesso!", "red"))
        else:
            print(dye("Carona não " + status + "*!", "red"))

        return True

    def find_carpool(self) -> bool:
        raise NotImplementedError


    def clear_rides_history(self):
        """
        limpar histórico de corridas
        """
        raise NotImplementedError
        self.rides_history.clear()



class Admin(User):
    """administrador"""

    def __init__(self, username: str, password: str | None = None) -> None:
        super().__init__(username, password)

    def __repr__(self) -> str:
        return super().__repr__()

    def set_user_menu(self) -> Menu:
        menu = super().set_user_menu()
        # menu.options.append(("DEBUG", None, None))
        menu.options.append(("Sair", "Saindo…"))
        return menu



# ############################################################### variáveis globais
users: dict[str, User | Regular | Admin] = {}

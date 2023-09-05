""" módulo de usuário """

from getpass import getpass
from modules.interfaces import DraftInterface, abstractmethod
from modules.carpools import Carpool, carpools, Any
from modules.profile import Profile
from modules.menu import Menu, dye

# ######################################WWWWWWWWWWWW######################### variáveis globais
users: dict[str, Any] = {} # | None = None # dict[str, User | Regular | Admin]

class User(DraftInterface):
    """ rascunho da classe usuário """
    # _users: dict[str, Any] = {}

    def __init__(self, username: str, password: str | None = None) -> None:
        self._username: str = username
        self._password: str | None  # criar classe p/ senha
        self.change_password(password)
    
    @property
    def username(self) -> str:
        return self._username

    @property
    def password(self) -> str | None:
        return self._password

    def is_in(self, users: list | dict) -> bool:
        return self.username in users

    @staticmethod
    def print_from(users: list[Any] | dict[str, Any]) -> None:
        if type(users) is list:
            for user in users:
                print(user)
        elif type(users) is dict:
            for key, user in users.items():
                print(key, user)

    def change_username(self, username: str) -> None:
        self._username = username

    def change_password(self, password: str | None = None) -> None:
        password = None if password == "" else password
        self._password = password

    def password_is(self, input: str | None = None) -> bool:
        input = None if input == "" else input
        return input == self.password
    
    def set_user_menu(self) -> Menu:
        """ configurar menu de usuário """
        raise NotImplementedError
    
    @abstractmethod
    def access_user_menu(self, *args) -> bool | None:
        raise NotImplementedError
        
    @abstractmethod
    def set_account_menu(self) -> Menu:
        raise NotImplementedError
    
    @abstractmethod
    def access_account_menu(self, *args) -> bool | None:
        raise NotImplementedError
    
    def access_change_password(self, *args) -> bool | None:
        new_password: str = getpass("Defina a nova senha.\n  ~> ")

        if Menu.confirm("Tem certeza disso?"):
            self.change_password(new_password)
            print(dye("Senha alterada com sucesso!", "green"))
        else:
            print(dye("Senha não alterada!", "red"))
        return



class Regular(User):

    def __init__(self, username: str, password: str | None = None) -> None:
        super().__init__(username, password)
        self._profile: Profile = Profile(username)
        self.rides_history: dict = dict()
        
        self._user_menu: Menu = self.set_user_menu()
        self._account_menu: Menu = self.set_account_menu()

    def __repr__(self) -> str:
        """ retorna uma representação printável do objeto """
        string = str()
        string += f"Regular(username={self.username}, "
        string += f"password={self.password}, "
        string += f"profile={self._profile}, "
        string += f"rides_history={self.rides_history})"
        return string
    
    @property
    def profile(self) -> Profile:
        return self._profile
    
    @property
    def user_menu(self) -> Menu:
        return self._user_menu
    
    @property
    def account_menu(self) -> Menu:
        return self._account_menu

    def set_user_menu(self) -> Menu:
        title = "Menu: Usuário"
        invalid_selection_text = "Seleção inválida!"

        options = list()  # ¿mudar p/ tupla?
        # options.append(("Adicionar carona", self.add_carpool, carpools))
        # options.append(("Procurar carona", self.find_carpool, carpools))
        # options.append(('Sugerir carona', suggest_ride, None))
        # options.append(('Histórico de caronas', past_rides, None))
        # options.append(('Avaliar perfil', rate_profile, None))
        # options.append(('Valor extra', contribute, None))
        options.append(("Perfil", self.profile.access_profile_menu, None))
        options.append(("Conta", self.access_account_menu, None))
        options.append(("Sair", "Saindo…"))
        return Menu(title=title, options=options, invalid_selection_text=invalid_selection_text)
    
    def access_user_menu(self) -> bool | None:
        return self.user_menu.run_in_loop()    

    def access_change_username(self, *args) -> bool | None:
        # users: dict[str, Any] = args[0]
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
            self.profile.update_attribute('username', new_username)
            users[self.username] = self
            print(dye("Nome de usuário alterado com sucesso!", "green"))
        else:
            print(dye("Nome de usuário não alterado!", "red"))

        return

    def set_account_menu(self) -> Menu:
        """
        configurar menu de conta
        """
        title = "Menu: Conta"
        invalid_selection_text = "Seleção inválida!"

        options = list()  # ¿mudar p/ tupla?
        options.append(("Alterar username", self.access_change_username, users))
        options.append(("Alterar senha", self.access_change_password, None))
        options.append(("?", print, self))
        options.append(("Sair", "Saindo…"))

        return Menu(title=title, options=options, invalid_selection_text=invalid_selection_text)

    def access_account_menu(self, *args) -> bool | None:
        return self.account_menu.run_in_loop()

    def add_carpool(self, *args) -> bool:
        raise NotImplementedError
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

        carpool.view()
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
    


class Admin(User):

    def __init__(self, username: str, password: str | None = None) -> None:
        super().__init__(username, password)
        self._user_menu: Menu = self.set_user_menu()
        self._account_menu: Menu = self.set_account_menu()
        self._debug_menu: Menu= self.set_debug_menu()

    def __repr__(self) -> str:
        """ retorna uma representação printável do objeto """
        string = str()
        string += f"Admin(username={self.username}, "
        string += f"password={self.password})"
        return string

    @property
    def user_menu(self) -> Menu:
        return self._user_menu

    @property
    def account_menu(self) -> Menu:
        return self._account_menu
    
    @property
    def debug_menu(self) -> Menu:
        return self._debug_menu

    def set_user_menu(self) -> Menu:
        title = "Menu: Usuário*"
        invalid_selection_text = "Seleção inválida!"

        options = list()  # ¿mudar p/ tupla?
        options.append(("DEBUG", self.access_debug_menu, None))
        options.append(("Conta", self.access_account_menu, None))
        options.append(("Sair", "Saindo…"))
        return Menu(title=title, options=options, invalid_selection_text=invalid_selection_text)

    def access_user_menu(self, *args) -> bool | None:
        return self.user_menu.run_in_loop()
    
    def set_debug_menu(self) -> Menu:
        title = "Menu: DEBUG"
        invalid_selection_text = "Seleção inválida!"

        options = list()  # ¿mudar p/ tupla?
        options.append(("Remover todas as caronas", print, None))
        options.append(("Remover todas os usuários", print, None))
        options.append(("Sair", "Saindo…"))
        return Menu(title=title, options=options, invalid_selection_text=invalid_selection_text)

    def access_debug_menu(self, *args) -> bool | None:
        return self.debug_menu.run_in_loop()
    
    def set_account_menu(self) -> Menu:
        title = "Menu: Conta"
        invalid_selection_text = "Seleção inválida!"

        options = list()  # ¿mudar p/ tupla?
        options.append(("Alterar senha", self.access_change_password, None))
        options.append(("Retornar", "Retornando…"))

        return Menu(title=title, options=options, invalid_selection_text=invalid_selection_text)

    def access_account_menu(self, *args) -> bool | None:
        return self.account_menu.run_in_loop()
    

    @staticmethod
    def clear_rides_history(user: Regular) -> None:
        """
        limpar histórico de corridas
        """
        user.rides_history.clear()
        print(dye(f"Histórico de caronas de {user.username} foi removido!", "red"))
        raise NotImplementedError
    
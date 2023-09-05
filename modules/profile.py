""" módulo de perfil """

from modules.menu import Menu, dye

class Profile:
    """rascunho da classe perfil"""

    def __init__(self, username: str, attributes: dict[str, str] | None = None) -> None:
        self._attributes: dict[str, str] = dict() if attributes is None else attributes
        self.attributes.update({'username': username}) # **kwargs

        self._profile_menu: Menu = self.set_profile_menu()


    def __repr__(self) -> str:
        return f"Profile(attributes={self.attributes})"

    @property
    def attributes(self) -> dict[str, str]:
        return self._attributes

    @property
    def profile_menu(self) -> Menu:
        return self._profile_menu
    
    def set_profile_menu(self) -> Menu:
        """
        configurar menu de perfil
        """
        title = "Menu: Perfil"
        invalid_selection_text = "Seleção inválida!"

        options = list()  # ¿mudar p/ tupla?
        options.append(("Mostrar", self.view, None))
        options.append(("Atualizar atributo", self.access_update_attribute, None))
        options.append(("Retornar", "Retornando…", None))

        return Menu(title=title, options=options, invalid_selection_text=invalid_selection_text)
    
    def access_profile_menu(self, *args) -> bool | None:
        return self.profile_menu.run_in_loop()

    def update_attribute(self, key: str, value: str | None) -> str:
        """
        atualizar atributo
        """

        if value is None: # tenta remover
            try:
                self.attributes.pop(key)
            except KeyError:
                msg = "não adicionado anteriormente"
            msg = "removido"
        else:
            self.attributes.update({key: value})
            msg = "adicionado/editado"
            
        return msg

    def access_update_attribute(self, *args) -> bool:
        key = input("Insira a chave do atributo.\n  ~> ")
        if key == 'username':
            print(dye("Altere o username em Conta!", 'red'))
            return False
        
        value = input(
            "Defina o valor do atributo. "
            + dye(" Obs.: '' para remover.", "red")
            + "\n  ~> "
        )

        if value == "":
            value = None

        msg = self.update_attribute(key, value)
        print(dye("Atributo " + msg + "!", 'red'))
        return True
        
    def view(self, *args) -> bool:
        """
        visualizar, porcamente, o perfil
        """
        width = 52 # valor arbitrário
        username = self.attributes.get('username')
        print(
            f'╔{"":═^{width}}╗',
            f'║{f"Perfil de #{username}":^{width}}║',
            f'╠{"": ^{width}}╣',
            sep="\n",
        )

        for key, value in self.attributes.items():
            print(f'║{f" {key}: {value} ":<{width}}║')
        print(f'╚{"":═^{width}}╝')

        return True
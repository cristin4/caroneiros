"""módulo de perfil"""


class Profile:
    """rascunho da classe perfil"""

    def __init__(self, username: str, attributes: dict[str, str] | None = None) -> None:
        self._attributes: dict[str, str] = dict() if attributes is None else attributes
        self.attributes.update({'username': username})


    def __repr__(self) -> str:
        return f"Profile(attributes={self.attributes})"

    @property
    def attributes(self) -> dict[str, str]:
        return self._attributes
    
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

    def view(self) -> None:
        """
        visualizar, porcamente, o perfil
        """
        width = 30 # valor arbitrário
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
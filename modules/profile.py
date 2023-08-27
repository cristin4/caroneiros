'''módulo de perfil'''


class Profile:
    '''rascunho da classe perfil''' 

    def __init__(self, attributes: dict | None = None) -> None:
        self.attributes: dict = {} if attributes is None else attributes

    def __repr__(self) -> str:
        return f'Profile(attributes={self.attributes})'

    def update_attribute(self, key, value) -> str:
        '''atualizar atributo'''

        # tenta remover
        if value is None:
            try:
                self.attributes.pop(key)
            except KeyError:
                return 'não adicionado anteriormente'

            return 'removido'

        self.attributes.update({key: value})
        return 'adicionado/editado'

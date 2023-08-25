'''módulo de perfil'''


class Profile:
    '''rascunho da classe perfil'''

    def __init__(self):
        self.attributes: dict = {}

    def get_attributes(self):
        '''¿?'''
        return self.attributes.items()

    def edit_attribute(self, key, value=None):
        '''¿?'''
        if value is None:
            try:
                self.attributes.pop(key)
                return 'removido'
            except KeyError:
                return 'não adicionado anteriormente'

        self.attributes.update({key: value})
        return 'adicionado/editado'

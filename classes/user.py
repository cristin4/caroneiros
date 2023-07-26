'''usuário'''


class User:
    '''rascunho de usuário'''

    def __init__(self, name, password = None):
        self.name = name
        self.password = password
        self.attributes = None
        self.ride_history = None


'''carona'''


class Carpool:
    '''rascunho de carona'''

    def __init__(self, destination, origin, driver_username=None, seats_available=1, status='offered'):
        self.identifier = None
        self.ride_date = None # ¿data? da corrida
        self.destination = destination
        self.origin = origin
        self.driver_username = driver_username
        self.seats_available = seats_available # assentos disponíveis
        self.status = status # ofertada/demandada/fechada
        self.passengers = None # lista de ¿caroneiros?
    
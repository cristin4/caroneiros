'''módulo de carona'''


from datetime import datetime
from uuid import uuid4
from typing import Literal
from dataclasses import dataclass


@dataclass
class Ride:
    '''¿?'''
    date: datetime  # ¿data? da corrida
    origin: str
    destination: str


class Carpool:
    '''rascunho da classe carona'''

    def __init__(self, destination, origin, driver_username=None, status='?'):
        self.__identifier = str(uuid4())[0:5] # ¿?
        self.ride = Ride(date=None, destination=destination, origin=origin)
        self.driver_username: str = driver_username
        self.seats_available: int = 0  # assentos disponíveis
        self.status: Literal['demanded', 'offered', 'fulled'] = status
        self.passengers_usernames: list  # lista de ¿caroneiros?

    @staticmethod
    def list_carpools_in(carpools_dictionary):
        '''¿?'''
        for key, value in carpools_dictionary.items():
            print(key, value.tuple_attributes())

    def is_in(self, carpools):
        '''¿?'''
        return self.identifier in carpools

    @property
    def identifier(self):
        '''¿?'''
        return self.__identifier

    def show_me(self):
        '''¿?'''
        width = 30

        print(f'╓{"":─^{width}}╖',
              f'║{"Carona #" + self.identifier:^{width}}║',
              f'╟{"":─^{width}}╢', sep='\n')

        # for key, value in ('a','b'):
        print(f'║{f"?: ?":<{width}}║')
        print(f'╙{"":─^{width}}╜')

    def tuple_attributes(self):
        '''¿?'''
        return self.__dict__

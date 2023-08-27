'''módulo de carona'''


from datetime import datetime
from uuid import uuid4
from typing import Any, Literal
from dataclasses import dataclass


@dataclass
class Ride:
    '''rascunho da classe corrida'''
    date: datetime|None  # ¿data? da corrida
    origin: str
    destination: str

    def __repr__(self) -> str:
        return f'{self.origin} → {self.destination} ({self.date})'


class Carpool:
    '''rascunho da classe carona'''

    def __init__(self, destination, origin, driver_username=None, status=None):
        self._identifier: str = str(uuid4())[0:5]  # ¿?
        self.ride = Ride(date=None, destination=destination, origin=origin)
        self.status: Literal['demanded', 'offered', 'fulled'] | None = status
        self.driver_username: str|None = driver_username
        self.seats_provided: int|None = None  # assentos disponibilizados
        self._passengers_usernames: list = []

    def __repr__(self) -> str:
        string = f'Carpool(identifier={self.identifier}, '
        string += f'ride={self.ride}, '
        string += f'status={self.status}, '
        string += f'driver_username={self.driver_username}, '
        string += f'seats_available={self.seats_provided}, '
        string += f'passengers_usernames={self.passengers_usernames})'
        return string

    @property
    def identifier(self) -> str:
        '''¿?'''
        return self._identifier
    
    @staticmethod
    def list_carpools_in(carpools_dictionary: dict):
        '''imprime caronas da lista'''
        for key, value in carpools_dictionary.items():
            print(key, value)

    def is_in(self, carpools: dict) -> bool:
        '''verifica se a instancia pertence ao dicionário'''
        return self.identifier in carpools

    def show_me(self) -> None:
        '''mostrar-me'''

        """ attributes = dict(self.__dict__) # gambiarra p/ corrigir
        for key, value in attributes.items():
            print(f'{key}: {value}') """
        
        width = 60

        print(f'╓{"":─^{width}}╖',
              f'║{"Carona #" + self.identifier:^{width}}║',
              f'╟{"":─^{width}}╢',
              f'║{f"corrida: {self.ride}":<{width}}║',
              f'║{f"status: {self.status}":<{width}}║',
              f'║{f"motorista: {self.driver_username}":<{width}}║',
              f'║{f"assentos disponibilizados: {self.seats_provided}":<{width}}║',
              f'║{f"passageiros: {self.passengers_usernames}":<{width}}║',
              f'╙{"":─^{width}}╜', sep='\n')

    def driver_is(self, driver_username: str) -> bool:
        return self.driver_username == driver_username
    
    def update_status(self) -> None:
        if not self.has_vacancy():
            self.status = 'fulled'
    
    def has_driver(self) -> bool:
        return bool(self.driver_username)
    
    def add_passenger(self, passenger_username: str|None) -> None:
        if self.has_vacancy() and passenger_username:
            self._passengers_usernames.append(passenger_username)

    @property
    def passengers_usernames(self) -> list:
        return self._passengers_usernames

    def has_vacancy(self) -> bool:
        return len(self.passengers_usernames) < self.seats_provided if self.seats_provided else True
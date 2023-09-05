"""módulo de interfaces"""
from abc import ABC, abstractmethod

class DraftInterface(ABC):

    @abstractmethod
    def is_in(self) -> bool:
        """
        verificar se a instancia está na coleção
        """
        raise NotImplementedError
    
    @staticmethod
    @abstractmethod
    def print_from(parameter_list) -> None:
        """
        imprimir objetos da colecão
        """
        raise NotImplementedError
    
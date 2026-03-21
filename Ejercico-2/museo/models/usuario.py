from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, nombre, password):
        self.nombre = nombre
        self.password = password

    @abstractmethod
    def rol(self):
        pass
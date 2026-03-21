from abc import ABC, abstractmethod


class Autenticable(ABC):
    @abstractmethod
    def autenticar(self, password):
        pass
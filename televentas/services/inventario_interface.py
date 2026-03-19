from abc import ABC, abstractmethod


class InventarioInterface(ABC):

    @abstractmethod
    def obtener_producto(self, codigo: str):
        pass

    @abstractmethod
    def actualizar_stock(self, codigo: str, cantidad: int):
        pass
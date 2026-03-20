from abc import ABC, abstractmethod
from datetime import date

class Obra(ABC):
    def __init__(self, titulo, autor, periodo, valor, fecha_creacion, fecha_ingreso):
        self.titulo = titulo
        self.autor = autor
        self.periodo = periodo
        self.valor = valor
        self.fecha_creacion = fecha_creacion
        self.fecha_ingreso = fecha_ingreso
        self.en_restauracion = False
        self.restauraciones = []

    @abstractmethod
    def mostrar_detalle(self):
        pass

    def agregar_restauracion(self, restauracion):
        self.restauraciones.append(restauracion)

    def necesita_restauracion(self):
        """Cada 5 años"""
        hoy = date.today()
        return (hoy - self.fecha_ingreso).days >= 5 * 365
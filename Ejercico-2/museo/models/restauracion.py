from datetime import date


class Restauracion:
    def __init__(self, tipo):
        self.tipo = tipo
        self.fecha_inicio = date.today()
        self.fecha_fin = None

    def finalizar(self):
        self.fecha_fin = date.today()
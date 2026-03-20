from models.obra import Obra
class Cuadro(Obra):
    def __init__(self, titulo, autor, periodo, valor, fecha_creacion, fecha_ingreso, estilo, tecnica):
        super().__init__(titulo, autor, periodo, valor, fecha_creacion, fecha_ingreso)
        self.estilo = estilo
        self.tecnica = tecnica

    def mostrar_detalle(self):
        return f"Cuadro: {self.titulo}, Técnica: {self.tecnica}"
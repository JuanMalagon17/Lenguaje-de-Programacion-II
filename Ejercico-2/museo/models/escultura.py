from models.obra import Obra
class Escultura(Obra):
    def __init__(self, titulo, autor, periodo, valor, fecha_creacion, fecha_ingreso, estilo, material):
        super().__init__(titulo, autor, periodo, valor, fecha_creacion, fecha_ingreso)
        self.estilo = estilo
        self.material = material

    def mostrar_detalle(self):
        return f"Escultura: {self.titulo}, Material: {self.material}"
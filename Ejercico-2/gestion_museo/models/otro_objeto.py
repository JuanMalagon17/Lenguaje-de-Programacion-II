from models.obra import Obra

class OtroObjeto(Obra):
    def mostrar_detalle(self):
        return f"Objeto: {self.titulo}"
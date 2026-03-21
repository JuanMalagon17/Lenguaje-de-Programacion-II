from models.usuario import Usuario


class Visitante(Usuario):
    def rol(self):
        return "Visitante"

    def ver_obras(self, museo):
        return [obra.mostrar_detalle() for obra in museo.obras]
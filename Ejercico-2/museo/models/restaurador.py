from models.usuario import Usuario


class Restaurador(Usuario):
    def rol(self):
        return "Restaurador"

    def ver_restauraciones(self, obra):
        return sorted(obra.restauraciones, key=lambda r: r.fecha_inicio)
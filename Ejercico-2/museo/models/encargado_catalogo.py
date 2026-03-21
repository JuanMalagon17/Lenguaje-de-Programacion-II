from models.usuario import Usuario


class EncargadoCatalogo(Usuario):
    def rol(self):
        return "Encargado de Catálogo"
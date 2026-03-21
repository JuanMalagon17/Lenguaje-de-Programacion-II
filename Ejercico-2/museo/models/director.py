from models.usuario import Usuario


class Director(Usuario):
    def rol(self):
        return "Director"

    def consultar_valor_total(self, museo):
        return museo.valor_total()
class AutenticacionService:
    def autenticar(self, usuario, password):
        return usuario.password == password
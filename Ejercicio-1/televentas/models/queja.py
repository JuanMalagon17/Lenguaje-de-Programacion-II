class Queja:
    def __init__(self, cliente, descripcion: str):
        self.cliente = cliente
        self.descripcion = descripcion

    def enviar(self):
        print(f"Queja enviada al gerente: {self.descripcion}")
class Transportadora:

    def __init__(self, nombre: str):
        self.nombre = nombre

    def enviar_pedido(self):
        print(f"Pedido enviado por {self.nombre}")
class Logistica:

    def __init__(self, transportadoras):
        self.transportadoras = transportadoras

    def seleccionar_transportadora(self):
        return self.transportadoras[0]

    def enviar(self):
        transportadora = self.seleccionar_transportadora()
        transportadora.enviar_pedido()
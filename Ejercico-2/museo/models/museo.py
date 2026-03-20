class Museo:
    def __init__(self):
        self.obras = []
        self.museos_colaboradores = []

    def agregar_obra(self, obra):
        self.obras.append(obra)

    def valor_total(self):
        return sum(obra.valor for obra in self.obras)
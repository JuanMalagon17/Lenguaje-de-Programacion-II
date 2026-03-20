class Catalogo:

    def __init__(self, inventario):
        self.inventario = inventario

    def consultar_producto(self, codigo: str):
        return self.inventario.obtener_producto(codigo)
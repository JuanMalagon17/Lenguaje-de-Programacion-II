from services.inventario_interface import InventarioInterface

class ServicioInventario(InventarioInterface):

    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.codigo] = producto

    def obtener_producto(self, codigo: str):
        return self.productos.get(codigo)

    def actualizar_stock(self, codigo: str, cantidad: int):
        if codigo in self.productos:
            self.productos[codigo].cantidad -= cantidad
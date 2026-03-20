from typing import List, Tuple
from models.producto import Producto
from pagos.pago import Pago

class OrdenCompra:
    def __init__(self, cliente, pago: Pago):
        self.cliente = cliente
        self.pago = pago
        self.productos: List[Tuple[Producto, int]] = []
        self.confirmada = False

    def agregar_producto(self, producto: Producto, cantidad: int):
        self.productos.append((producto, cantidad))

    def calcular_total(self):
        return sum(p.precio * c for p, c in self.productos)

    def confirmar(self):
        total = self.calcular_total()
        self.pago.procesar_pago(total)
        self.confirmada = True

    def cancelar(self):
        self.confirmada = False
        print("Orden cancelada")
        
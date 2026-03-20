from models.producto import Producto
from models.cliente import Cliente
from models.orden import OrdenCompra
from pagos.pago_tarjeta import PagoTarjeta

def main():
    cliente = Cliente("Juan", "juan@mail.com")
    pago = PagoTarjeta()

    producto = Producto("001", "Laptop", 3000, 10)

    orden = OrdenCompra(cliente, pago)
    orden.agregar_producto(producto, 2)

    orden.confirmar()

if __name__ == "__main__":
    main()
    
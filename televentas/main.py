from models.producto import Producto
from models.cliente import Cliente
from models.orden import OrdenCompra
from models.queja import Queja
from pagos.pago_tarjeta import PagoTarjeta
from services.servicio_inventario import ServicioInventario
from services.catalogo import Catalogo
from utils.transportadora import Transportadora
from services.logistica import Logistica


def main():
    inventario = ServicioInventario()

    producto = Producto("001", "Laptop", 3000, 10)
    inventario.agregar_producto(producto)

    catalogo = Catalogo(inventario)
    print(catalogo.consultar_producto("001"))

    cliente = Cliente("Juan", "juan@mail.com")
    pago = PagoTarjeta()

    orden = OrdenCompra(cliente, pago)
    orden.agregar_producto(producto, 1)
    orden.confirmar()

    logistica = Logistica([Transportadora("Servientrega")])
    logistica.enviar()

    queja = Queja(cliente, "Demora en la entrega del pedido")
    queja.enviar()

if __name__ == "__main__":
    main()

from models.producto import Producto
from services.servicio_inventario import ServicioInventario

def main():
    inventario = ServicioInventario()

    producto = Producto("001", "Laptop", 3000, 10)
    inventario.agregar_producto(producto)

    print(inventario.obtener_producto("001"))

if __name__ == "__main__":
    main()
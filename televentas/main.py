from services.catalogo import Catalogo
from services.servicio_inventario import ServicioInventario
from models.producto import Producto

def main():
    inventario = ServicioInventario()
    producto = Producto("001", "Laptop", 3000, 10)

    inventario.agregar_producto(producto)

    catalogo = Catalogo(inventario)
    print(catalogo.consultar_producto("001"))

if __name__ == "__main__":
    main()
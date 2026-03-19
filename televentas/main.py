from models.producto import Producto
from models.cliente import Cliente


def main():
    cliente = Cliente("Juan", "juan@mail.com")
    print(cliente.solicitar_catalogo())


if __name__ == "__main__":
    main()
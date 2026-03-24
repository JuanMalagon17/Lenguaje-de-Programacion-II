from datetime import date

from models.cuadro import Cuadro
from models.museo import Museo
from models.visitante import Visitante
from models.director import Director
from services.gestor_restauracion import GestorRestauracion
from services.gestor_cesion import GestorCesion
from services.autenticacion import AutenticacionService


def main():
    print("=== SISTEMA DE GESTIÓN DE MUSEO ===\n")

    # 🔹 Crear museo
    museo = Museo()

    # 🔹 Crear obra
    cuadro = Cuadro(
        "Mona Lisa",
        "Da Vinci",
        "Renacimiento",
        1000000,
        date(1503, 1, 1),
        date(2010, 1, 1),
        "Retrato",
        "Óleo"
    )

    museo.agregar_obra(cuadro)

    print("Obra creada:")
    print(cuadro.mostrar_detalle())
    print()

    # 🔹 Valor total
    print("Valor total del museo:")
    print(museo.valor_total())
    print()

    # 🔹 Restauración
    gestor_restauracion = GestorRestauracion()
    gestor_restauracion.verificar_restauraciones([cuadro])

    print("Restauraciones realizadas:", len(cuadro.restauraciones))
    print()

    # 🔹 Autenticación
    auth = AutenticacionService()
    director = Director("Carlos", "123")

    acceso = auth.autenticar(director, "123")
    print("Autenticación del director:", acceso)
    print()

    # 🔹 Cesión de obra
    gestor_cesion = GestorCesion()
    gestor_cesion.ceder_obra(
        cuadro,
        "Museo del Prado",
        5000,
        date(2024, 1, 1),
        date(2024, 6, 1)
    )

    print("Obra cedida correctamente")
    print()

    # 🔹 Vista visitante
    visitante = Visitante("Juan", "000")
    print("Obras disponibles para visitante:")
    print(visitante.ver_obras(museo))
    print()

    # 🔹 Restaurador consulta historial
    from models.restaurador import Restaurador
    restaurador = Restaurador("Ana", "456")

    print("Historial de restauraciones:")
    print(restaurador.ver_restauraciones(cuadro))


if __name__ == "__main__":
    main()
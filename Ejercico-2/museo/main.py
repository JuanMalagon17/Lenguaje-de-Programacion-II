from datetime import date
from models.cuadro import Cuadro
from services.gestor_cesion import GestorCesion


def main():
    gestor = GestorCesion()

    cuadro = Cuadro(
        "Mona Lisa",
        "Da Vinci",
        "Renacimiento",
        1000000,
        date(1503, 1, 1),
        date(2020, 1, 1),
        "Retrato",
        "Óleo"
    )

    gestor.ceder_obra(
        cuadro,
        "Museo del Prado",
        5000,
        date(2024, 1, 1),
        date(2024, 6, 1)
    )

    print("Obra cedida correctamente")


if __name__ == "__main__":
    main()
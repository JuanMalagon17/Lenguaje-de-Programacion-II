from datetime import date
from models.cuadro import Cuadro

def main():
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

    print(cuadro.mostrar_detalle())


if __name__ == "__main__":
    main()
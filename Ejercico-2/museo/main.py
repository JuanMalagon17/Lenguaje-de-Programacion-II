from datetime import date
from models.cuadro import Cuadro
from models.restauracion import Restauracion


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

    restauracion = Restauracion("Limpieza")
    cuadro.agregar_restauracion(restauracion)

    print("Restauraciones:", len(cuadro.restauraciones))

if __name__ == "__main__":
    main()
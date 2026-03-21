from datetime import date
from models.cuadro import Cuadro
from services.gestor_restauracion import GestorRestauracion


def main():
    gestor = GestorRestauracion()

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

    gestor.iniciar_restauracion(cuadro, "Limpieza")

    print("En restauración:", cuadro.en_restauracion)


if __name__ == "__main__":
    main()
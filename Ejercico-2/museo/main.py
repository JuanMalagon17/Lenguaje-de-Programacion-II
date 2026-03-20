from datetime import date
from models.cuadro import Cuadro
from models.museo import Museo

def main():
    museo = Museo()

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

    museo.agregar_obra(cuadro)

    print("Valor total:", museo.valor_total())


if __name__ == "__main__":
    main()
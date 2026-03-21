from models.restauracion import Restauracion


class GestorRestauracion:
    def iniciar_restauracion(self, obra, tipo):
        restauracion = Restauracion(tipo)
        obra.en_restauracion = True
        obra.agregar_restauracion(restauracion)

    def finalizar_restauracion(self, obra):
        if obra.restauraciones:
            obra.restauraciones[-1].finalizar()
            obra.en_restauracion = False

    def verificar_restauraciones(self, obras):
        for obra in obras:
            if obra.necesita_restauracion():
                self.iniciar_restauracion(obra, "Mantenimiento automático")
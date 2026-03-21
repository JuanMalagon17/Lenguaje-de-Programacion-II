class GestorCesion:
    def ceder_obra(self, obra, museo, valor, fecha_inicio, fecha_fin):
        obra.cesion = {
            "museo": museo,
            "valor": valor,
            "inicio": fecha_inicio,
            "fin": fecha_fin
        }
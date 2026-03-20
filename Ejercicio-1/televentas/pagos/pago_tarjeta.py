from pagos.pago import Pago

class PagoTarjeta(Pago):

    def procesar_pago(self, monto: float):
        print(f"Pago de ${monto} realizado con tarjeta")
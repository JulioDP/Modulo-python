import time


class TiempoTrabajo:

    def __init__(self,horaEntrada,minutoEntrada):
        self.entradaHora = horaEntrada
        self.entradaMinuto = minutoEntrada
        self.hora = time.strftime('%H')
        self.minuto = time.strftime('%M')


    def verificarSalida(self):
        veryHora = int(self.hora) - self.entradaHora
        verMinuto = int(self.minuto) - self.entradaMinuto
        if (veryHora > 7):
            print("Hora completada favor de ir a descansar")
        else:
            print("Faltan",7 - veryHora ,"hora", verMinuto,"minuto para completar")

ob = TiempoTrabajo(9,30)
ob.verificarSalida()


class Movil:
    def __init__(self, number):
        self.number = number

    def turn_on(self):
         print(f"el teléfono móvil {self.number} está encendido")

    def turn_off(self):
         print("el teléfono móvil está apagado")

    def call(self, number):
         print(f"Llamando a {number}")


alba_movil = Movil(number=610740681)
rafa_movil = Movil(number=623575786)
rafa_movil.turn_on()
alba_movil.turn_on()
rafa_movil.call(8815909)
alba_movil.call(623574786)
alba_movil.turn_off()
rafa_movil.turn_off()

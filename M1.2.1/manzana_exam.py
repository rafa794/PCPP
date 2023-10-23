from random import uniform


class Manzana:

    manzanas_procesadas = 0
    peso_total_manzana = 0

    def __init__(self):
        if Manzana.peso_total_manzana >= 300 or Manzana.manzanas_procesadas >= 1000:
            print(f"Numero total de manzanas creadas = {Manzana.manzanas_procesadas}, "
                  f"peso total = {Manzana.peso_total_manzana} ")
            raise Exception("Limitación alcanzada")
        self.peso = uniform(1, 2)
        print(f"Peso de la manzana actual: {self.peso}, Peso total acumulado: {Manzana.peso_total_manzana + self.peso}")  # Diagnóstico
        Manzana.manzanas_procesadas += 1
        Manzana.peso_total_manzana += self.peso


manzanas_creadas = []

try:
    for _ in range(310):
        manzana = Manzana()
        manzanas_creadas.append(manzana)
except Exception as e:
    for manzana in manzanas_creadas:
        print(manzana)
    print(f"Excepción capturada: {e}")





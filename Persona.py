class Persona:
    def __init__(self, edad, altura, peso):
        self.edad = edad
        self.altura= altura
        self.peso = peso

    def __add__(self, otro):
        return self.peso + otro.peso

    def __str__(self):
        return f"{Persona} tiene {self.edad} años, mide {self.altura // 100} metro {self.altura % 100} y pesa {self.peso} kilos"

Juan = Persona(20, 180, 80)
Alba = Persona(22, 176, 60)
Maria = Persona(22, 176, Alba + Juan)

print(Maria)
print(Alba)
print(Juan)
print(dir(Juan), help(Juan))
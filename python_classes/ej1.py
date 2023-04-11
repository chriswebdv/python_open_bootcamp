class Vehiculo:
    def __init__(self, Color, Ruedas, Puertas):
        self.Color = Color
        self.Ruedas = Ruedas
        self.Puertas = Puertas


class Coche(Vehiculo):
    def __init__(self, Velocidad, Cilindrada, Color, Ruedas, Puertas):
        self.Velocidad = Velocidad
        self.Cilindrada = Cilindrada
        super().__init__(Color, Ruedas, Puertas)
        
coche1 = Coche(120, 8, 'blanco', 4, 4)

print(coche1.Color)
print(coche1.Ruedas)
print(coche1.Puertas)
print(coche1.Velocidad)
print(coche1.Cilindrada)


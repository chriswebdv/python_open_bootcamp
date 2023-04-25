#En este segundo ejercicio, tendréis que crear un 
# archivo py y dentro crearéis una clase Vehículo, 
# haréis un objeto de ella, lo guardaréis en un archivo 
# y luego lo cargamos.

import pickle

class Vehiculo:
    def __init__(self, color, marca):
        self.color = color
        self.marca = marca

v1 = Vehiculo("rojo", "audi")

with open('vehiculo.txt', 'wb') as f:
    pickle.dump(Vehiculo, f)


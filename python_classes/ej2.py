# En este segundo ejercicio, tendréis que crear un programa 
# que tenga una clase llamada Alumno que tenga como atributos 
# su nombre y su nota. Deberéis de definir los métodos 
# para inicializar sus atributos, imprimirlos y mostrar 
# un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def resultado_nota(self):
        if self.nota >= 70:
            print('Pasaste la clase! ' +self.nombre)
        
        else:
            print('No pasaste!')
        

a1 = Alumno('Rogelio', 70)
print(a1.nombre)
print(a1.nota) 
a1.resultado_nota()



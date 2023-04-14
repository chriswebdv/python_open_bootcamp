# En este segundo ejercicios tendréis que crear un script que nos 
# diga si es la hora de ir a casa. Tendréis que hacer uso 
# del modulo time. 
# Necesitaréis la fecha del sistema y poder comprobar la hora.
# En el caso de que sean más de las 7, se mostrará un mensaje y 
# en caso contrario, haréis una operación para calcular el tiempo 
# que queda de trabajo.

import time

# Obtener la fecha y hora del sistema
fecha_actual = time.localtime()
hora_actual = fecha_actual.tm_hour

# Comprobar si es hora de ir a casa (más de las 7 PM)
if hora_actual >= 19:
    print("¡Es hora de ir a casa!")
else:
    # Calcular el tiempo que queda de trabajo en horas y minutos
    hora_final = 19  # Hora de finalización del trabajo (7 PM)
    minuto_final = 0  # Minuto de finalización del trabajo
    tiempo_restante = ((hora_final - hora_actual) * 60) + (minuto_final - fecha_actual.tm_min)
    horas_restantes = tiempo_restante // 60
    minutos_restantes = tiempo_restante % 60

    print("Aún quedan {} horas y {} minutos de trabajo".format(horas_restantes, minutos_restantes))


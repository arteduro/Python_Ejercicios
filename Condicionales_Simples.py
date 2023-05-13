print("Sistema para calcular el promedio de un alumno.")

nombre = input("Para comensar, cúal es tu nombre: ")

matematicas = int(input(nombre + " ¿Cuál es tu calificación en matematicas: "))
química = int(input(nombre + " ¿Cuál es tu calificación en química: "))
bíologia = int(input(nombre + " ¿Cuál es tu calificación en bíologia: "))

promedio = (matematicas + química + bíologia) / 3

if promedio >=6:
    print(' Felicidades ' + nombre + ' "Aprobaste" con un promedio de: ',promedio)

else:
    print('Lo siento ' + nombre + ' "Reprobaste el año" ')

print("Fin")
                        

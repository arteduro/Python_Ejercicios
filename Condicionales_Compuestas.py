print("Sistema para calcular el promedio de un alumno.")

nombre = input("Para comensar, cúal es tu nombre: ")

matematicas = float(input(nombre + " ¿Cuál es tu calificación en matematicas: "))
química = float(input(nombre + " ¿Cuál es tu calificación en química: "))
bíologia = float(input(nombre + " ¿Cuál es tu calificación en bíologia: "))

promedio = (matematicas + química + bíologia) / 3

if promedio >=6:
    print(' Felicidades ' + nombre + ' "Aprobaste" con un promedio de: ', round(promedio,2))

else:
    print('Lo sientimos ' + nombre + ' "Reprobaste" el año con un promedio: ', round(promedio,2))

print("Fin")

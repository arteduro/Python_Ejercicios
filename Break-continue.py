#Ejemplo de while con break: se utiliza para detener una iteración

print("While con la sentencia break \n")
contador = 0

while contador < 10:
    contador += 1

    if contador == 5:
        break

    print("El valor actual de la sentecia es:", contador)

print("Fin del programa, la sentencia break se ha ejecutado.")


#Ejemplo de while con continue: permite detener las iteraciones y volver al princio del ciclo

print("\nWhile con la sentencia break \n")
contador = 0

while contador < 10:
    contador += 1

    if contador == 5:
        continue

    print("El valor actual de la sentecia es:", contador)





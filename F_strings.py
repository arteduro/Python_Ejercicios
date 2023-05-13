#Método fstring: son la malternativa de contatenación más eficiente
#permiten agregar expresiones dentro de una constante de tipo string

#Ejemplo 1

print(f"El resultado de 4 + 5 = {4+5}")


#Ejemplo 2

nombre = "Edgar"
estatura = 1.67
edad = 45

print(f"Hola {nombre} tienes {edad} y mides {estatura} centimetros.")


#Ejemplo 3


nombre = input("¿Cúal es tu nombre?: ")
num_uno = int(input("Introduce un número: "))
num_dos = int(input("Introduce un segundo número: "))

print(f"Hola {nombre} el resultado de {num_uno} + {num_dos} es: {num_uno +num_dos}")

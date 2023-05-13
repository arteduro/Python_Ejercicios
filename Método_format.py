#Método Format:nos permite mostrar los valores contenidos en una variable
#y utilizarlos dentro de una cadena de caracteres,
#sustutuyendo el nombre de la variable con un par de {}


#Opción 1

nombre = "Edgar"
edad = 45

print("hola {} tienes {} años.".format(nombre, edad))


# Opción 2

print("hola {nombre} tienes {edad} años.".format(nombre = "Edgar", edad = 45))



#Opción 3

nombre = "Edgar"
edad = 45

print("hola {0} tienes {1} años.".format(nombre, edad))



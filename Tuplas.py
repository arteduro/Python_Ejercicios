#Ejemplo de Tupla
thistuple = ("apple", "banana", "cherry")
print(thistuple)


#Ejemplo de Tupla con duplicado
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Longitud de una Tupla
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#Acceder a elementos de una Tupla
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Actualizar Tupla =Convierta la tupla en una lista para poder cambiarla
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#Agragar elemntos a una Tupla
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)


#Desempaquetando una tupla
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#Bucle a través de una tupla
thistuple = ("Manzana", "banano", "Piña")
for x in thistuple:
  print(x)

#Bucle a través de los números de índice
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

  
#Une dos tuplas
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#multiplicar tuplas
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

#Método Python Tuple count()=Devuelve el número de veces que aparece el valor 5 en la tupla
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)


#Método Python Tuple index()=Busque la primera aparición del valor 8 y devuelva su posición
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)



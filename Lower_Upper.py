#Métodos Islower () y lower():se utlizan para identificar si todas las letras de una cadena de caracteres,
#se encuentran en Minúscula y sino convertirlas todas en minusculas.


#Métodos Isupper Upper() y Upper():se utlizan para identificar si todas las letras de una cadena de caracteres,
#se encuentran en Mayúsculas  y sino convertirlas todas en mayúsculas.

 

string = input("introduce un string: ")

print(f"\n¿Todas las letras estan en minúsculas: {string.islower()}")
string = string.lower()
print(f"String en minúculas: {string}")

print(f"\n¿Todas las letras estan en mayúsculas: {string.upper()}")
print(f"String en mayúsculas: {string.upper()}")
print(f"string original: {string}")


#Método sort():nos permite ordenar una lista, tanto en orden ascende como descendente.
#
numeros = [5, 3, 1, 2, 4]
vocales = ["o", "u", "a", "i", "e" ]
           
# Lista numeros
print(f"\nLista de números: {numeros}")

numeros.sort()
print(f"\nLista de números: {numeros}")

numeros.sort(reverse = True)
print(f"\nLista de números: {numeros}")


# Lisla vocales

print(f"\nLista de vocales: {vocales}")

vocales.sort()
print(f"\nLista de vocales: {vocales}")


vocales.sort(reverse = True)
print(f"\nLista de números: {vocales}")

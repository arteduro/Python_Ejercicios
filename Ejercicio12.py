#Programa que dada la siguiente lista, elimina el primer y último elemento de la lista.
#posteriormente mostrará dos listas: una con los elementos que no fueron eliminados y otra con los elementos eliminados.

numeros = [1, 2, 3, 4, 5]
print(f"Lista números: {numeros}")

numeros_eliminados = []
numeros_eliminados.append(numeros.pop(0))
numeros_eliminados.append(numeros.pop())

print(f"Lista números: {numeros} \nLista números eliminados: {numeros_eliminados}")

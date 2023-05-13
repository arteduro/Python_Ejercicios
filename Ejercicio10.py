#Programa que solicita desde teclado la longitud de una lista, solicitara nuevamente desde teclado,
#cada uno de los elementos que contiene la lista, e irlos indroduciendo elemento a elemento dentro de la lista,
#finalmente muestra la lista, y a su vez, la suma de todos los elemntos que componen a la lista.

numeros = []
longitud_lista = int(input("¿Cuantos números enteros contendrá la lista?: "))

for _ in range(longitud_lista):
    numeros.append(int(input("Introduce un número entero: ")))

print(f"\nLista: {numeros} \nLa suma total de los elementos es: {sum(numeros)}")


#Programa  que genera umna matriz con valores de tipo entero desde teclado de manera automatizada, el usuario tendrá que
#especificar, através de teclado, la cantidad de filas y columnas, además deberá pedir al usuario los avlores de la matriz
# y mostrará el resultado en pantalla en forma de matriz.

rows = int(input("¿Cuántas filas tendrá la matriz?: "))
columns = int(input("¿Cuántas columnas tendrá la matriz?: "))

matrix = []

for row_position in range(rows):
    row = []
    for element in range(columns):
        row.append(int(input(f"Introduce un elemneto a la fila {row_position}: ")))
    matrix.append(row)    

for row in matrix:
    print(row)

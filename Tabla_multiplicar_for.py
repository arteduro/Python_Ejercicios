#Programa que muestra en pantalla, la tabla de multiplicar de un núnero cualquiera.

num = int(input("¿Qué tabla de multiplicar quiere ver?:"))

print(f"La tabla del {num} es:")
for i in range(11):
    print(f"{num} x {i} = {num * i}")

    

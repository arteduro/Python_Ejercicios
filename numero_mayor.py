print("**************************************************************************")
print("Programa para determinar ¿Cuál es el número más grande entre tres números.")
print("**************************************************************************\n")

num_uno = int(input("Por favor digite el primer número: "))

num_dos = int(input("Por favor digite el segundo número: "))

num_tres = int(input("Por favor digite el tercer número: "))

if num_uno > num_dos and num_uno > num_tres:
    print("El número",num_uno, "Es el más grande entre los tres Numeros.")
    
elif num_dos >  num_tres:
    print("El número",num_dos, "Es el más grande entre los tres Numeros.")
    
    
else:
    print("El número",num_tres, "Es el más grande entre los tres Numeros.")
    

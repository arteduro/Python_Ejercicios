#Conjución

print("Conjución (and)")

num_uno = int(input("escribe un número mayor a 2 y menor que 5: "))

if num_uno >2 and num_uno < 5 :
    print("El número", num_uno, "cumple con la condición.\n")
else:
    print("El número", num_uno, "No cumple con la condición.\n")
    


#Disyunción

print("Disyunción (or)")

palabra = input("para cumplir con la cindición escribe 'si' o 'yes': ")


if palabra == "si" or palabra == "yes":
    print("La condición se ha cunplido.\n")
else:
    print("La condición no se ha cumplido.\n")




#Negación

print("Negación (not)")

num_uno = int(input("Introduce un Numero igual a 5: "))

if not num_uno == 5 :
    print("\n El número es diferente de cinco y si cumple con la condición.\n")
else:
    print("\n El número igual a cinco y No cumple con la condición.\n")











    


#Año Bisiesto
print("Dígite el año:")
anio = int(input("Introduce el número: "))


if anio % 4 == 0 and anio %1==0 != 0 or anio % 400 == 0 :
    print ("Año Bisiesto")

else:
    print("Año No Bisiesto")

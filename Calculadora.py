print("Calcualdora con una sola variable. \n")

print("********************")
print("* Menú de opciones *")
print("********************")

print("1.Suma")
print("2.Resta")
print("3.Multiplicación")
print("4.División")
print("5.División entera")
print("6.Exponente")
print("7.Módulo o resto \n")


numero = int(input("Intoduce la opción deseada:"))

if numero == 1:

    print("Elegiste la Suma \n")
    numero = int(input("Introduce el primer número:"))
    numero += int(input("Introduce el segundo número:"))
    print("El resulatdo de la suma es:",numero)

elif numero == 2:

    print("Elegiste la Resta \n")
    numero = int(input("Introduce el primer número:"))
    numero -= int(input("Introduce el segundo número:"))
    print("El resulatdo de la resta es:",numero)

elif numero == 3:

    print("Elegiste la Multiplicación \n")
    numero = int(input("Introduce el primer número:"))
    numero *= int(input("Introduce el segundo número:"))
    print("El resulatdo de la multiplicación es:",numero)

elif numero == 4:

    print("Elegiste la División \n")
    numero = float(input("Introduce el primer número:"))
    numero /= float(input("Introduce el segundo número:"))
    print("El resulatdo de la división es:", round(numero,2))

elif numero == 5:

    print("Elegiste la División Entera \n")
    numero = int(input("Introduce el primer número:"))
    numero //= int(input("Introduce el segundo número:"))
    print("El resulatdo de la división entera  es:",numero)

elif numero == 6:

    print("Elegiste la Exponente \n")
    numero = int(input("Introduce el primer número:"))
    numero **= int(input("Introduce el segundo número:"))
    print("El resulatdo del exponente es:",numero)

elif numero == 7:

    print("Elegiste el Módulo \n")
    numero = int(input("Introduce el primer número:"))
    numero %= int(input("Introduce el segundo número:"))
    print("El resulatdo del módulo  o resto es:",numero)

else:
    print("Opción No válida, vuelve a intentar.")



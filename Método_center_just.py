#Método center():permite centrar un string añadiendo espacios según lo señalemos.
#Método ljust():permite alinear u string a la izquierda añadiendo espacios según lo señalemos.
#método rjust():permite alinear u string a la derecha añadiendo espacios según lo señalemos.
string = "Menú"

print("Métodos con espacios: ")
print(string.center(20))
print(string.ljust(20))
print(string.rjust(20))


print("\nMétodos con carácter: ")
print(string.center(20, "="))
print(string.ljust(20, "="))
print(string.rjust(20, "="))


print("\nVariable modificada: ")
string = string.center(20, "=")
print(string)
      

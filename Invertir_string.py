#Programa que invierte una cadena de caracteres.

string = input("Introduce un string para invertirlo: ")
string_reversed = ""

for character in string:
    string_reversed = character + string_reversed

print(f"string invertido: {string_reversed}")    

#Substring o subcadena:es una sucesión de caracteres dentro de una cadena principal.

string = "0123456789"
substring = ""
print(f"Cadena principal: {string}")

substring = string[0]
print(f"\nSubcadena con índice en la posición [0] es: {substring}")

substring = string[5]
print(f"\nSubcadena con índice en la posición [5] es: {substring}")

substring = string[-4]
print(f"\nSubcadena con índice en la posición [-4] es: {substring}")

substring =string[0:3]
print(f"\nSubcadena con índices en las posiciónes [0:3] es: {substring}")

substring = string[:3]
print(f"\nSubcadena con índices en las posiciónes [:3] es: {substring}")

substring = string[5:]
print(f"\nSubcadena con índices en las posiciónes [5:] es: {substring}")

substring = string[-4:-1]
print(f"\nSubcadena con índices en las posiciónes [-4:-1] es: {substring}")

substring = string[:]
print(f"\nSubcadena con índices en las posiciónes [:] es: {substring}")

substring = string[1:6:2]
print(f"\nSubcadena con índices en las posiciónes y salto [1:6:2] es: {substring}")

substring = string[::3]
print(f"\nSubcadena con índices en las posiciónes y salto [::3] es: {substring}")

















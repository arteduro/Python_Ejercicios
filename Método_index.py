#Método index():nos permite localizar dentro de una lista, un elemnto específico.

vocales = ["a", "e", "i", "o", "u", "a",]

print(f"Lista de vocales: {vocales}")
print(f"La letra a está en la posición: {vocales.index('a')}")
print(f"La letra i está en la posición: {vocales.index('i')}")
print(f"La letra u en el rango 2-final está en la posición: {vocales.index('u', 2)}")
print(f"La letra i en el rango 2-4 está en la posición: {vocales.index('i', 2, 4)}")

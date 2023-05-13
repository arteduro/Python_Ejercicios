#Método Title: permite convertir la primera letra de cada palabra a mayúsculas.
#Método Istitle: permite convertir el resto de las letras de cada palabra a minúsculas.
frist_name = input("Nombre: ")
last_name = input("Apellido: ")
full_name = f"{frist_name} {last_name}"

print()
print(f"¿ Elformato del método title() se ha aplicado?: {full_name.istitle()}")
print(f"Aplicando el método title(): {full_name.title()}")
print(f"Volvamos a imprimir el nombre: {full_name}")

print()
full_name = full_name.title()
print(f"¿ Elformato del método title() se ha aplicado?: {full_name.istitle()}")
print(f"Se ha aplicado el método title() de manera permanente: {full_name}")


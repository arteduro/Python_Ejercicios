#Instrucción del: nos permite eliminar toda una lista, y a su vez, nos permite eliminar un único elemento.
#o bien, eliminar dos o más elemntos de manera simultanea.

vocales = ["a", "e", "i", "o", "u",]
print(f"Listas: {vocales}")
del vocales[3]
print(f"del vocales[3]: {vocales}")

vocales = ["a", "e", "i", "o", "u",]
print(f"\nListas: {vocales}")
del vocales[0:2]
print(f"del vocales[0:2]: {vocales}")

vocales = ["a", "e", "i", "o", "u",]
print(f"\nListas: {vocales}")
del vocales[:]
print(f"del vocales[:]: {vocales}")


print("""\n(_______)  | |                       /\         _                          
 _____   _ | | ____  ____  ____     /  \   ____| |_  ____ ____  ____  ____ 
|  ___) / || |/ _  |/ _  |/ ___)   / /\ \ / ___)  _)/ _  ) _  |/ _  |/ _  |
| |____( (_| ( ( | ( ( | | |      | |__| | |   | |_( (/ ( ( | ( ( | ( ( | |
|_______)____|\_|| |\_||_|_|      |______|_|    \___)____)_||_|\_|| |\_||_|
             (_____|                                          (_____|      """)



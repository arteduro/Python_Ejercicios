#Método pop():nos permite acceder a una lista y elinimar ta sea el último elemento o un elemento esprcífico.

vocales = ["a", "e", "i", "o", "u",]
print(f"Lista: {vocales}")
print(f"Elemento eliminado: {vocales.pop()}")
print(f"Lista: {vocales}")

vocales = ["a", "e", "i", "o", "u",]
print(f"\nLista: {vocales}")
print(f"Elemento eliminado en la posición 2: {vocales.pop(2)}")
print(f"Lista: {vocales}")

vocales = ["a", "e", "i", "o", "u",]
print(f"\nLista: {vocales}")
print(f"Elemento eliminado en la posición 0: {vocales.pop(0)}")
print(f"Lista: {vocales}")

vocales = ["a", "e", "i", "o", "u",]
print(f"\nLista: {vocales}")
print(f"Elemento eliminado en la posición -2: {vocales.pop(-2)}")
print(f"Lista: {vocales}")

print("""\n|  ___|  | |                   / _ \     | |                        
| |__  __| | __ _  __ _ _ __  / /_\ \_ __| |_ ___  __ _  __ _  __ _ 
|  __|/ _` |/ _` |/ _` | '__| |  _  | '__| __/ _ \/ _` |/ _` |/ _` |
| |__| (_| | (_| | (_| | |    | | | | |  | ||  __/ (_| | (_| | (_| |
\____/\__,_|\__, |\__,_|_|    \_| |_/_|   \__\___|\__,_|\__, |\__,_|
             __/ |                                       __/ |      
            |___/                                       |___/   """)

##Método append():nos permite agregar nuevos elementos al final de una lista.

print("Agregando un elemento a la lista.")
letters = ["a", "b", "c", "d"]
print(f"Lista: {letters}")
letters.append("e")
print(f"Lista: {letters}")

print("\nAgregando tres elementos a la lista.")
letters = ["a", "b", "c", "d"]
print(f"Lista: {letters}")
letters.append("e")
letters.append("f")
letters.append("g")
print(f"Lista: {letters}")

print("\nAgregando tres elementos de distinti tipo de dato a la lista.")
letters = ["a", "b", "c", "d"]
print(f"Lista: {letters}")
letters.append(5)
letters.append(2.5)
letters.append(True)
print(f"Lista: {letters}")

print("""\n|  ___|  | |                   / _ \     | |                        
| |__  __| | __ _  __ _ _ __  / /_\ \_ __| |_ ___  __ _  __ _  __ _ 
|  __|/ _` |/ _` |/ _` | '__| |  _  | '__| __/ _ \/ _` |/ _` |/ _` |
| |__| (_| | (_| | (_| | |    | | | | |  | ||  __/ (_| | (_| | (_| |
\____/\__,_|\__, |\__,_|_|    \_| |_/_|   \__\___|\__,_|\__, |\__,_|
             __/ |                                       __/ |      
            |___/                                       |___/   """)


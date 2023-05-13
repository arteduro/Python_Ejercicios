#Método Insert():nos permite insertar un elemento en una posición determinada.

print("Lista original")
letters = ["b", "d", "f", "g"]
print(f"Lista: {letters}")

print("\n Insertanso 'a' en posición 0")
letters.insert(0, "a")
print(f"Lista: {letters}")

print("\n Insertanso 'c' en posición 2")
letters.insert(2, "c")
print(f"Lista: {letters}")

print("\n Insertanso 'e' en posición 4")
letters.insert(4, "e")
print(f"Lista: {letters}")

print("\n Insertanso 'z' en posición 100")
letters.insert(100, "z")
print(f"Lista: {letters}")

print("""\n|  ___|  | |                   / _ \     | |                        
| |__  __| | __ _  __ _ _ __  / /_\ \_ __| |_ ___  __ _  __ _  __ _ 
|  __|/ _` |/ _` |/ _` | '__| |  _  | '__| __/ _ \/ _` |/ _` |/ _` |
| |__| (_| | (_| | (_| | |    | | | | |  | ||  __/ (_| | (_| | (_| |
\____/\__,_|\__, |\__,_|_|    \_| |_/_|   \__\___|\__,_|\__, |\__,_|
             __/ |                                       __/ |      
            |___/                                       |___/   """)

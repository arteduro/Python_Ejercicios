#Método remove():nos permite eliminar un elemento dentro de una lista,especificando atravéz de un argumento,
#el elemnto que deseamos eliminar

vocales = ["a", "e", "i", "o", "u",]
print(f"Lista: {vocales} \Elemento a eliminar: i")
vocales.remove("i")
print(vocales)

vocales = ["a", "e", "i", "o", "u",]
print(f"\nLista: {vocales} \Elemento a eliminar: o")
vocales.remove("o")
print(vocales)

vocales = ["a", "e", "i", "o", "i",]
print(f"\nLista: {vocales} \Elemento a eliminar: i")
vocales.remove("i")
print(vocales)

print("""\n|  ___|  | |                   / _ \     | |                        
| |__  __| | __ _  __ _ _ __  / /_\ \_ __| |_ ___  __ _  __ _  __ _ 
|  __|/ _` |/ _` |/ _` | '__| |  _  | '__| __/ _ \/ _` |/ _` |/ _` |
| |__| (_| | (_| | (_| | |    | | | | |  | ||  __/ (_| | (_| | (_| |
\____/\__,_|\__, |\__,_|_|    \_| |_/_|   \__\___|\__,_|\__, |\__,_|
             __/ |                                       __/ |      
            |___/                                       |___/   """)

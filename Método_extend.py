#Método extend():nos permite concatenar dos o más listas,y a su vez,nos permite agregar varios elementos a una lista.

invitados = ["Carolina", "Juan", "Gerardo"]
amigos = ["Luis", "Ana"]
print(f"Lista invitados: {invitados} \nLista amigos: {amigos}")
invitados.extend(amigos)
print(f"Lista invitados: {invitados}")

numeros = [10, 20]
print(f"\nLista números: {numeros}")
numeros.extend(range(30, 100, 10))
print(f"Lista números: {numeros}")

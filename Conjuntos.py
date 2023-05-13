
set_paises = {'Colombia', 'Mexico', 'Bolivia'}


#Tamaño del conjunto
tamaño = len(set_paises)
print(tamaño)

#Preguntar por elemento especifíco}
print("Colombia" in set_paises)

# agregar
set_paises.add('Peru')
print(set_paises)


# actualizar
set_paises.update({'Venezuela', 'Brazil', 'Chile'})
print(set_paises)


# eliminar
set_paises.remove("Chile")
print(set_paises)


# Desartar = eliminar
set_paises.discard("Venezuela")
print(set_paises)


# Vaciar comjunto = eliminar
set_paises.clear()
print(set_paises)
print(len(set_paises))

# ----------------------
# CONJUNTO (SET) [Colección no ordenada y mutable de elementos únicos]
# ----------------------

# El booleano True con el número 1
# El booleano False con el número 0

# conjunto_frutas = { "Manzana", "Plátano", "Pera", 0, 1, True, False} # Toma 5 de longitud solamente porque a 0 y 1 lo toma como true y false

# longitud = len(conjunto_frutas)

# print(longitud)

# conjunto_frutas = set( ( "Manzana", "Pera", "Uva" ) )

# print(conjunto_frutas)

# conjunto_frutas = ("Manzana",) # Para crear un conjunto con un solo elemento debo poner la coma luego del primer elemento de lo contrario me toma el string como una colección
#                                # Esto es tanto para el set como para las tuplas3

# print(conjunto_frutas)


# # Acceder y Agregar items de un set

# conjunto_frutas = {"Manzana", "Pera", "Limón", "Naranja"} # No se puede acceder a un item en particular a traves de un indice porque no tienen orden

# print("---------------------------")
# for fruta in conjunto_frutas:
#     print(fruta)

# print("---------------------------")
# if "Manzana" in conjunto_frutas:
#     print("Si existe")

# print("---------------------------")
# conjunto_frutas.add("Banana")
# print(conjunto_frutas)

# # Agregar mas sets

# conjunto_tropicales = {"Piña", "Mango", "Papaya"}

# conjunto_frutas.update(conjunto_tropicales)

# print("---------------------------")
# print(conjunto_frutas)


# # Agregar a un set una lista que no es un set

# lista_frutas = ["Kiwi", "Mandarina"]

# conjunto_frutas.update(lista_frutas)

# print("---------------------------")
# print(conjunto_frutas)

# # Eliminar un elemento

# conjunto_frutas.remove("Manzana")

# print("---------------------------")
# print(conjunto_frutas)

# conjunto_frutas.discard("Manzana")

# print("---------------------------")
# print(conjunto_frutas)

# conjunto_frutas.pop() # Borra uno aleatoreamente

# print("---------------------------")
# print(conjunto_frutas)

# conjunto_frutas.clear() # Borra todo

# print("---------------------------")
# print(conjunto_frutas)


# del conjunto_frutas # Borra el espacio en memoria y da none en el print

# print("---------------------------")
# print(conjunto_frutas)


# Juntar Conjuntos y Bucles

# conjunto_letras = {"a", "b", "c"}
# conjunto_numeros = {1, 2, 3}

# union = conjunto_letras.union(conjunto_numeros)

# print(union)

# print("--------------------------------")

# union = conjunto_letras | conjunto_numeros

# print(union)

# print("--------------------------------")

# conjunto_letras.update(conjunto_numeros) 

# print(conjunto_letras)


# set_tecnologia_universidad_chicago = {"Python", "Javascript", "AWS"}
# set_tecnologia_universidad_oxford = {"Python", "Typescript", "GoogleCloud"}

# # Tanto el intersection como el & agrupan los elementos que tienen en común lo sets
# set3 = set_tecnologia_universidad_chicago.intersection(set_tecnologia_universidad_oxford)

# print(set3)

# set3 = set_tecnologia_universidad_chicago & set_tecnologia_universidad_oxford

# print(set3)

# # Me actualiza el segundo listado con la intersección
# set_tecnologia_universidad_chicago.intersection_update(set_tecnologia_universidad_oxford)

# print(set_tecnologia_universidad_chicago)


# set_chicago = {"Python", "Javascript", "AWS"}
# set_oxford = {"Python", "Typescript", "GoogleCloud"}

# # Agrupa los elementos diferentes entre los dos listados tanto difference como -
# set3 = set_chicago.difference(set_oxford)

# print(set3)

# set3 = set_chicago - set_oxford

# print(set3)

# # Actualiza el segundo listado con las diferencias
# set_chicago.difference_update(set_oxford)

# print(set_chicago)


conjunto_frutas = { "Manzana", "Plátano", "Pera"}

# La única forma de recorrer el set es con un for porque al no tener indice no podemos utilizar el while
for fruta in conjunto_frutas:
    print(fruta)


# con copy copiamos un conjunto

conjunto_copia = conjunto_frutas.copy()
print(conjunto_copia)
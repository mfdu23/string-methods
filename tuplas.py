# --------------------------------------
# TUPLAS [ Colección de elementos inmutables y ordenados ] 
# --------------------------------------

# frutas = ("Manzana", "Plátano", "Uvas")
# numeros = (1,2,3)
# booleanos = (True, True, False)
# mixto = ("Manzana", 1, True)
# frutas = tuple(("Manzana", "Plátano", "Uva")) # Inicio Tuola con constructor

frutas = ("Manzana", "Uva", "Fresa", "Mandarina", "Aguacate", "Kiwi")

# print(frutas[1:4])
# if "Mandarina" in frutas:
#     print("Sí, hay mandarina entre las frutas que tengo")    

# frutas[1] = "Coco" # No se puede modificar el indice 1 porque es una tupla

# Para poder modificar la tupla se hace lo siguiente

# frutas2 = list(frutas) #Lista
# frutas2[1] = "Coco" # Modifico la lista

# frutas = tuple(frutas2) # Convierto a tupla la lista y la reasino a la variable original

# print(frutas)

# tupla_frutas = ("Manzana", "Uva", "Fresa", "Mandarina", "Aguacate", "Naranja", "Kiwi")

# lista_frutas = list(tupla_frutas)

# lista_frutas.append("Coco")

# tupla_frutas = tuple(lista_frutas)

# print(tupla_frutas)

# Agregar una tupla a otra tupla

# tupla_verduleria = ("Manzana", "Uva", "Fresa", "Mandarina", "Aguacate", "Naranja", "Kiwi")
# tupla_verdura = ("Zabahoria", "Ajo", "Brocoli")

# tupla_verduleria += tupla_verdura

# print(tupla_verduleria)

# Remover un item

# tupla_frutas = ("Manzana", "Uva", "Fresa", "Mandarina", "Aguacate", "Naranja", "Kiwi")

# lista_fruta = list(tupla_frutas)

# lista_fruta.remove("Uva")

# tupla_frutas = tuple(lista_fruta)

# print(tupla_frutas)

# del(tupla_frutas) # Elimina la tupla completa

# print(tupla_frutas)

# Desenpaquetado de tuplas
tupla_frutas = ("Manzana", "Uva", "Fresa", "Mandarina", "Aguacate", "Naranja", "Kiwi")

(a, b, c, d, e, f, g) = tupla_frutas # Desenpaquetado de tuplas en distintas variables (No se puede desenpaquetar solo una parte)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

# (a, b, c) = tupla_frutas # No se puede desenpaquetar así porque la cantidad de items es 7

# print(a)
# print(b)
# print(c)

(a, b, c, *d) = tupla_frutas # Pero si se puede hacer esto para obtener los primeros 3 items

print("------------------------------")
print(a)
print(b)
print(c)
print(d)


(a, *b, c) = tupla_frutas # Si necesito desempaquetar la primera y la última hago lo siguiente

print("------------------------------")
print(a)
print(b)
print(c)

# Lo que hace el asterisco es tomar todo lo que está en valores individuales y asignar una lista


# BUCLES EN TUPLAS
print("------------------------------")
for fruta in tupla_frutas:
    print(fruta)

print("------------------------------")
for i in range(len(tupla_frutas)):
    print(tupla_frutas[i], "con el indice:", i)

print("------------------------------")
i = 0
while i < len(tupla_frutas):
    print(tupla_frutas[i])
    i += 1



# UNION DE TUPLAS
tupla_frutas1 = ("Manzana", "Uva", "Fresa")
tupla_frutas2 = ("Mandarina", "Aguacate", "Naranja", "Kiwi")

tupla_frutas = tupla_frutas1 + tupla_frutas2

print("------------------------------")
print(tupla_frutas)

tupla_frutas = tupla_frutas1 * 2 + tupla_frutas2 # Se pueden múltiplicar las tuplas

print("------------------------------")
print(tupla_frutas)

print("------------------------------")
print(tupla_frutas1.index("Uva")) # Me perimite ver en que posición está un indice determinado


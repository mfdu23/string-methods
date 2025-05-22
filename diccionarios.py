# ----------------------------
# DICCIONARIO [Colección no ordenada de pares clave-valor]
# ---------------------------

# Los diccionarios mantienen el orden con que fueron creados

from logging.config import dictConfig


diccionario = {
    "nombre": "Martin Dupraz",
    "tecnologias": ["Python", "Javascript"],
    "edad": 41,
    "ciudad": "Las Varillas",
    "profesión": "Desarrollador"

}

# print(diccionario)

# print(diccionario["nombre"])
# print(diccionario["tecnologias"])

# # Asignar variable a un dato

# nombre = diccionario.get("nombre")

# print(nombre)

# # Obtener las claves

# claves = diccionario.keys()
# print(claves)

# # Asignar valor a una clave

# diccionario["nombre"] = "Pablo Perez"

# print(diccionario)

# #Agregar una clave al diccionario (Al poner una clave que no existia me crea una nueva)

# diccionario["primo"] = "Martin Dupraz"

# print(diccionario)

# # Me muestra solo los valores
# valores = diccionario.values()
# print(valores)

# # Lista de tuplas clave valor
# item = diccionario.items()
# print(item)

# # Validar si existe una clave

# if "nombre" in diccionario:
#     print("Existe clave")

# # Agregar, Cambiar y eliminar pares clave - valor

# diccionario["nombre"] = "Ricardo Rojas"
# print(diccionario)

# diccionario.update({"nombre": "Ricardo Raul", "edad": 42})
# print(diccionario)

# # Agregar claves
# diccionario["direccion"] = "Jorge Baravalle 285"
# print(diccionario)

# diccionario.update({"nombre": "Ricardo Raul", "edad": 42, "Piso": "1 A"})
# print(diccionario)

# #Eliminar Claves
# diccionario.pop("profesión")
# print(diccionario)

# # Elimina el último
# diccionario.popitem()
# diccionario.popitem()
# print(diccionario)

# del diccionario["nombre"]
# print(diccionario)

# diccionario.clear()
# print(diccionario)


#Copiar diccionario y bucles

# diccionario2 = diccionario.copy() # Así no copia las diferencias, son dos diccionarios diferentes
# print(diccionario2)

# # diccionario2 = diccionario # Esto copia la referencia y si modificamos uno se modifica el otro porque mantiene la referencia

# diccionario2 = dict(diccionario)
# print(diccionario2)

# # Esto imprime las claves
# for key in diccionario:
#     print(key)

# # Esto imprime los valores de la clave
# for key in diccionario:
#     print(diccionario[key])

# # Esto imprime los valores de la clave
# for key in diccionario:
#     print("Clave",key, "Valor", diccionario[key])

# #Esto imprime los valores
# for valores in diccionario.values():
#     print(valores)

# # Desestructurar

# for x,y in diccionario.items():
#     print("Clave:",x, "- Valor:", y)

#Diccionarios anidads

familia = {
    "padre": {
        "nombre": "Raúl",
        "profesion": "Carpintero"
    },
    "madre": {
        "nombre": "Patricia",
        "profesion": "Abogada"
    },
    "hijo": {
        "nombre": "Pedro",
        "profesion": "desempleado"
    }
}

print(familia["padre"]["profesion"])

for pariente, data in familia.items():
    print(pariente)

    for clave in data:
        print(clave + ":", data[clave])
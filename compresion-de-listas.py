#------------------------------
# COMPRENSION DE LISTA [ Colección de elementos mutables y ordenados]
#------------------------------

#nombre
frutas = ["Manzana", "Plátano", "Pera", "Mandarina", "Fresa", "Piña"]
#               dato a                
#nombre         asignar   bucle                     condición
# frutas_con_e = [fruta for fruta in frutas if "e" in fruta]
# print(frutas_con_e)

# frutas_con_e2 = [fruta for fruta in frutas if fruta != "Mandarina"]
# print(frutas_con_e2)

# rango = [x for x in range(10) if x < 5]
# print(rango)

# mayusculas = [fruta.upper() for fruta in frutas]
# print(mayusculas)

# frutas_reemplazado = [fruta if fruta != "Pera" else "Aguacate" for fruta in frutas]
# print(frutas_reemplazado)

#--------------------------------
# ORDENAMIENTO DE LISTAS
#--------------------------------

# frutas.sort()
# print(frutas)

numeros = [9, 999, 88, 1, 2, 3]

# numeros.sort()
# print(numeros)

# frutas.sort(reverse=True)
# print(frutas)

frutas2 = ["Manzana", "Plátano", "pera", "mandarina", "Fresa", "Piña"]
# frutas2.sort()
# frutas2.sort(key = str.lower) # Para no prestarle atención al orden entre mayúsculas y minúsculas

frutas2.reverse() # Da vuelta toda la lista

print(frutas2)
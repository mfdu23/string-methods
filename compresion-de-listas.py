#------------------------------
# LISTA [ Colección de elementos mutables y ordenados]
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

 frutas_reemplazado = [fruta if fruta != "Pera" else "Aguacate" for fruta in frutas]
 print(frutas_reemplazado)
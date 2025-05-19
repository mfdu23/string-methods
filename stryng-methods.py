texto = "hoLa muNdo"
texto_con_espacios = "      texto con espacios        "
texto_separado = "Python,Javascript,Django,React"
lista = ["Hola", "Juan", "Carlos"]
numeros = "123456"
letras = "abc"
espacio = " "
repeticion = "manzana, banana, manzana, pera"

print("capitalize: ", texto.capitalize()) #Convierte la primera letra en mayuscula el resto en minuscula
print("upper:", texto.upper()) #Convierte el text entero en mayúsculas
print("lower:", texto.lower()) #Convierte el texto entero en minúsculas
print("strip", texto_con_espacios.strip()) #Elimna los espacios al comienzo y al final
print("replace", texto_con_espacios.replace("espacios", "gracias")) # Reemplaza una palabra por otra
print("split", texto_separado.split(",")) # Separar texto en items en una lista
print("join", ",".join(lista)) # Junta los items de una lista en un string
print("find:", texto.find("muNdo")) # Muestra la posición donde arranca el texto ingresado
print("startswith:", texto.endswith("hoLa")) # Indica si comienza o no con una palabra ingresaqda
print("endwith:", texto.endswith("muNdo")) # Indica si termina o no con una palabra ingresaqda
print("isdigit:", numeros.isdigit()) # Indica si todos los caracteres son números o no (espacios no son numeros)
print("isalpha:", texto.isalpha()) # Indica si todos los caracteres son letras o no (espacios no son letras)
print("isalnum", letras.isalnum()) # Indica si todos los caracteres son alphanuméricos o no (espacios no son letras ni números)
print("isspace:", espacio.isspace()) # Insica si el texto ingresado es solo espacios
print("count:", repeticion.count("manzana")) # Indica cuantas veces se repite la palabra ingresada
print("index:", texto.find("muNdo")) # Muestra la posición donde arranca el texto ingresado
print("rfinde:", repeticion.rfind("manzana")) # Indica la posición en donde arranza la última repetición



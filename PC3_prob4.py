#Escriba una función que, dado un string, retorne la longitud de la última palabra. Se considera
#que las palabras están separadas por uno o más espacios. También podría haber espacios al
#principio o al final del string pasado por parámetro.

def longitud_ultima_palabra(string):
    # Eliminar los espacios al principio y al final del string
    string = string.strip()
    
    # Dividir el string en palabras separadas por espacios
    palabras = string.split()
    
    # Verificar si hay palabras en el string
    if len(palabras) == 0:
        return 0
    
    # Obtener la última palabra y retornar su longitud
    ultima_palabra = palabras[-1]
    return len(ultima_palabra)


texto = "Buenas noches con todos"
longitud = longitud_ultima_palabra(texto)
print("Longitud de la última palabra:", longitud)
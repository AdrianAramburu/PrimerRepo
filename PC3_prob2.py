#Cree un programa que solicite al usuario una lista de calificaciones separadas por comas. Divida
#la cadena en calificaciones individuales y almacénelas en una lista para luego convertir cada
#calificación en un entero. Deberá utilizar una sentencia try/except para informar al usuario
#cuando los valores introducidos no puedan ser convertidos debido a un error de tipeo o
#formato. (Los métodos de cadena le serán de utilidad)

def las_calificaciones():
    while True:
        califica_input = input("Digite las calificaciones (separador-->,): ")
        califica_list = califica_input.split(',')
        califica_convertidas = []

        try:
            for calificacion in califica_list:
                califica_entero = int(calificacion.strip())
                califica_convertidas.append(califica_entero)
            return califica_convertidas
        except ValueError:
            print("Ha ocurrido un error, las calificaciones deben ser numeros enteros")

calificaciones = las_calificaciones()
print("Calificaciones:", calificaciones)
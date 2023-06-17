#Implemente un programa que solicite al usuario una fracción, con
#formato X/Y, donde cada uno de X e Y es un número entero, y luego
#muestra, como un porcentaje redondeado al número entero más
#cercano, donde se indicará la cantidad de combustible en el
#tanque. Se debe tener en cuenta los siguientes casos:
#- Colocar E en caso X/Y sea menor a 1% del total
#- Colocar F en caso X/Y sea mayor a 99%.
#- En otro caso, devolver el valor en porcentaje %


def porcentaje(fraccion):
    try:
        num, den = map(int, fraccion.split('/'))
        if den == 0:
            raise ZeroDivisionError
        if num < 0 or den <= 0:
            raise ValueError
        el_porcentaje = (num / den) * 100
        if el_porcentaje < 1:
            return "E"
        elif el_porcentaje >= 100:
            return "F"
        else:
            return f"{round(el_porcentaje)}%"
    except ValueError:
        print("Ah ocurrido un error... Los números deben ser enteros y mayores o iguales a cero.")
    except ZeroDivisionError:
        print("Ah ocurrido un error... Vuelve a intentarlo")
    return None

def pido_fraccion():
    while True:
        frac = input("Digite una fracción (X/Y): ")
        res = porcentaje(frac)
        if res is not None:
            return res

resultado = pido_fraccion()
if resultado is not None:
    print("La cantidad de combustible en el tanque es:", resultado)








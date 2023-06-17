def suma(m, n):
    try:
        resultado = m + n
        return resultado
    except TypeError:
        print("Ha ocurrido un error...")

def resta(m, n):
    try:
        resultado = m - n
        return resultado
    except TypeError:
        print("Ha ocurrido un error...")

def producto(m, n):
    try:
        resultado = m * n
        return resultado
    except TypeError:
        print("Ha ocurrido un error...")

def division(m, n):
    try:
        if n == 0:
            raise ZeroDivisionError
        resultado = m / n
        return resultado
    except ZeroDivisionError:
        print("Ha ocurrido un error... No se puede dividir entre cero")
    except TypeError:
        print("Ha ocurrido un error...")

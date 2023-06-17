#Escribe una función de Python que imprima las primeras n filas del triángulo de Pascal.
#Nota: El triángulo de Pascal es una figura aritmética y geométrica imaginada por primera vez por Blaise Pascal.

def triangulo_pascal(n):
    if n <= 0:
        print("El número de filas debe ser mayor a cero.")
        return
    
    triángulo = []
    for i in range(n):
        fila = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                fila[j] = triángulo[i-1][j-1] + triángulo[i-1][j]
        triángulo.append(fila)
    
    for fila in triángulo:
        for num in fila:
            print(num, end=' ')
        print()

triangulo_pascal(5)
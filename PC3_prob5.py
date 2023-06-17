#Desarrollar un módulo que contenga las siguientes funciones:
#● Que genere 20 números enteros aleatorios entre 0 y 100 y devuelva una lista.
#● Mostrar la lista obtenida por pantalla.
#● Ordenar los valores de la lista y mostrarla por pantalla.
#Luego crea un script main.py en el mismo directorio en el que deberás importar el módulo y ejecutar las funciones.
#Nota: utilizar el módulo “random” para generar un número aleatorio.

import random

def generar_numeros_aleatorios():
    numeros = []
    for _ in range(20):
        numero = random.randint(0, 100)
        numeros.append(numero)
    return numeros

def mostrar_lista(lista):
    print("Lista de números:")
    for numero in lista:
        print(numero, end=" ")
    print()

def ordenar_lista(lista):
    lista.sort()
    print("Lista ordenada:")
    for numero in lista:
        print(numero, end=" ")
    print()


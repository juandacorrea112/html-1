from matematicas import Matematica
from mensajero import Impresion

a = int(input("Ingrese un numero"))
b = int(input("Ingrese un numero"))

mate = Matematica()
muestra = Impresion()

suma = mate.sumar(a, b)
muestra.imprimir(suma)
# 1- Hacer un programa que imprima del 10 al 0 en orden decreciente.
desde = 10
hasta = 0
elementos = [0,1,2,3,4,5,6,7,8,9,10]
def imprimir(dato):
    print(dato)

while (desde >= hasta):
    imprimir(elementos[desde])
    desde = desde - 1
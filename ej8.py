# 8- Ingresar 5 numeros por teclado y al final de los
# mismos, el programa debe emitir los siguientes
# datos: Suma total, Cantidad de numeros impares, y
# un mensaje que indique si existen números
# superiores a 100

numeros = []
numeros_impares = []
numeros_superior_100 = []

while(len(numeros) < 5):
    numero = int(input("Ingrese un número entero: "))
    numeros.append(numero)
    if(numero % 2 == 1):
        numeros_impares.append(numero)
    if(numero > 100):
        numeros_superior_100.append(numero)

print(f"{numeros}, la suma es de {sum(numeros)}")
print(f"impares: {len(numeros_impares)}")
if len(numeros_superior_100) > 0:
    print(f"si hay valores mayor que cien (100)")
else:
    print(f"no hay valores mayor que cien (100)")
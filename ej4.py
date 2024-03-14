# Hacer un programa que imprima los números
# impares entre el 10 y el cero en orden decreciente y
# que calcule la suma de esos números impares.

desde = 10
hasta = 0
impares = []
while(desde > hasta):
    if(desde % 2 == 1):
        impares.append(desde)
    desde = desde - 1
print(f"impares: {impares}, la suma es de {sum(impares)}")

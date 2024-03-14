# 7- Hacer un programa que imprima y cuente los múltiplos de 3 que hay entre el 0 y el 20

desde = 0
hasta = 20
multiplos_de_3 = []
while (desde < hasta):
    if(desde % 3 == 0):
        multiplos_de_3.append(desde)
    desde = desde + 1

print(f"{multiplos_de_3}, hay cantidad: {len(multiplos_de_3)}")
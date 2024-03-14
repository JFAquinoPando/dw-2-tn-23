lista_super = ["leche", "pan", "carne", "frutas", "verduras"]
print(lista_super)

lista_super.append("Productos de Limpieza")
print(lista_super)

lista_super.remove("Carne".lower())
print(lista_super)

posicion = 0
for producto in lista_super:
    posicion = posicion + 1
    print(f"{posicion}- {producto}")

cantidad = 0
while(cantidad < len(lista_super)):
    print(lista_super[cantidad])
    cantidad = cantidad + 1
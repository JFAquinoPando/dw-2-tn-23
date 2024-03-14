# ejemplo de sorteo para Conmebol
# importamos (traemos) todas las funciones de la librería random (aleatorio)
import random

# Lista de clubes que pasaron a cuartos de final
listaClubes = ["Boca Juniors", "Sportivo Trinidense", "River Plate",
            "Cerro", "Libertad", "Peñarol" ,"Platense", "Fluminense"]

# Lista de llaves y emparejamientos para cuartos
listaEmparejamientos4tos = []
listaLlave = []

# Mientas la cantidad de clubes en la lista sea mayor a cero
while (len(listaClubes) > 0):
    # genero un numero entre 0 y la cantida de elementos menos uno
    posicion_aleatoria = random.randint(0,len(listaClubes)-1)

    #Agrego a la lista llave el club que salio sorteado
    listaLlave.append(listaClubes[posicion_aleatoria])
    # Lo quito a ese mismo club de la lista de clubes
    listaClubes.remove(listaClubes[posicion_aleatoria])
    
    #Si ya está lista una llave con 2 equipos
    if(len(listaLlave) == 2):
        # Lo agregamos a los enfrentamientos de cuartos
        listaEmparejamientos4tos.append(listaLlave)
        # Limpiamos/vaciamos a llave
        listaLlave = []

#print(listaEmparejamientos4tos)

posicion = 0
# Recorro todo e imprimo
while(len(listaEmparejamientos4tos) > posicion):
    print(f"{posicion + 1}) {listaEmparejamientos4tos[posicion][0]} vs {listaEmparejamientos4tos[posicion][1]}")
    posicion = posicion + 1
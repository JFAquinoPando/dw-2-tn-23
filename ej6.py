# 6- Introducir por teclado tantas frases como se deseen y contarlas.

frases = []
frase = input("Introduce tu frase: ")

while(frase != "*"):
    frases.append(frase)
    frase = input("Introduce tu frase: ")

print(f"Tengo {len(frases)} frases...")
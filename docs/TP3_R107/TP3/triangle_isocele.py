h = int(input("Entrez la hauteur du triangle isocèle : "))

for i in range(1, h + 1):
    espaces = h - i
    etoiles = 2 * i - 1
    print(" " * espaces + "*" * etoiles)

compteur = 0

for i in range(1, 101):
    compteur += str(i).count('7')

print("Nombre de 7 rencontrés entre 1 et 100 :", compteur)

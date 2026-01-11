import random
def liste_utilisateur(n=5):
    """
    Retourne une liste de n entiers saisis par l'utilisateur
    Par défaut n vaut 5
    """
    liste = []
    for _ in range(n):
        Valeur = int(input("Saississez une valeur ? "))
        liste.append(Valeur)
    return liste
def liste_aleatoire(n=5, bornemin=0, bornemax=20):
    """
    Retourne une liste de n entiers aléatoires compris entre bornemin et bornemax
    Par défaut : n vaut 5, bornemin vaut 0 et bornemax vaut 100
    """
    liste = []
    for _ in range(n):
        Valeur = random.randint(bornemin, bornemax)
        liste.append(Valeur)
    return liste
#instruction de test
l1 = liste_utilisateur(4)
print(l1)
l2 = liste_aleatoire(4)
print(l2)
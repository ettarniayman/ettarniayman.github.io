import random

def liste_aleatoire(n, a=0, b=10):
    """Retourne une liste de n entiers aléatoires entre a et b (inclus)."""
    return [random.randint(a, b) for _ in range(n)]

def liste_utilisateur(n):
    """Demande à l'utilisateur de saisir n entiers et retourne la liste."""
    liste = []
    for i in range(n):
        val = int(input(f"Entrez l'entier {i+1} : "))
        liste.append(val)
    return liste
#test
if __name__ == "__main__":
    l1 = liste_utilisateur(4)
    print(l1)

    l2 = liste_aleatoire(4)
    print(l2)

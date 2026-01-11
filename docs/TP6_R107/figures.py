
def carre(n: int = 4) -> None:
    """
    Affiche un carré d'étoiles de côtés de longueur n
    """
    for _ in range(n):
        print("*" * n)

def carre_blanc(n: int = 4) -> None:
    """
    Affiche un carré d'étoiles de côtés de longueur n
    Les étoiles sont uniquement au bord du carré
    """
    for i in range(n):
        if i == 0 or i == n - 1:
            print("*" * n)
        else:
            print("*" + " " * (n - 2) + "*")

def tri_rect(h: int = 4) -> None:
    """
    Affiche un triangle rectangle d'étoiles de hauteur h
    """
    for i in range(1, h + 1):
        print("*" * i)

def tri_iso(h: int = 4) -> None:
    """
    Affiche un triangle isocèle d'étoiles de hauteur h
    """
    for i in range(1, h + 1):
        
        print(" " * (h - i) + "*" * (2 * i - 1))

if __name__ == "__main__":
    carre()
    print()
    carre_blanc()
    print()
    tri_rect()
    print()
    tri_iso()


choix = input("Voulez-vous compter vers le haut ou vers le bas ? (haut/bas) ").strip().lower()
if choix not in ["haut", "bas"]:
    print("Choix invalide. Veuillez taper 'haut' ou 'bas'.")
else:
    
    n = int(input("Entrez un nombre entier inférieur à 50 : "))

    if n >= 50:
        print("Le nombre doit être inférieur à 50.")
    else:
        if choix == "haut":
            for i in range(1, n + 1):
                if i < n:
                    print(i, end=", ")
                else:
                    print(i)
        else:  
            for i in range(50, n - 1, -1):
                if i > n:
                    print(i, end=", ")
                else:
                    print(i)


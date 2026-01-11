n = int(input("entrer un nombre inferieur a 20 : "))
if n > 20:
   n = int(input("erreur!! entrer un nombre inferieur a 20 : "))
else:
    for i in range(20, n - 1, -1):
        if i > n:
            print(i, end=", ")
        else:
            print(i)


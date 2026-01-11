mot = input("Mot ? ")
n = int(input("combien de repetition : "))
print("voici", n," repetition:", end=" ")
for i in range(n):
    print(mot, end=" ")
print()
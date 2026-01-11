import random

def adresses_ip(classe: str = "A") -> str:
    """
    Retourne une adresse IPv4 aléatoirement de classe `classe`.
    Classes possibles : A, B, C, D, E
    """
    plages = {
        "A": (0, 127),
        "B": (128, 191),
        "C": (192, 223),
        "D": (224, 239),
        "E": (240, 255)
    }
    
    if classe not in plages:
        raise ValueError("Classe invalide. Choisir parmi A, B, C, D, E.")
    premier_octet = random.randint(*plages[classe])
    autres_octets = [(0, 255) for _ in range(3)]
    
    adresse = f"{premier_octet}.{autres_octets[0]}.{autres_octets[1]}.{autres_octets[2]}"
    return adresse

def classe(adresse: str) -> str:
    """
    Retourne la classe de l'adresse IPv4 donnée.
    """
    premier_octet = int(adresse.split('.')[0])
    
    if 0 <= premier_octet <= 127:
        return "A"
    elif 128 <= premier_octet <= 191:
        return "B"
    elif 192 <= premier_octet <= 223:
        return "C"
    elif 224 <= premier_octet <= 239:
        return "D"
    elif 240 <= premier_octet <= 255:
        return "E"
    else:
        return "Classe inconnue"

if __name__ == "__main__":
    adr = adresses_ip("A")
    print(f"{adr} est de classe {classe(adr)}")

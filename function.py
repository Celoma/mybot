import random

def choisir_mot():
    with open ('data6-12.txt', 'r') as file:
        mots_pendu = file.read().split(", ")
    return random.choice(mots_pendu)[1:-1]

def afficher_mot(mot, lettres_trouvees):
    affichage = "`"
    for lettre in mot:
        if lettre.upper() in lettres_trouvees:
            affichage += lettre + " "
        else:
            affichage += "_ "
    affichage += "`"
    return affichage.strip()

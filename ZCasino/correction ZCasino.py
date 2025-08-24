from random import randrange
from math import ceil
import os

print("#### - ZCasino - ####")

def choix():
    while True:
        num = input("Veuillez choisir un numéro compris entre 0 et 49 : ")
        try:
            num = int(num)
            if 0 <= num <= 49:
                return num
            else:
                print("Choix non valide - Le numéro doit être entre 0 et 49")
        except ValueError:
            print("Choix non valide - Veuillez entrer un nombre entier")

def somme(argent):
    while True:
        s = input(f"Entrez la somme que vous souhaitez miser (max {argent}$) : ")
        try:
            s = float(s)
            if s <= 0:
                print("Choix non valide - La mise doit être positive")
            elif s > argent:
                print(f"Votre argent restant est de {argent}$ et est insuffisant pour cette mise...")
            else:
                return ceil(s)
        except ValueError:
            print("Choix non valide - Veuillez entrer un nombre")

def argent_total():
    while True:
        argent = input("Entrez la somme dans votre porte-feuille : ")
        try:
            argent = float(argent)
            if argent <= 0:
                print("Argent insuffisant!")
            else:
                return argent
        except ValueError:
            print("Choix non valide - Veuillez entrer un nombre")

def continuer(argent):
    if argent <= 0:
        print("Malheureusement vous n'avez plus d'argent")
        return False
    
    while True:
        rep = input("Voulez-vous miser encore ? (o/n) : ").lower().strip()
        if rep == "o":
            return True
        elif rep == "n":
            return False
        else:
            print("Choix invalide! (Veuillez choisir entre oui (o) et non (n))")

def est_pair(nbr):
    return nbr % 2 == 0

def calculer_gains(mise, numero_mise, numero_gagnant):
    """
    Calcule les gains selon les règles :
    - Numéro exact : récupère la mise + 3x la mise = 4x la mise
    - Même couleur : récupère la mise + 50% de la mise = 1.5x la mise  
    - Sinon : perd la mise = 0
    """
    if numero_gagnant == numero_mise:
        # Numéro exact : gain de 3x la mise + récupération de la mise
        return mise * 4
    elif est_pair(numero_mise) == est_pair(numero_gagnant):
        # Même couleur : gain de 50% + récupération de la mise
        return mise + ceil(mise * 0.5)
    else:
        # Perte totale
        return 0

def alea():
    return randrange(50)

def jouer_un_tour(argent):
    print(f"\n=== Nouveau tour - Vous avez {argent}$ ===")
    
    # Choix du numéro et de la mise
    num = choix()
    mise = somme(argent)
    numero_gagnant = alea()
    
    print(f"\nVous avez misé {mise}$ sur le numéro {num}")
    print(f"Le numéro gagnant est : {numero_gagnant}")
    
    # Calcul des résultats
    gains = calculer_gains(mise, num, numero_gagnant)
    nouvel_argent = argent - mise + gains
    
    # Affichage des résultats
    if numero_gagnant == num:
        print(f"🎉 FÉLICITATIONS ! Vous avez eu le numéro gagnant !")
        print(f"Vous récupérez votre mise ({mise}$) + vos gains ({gains-mise}$) = {gains}$")
    elif est_pair(num) == est_pair(numero_gagnant):
        couleur = "noire" if est_pair(numero_gagnant) else "rouge"
        print(f"🟡 Bonne couleur ! Les deux numéros sont de couleur {couleur}")
        print(f"Vous récupérez votre mise + 50% de bonus = {gains}$")
    else:
        couleur_mise = "noire" if est_pair(num) else "rouge" 
        couleur_gagnant = "noire" if est_pair(numero_gagnant) else "rouge"
        print(f"❌ Dommage ! Votre numéro était {couleur_mise} et le gagnant est {couleur_gagnant}")
        print(f"Vous perdez votre mise de {mise}$")
    
    print(f"Votre porte-feuille : {argent}$ → {nouvel_argent}$")
    
    return nouvel_argent

def main():
    print("Bienvenue au ZCasino !")
    print("Règles du jeu :")
    print("- Numéros pairs = couleur noire, numéros impairs = couleur rouge")  
    print("- Numéro exact : vous gagnez 3x votre mise")
    print("- Même couleur : vous gagnez 50% de votre mise") 
    print("- Sinon : vous perdez votre mise")
    print("-" * 50)
    
    argent = argent_total()
    
    while argent > 0:
        argent = jouer_un_tour(argent)
        
        if argent <= 0:
            print("\n💸 Vous n'avez plus d'argent ! Fin du jeu.")
            break
            
        if not continuer(argent):
            print(f"\nMerci d'avoir joué ! Vous repartez avec {argent}$")
            break
    
    print("Au revoir !")

# Lancement du jeu
if __name__ == "__main__":
    main()
    os.system("pause")
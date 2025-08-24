from random import randrange
from math import ceil
import os

print("#### - ZCasino - ####")

def choix():
    num = input("Veuillez choisir un numéro compris entre 0 et 49 : ")
    try:
        num = int(num)
        if (num < 0 or num > 49):
            print("Choix non valide")
            return choix()
        else:
            return num
    except:
        print("Choix non valide")
        return choix()

def somme(argent):
    s = input("Entrez la somme que vous souhaitez misé : ")
    try:
        s = float(s)
        if (s <= 0):
            print("Choix non valide")
            return somme(argent)
        elif (s > argent):
            print(f"Votre argent restant est de {argent} $ et est insuffisant pour cette mise...")
            return somme(argent)
        else:
            return ceil(s)
    except:
        print("Choix non valide")
        return somme(argent)

def argent_total():
    argent = input("Entrez la somme dans votre porte feuille : ")
    try:
        argent = float(argent)
        if (argent <= 0):
            print("Argent insufisant!")
            return argent_total()
        else:
            return argent
    except:
        print("Choix non valide")
        return argent_total()

def continuer(argent):
    if(argent > 0):
        rep = input("Voulez vous misé encore ? (o/n)")
        if (rep != "o" and rep != "n"):
            print("Choix invalide! (Veuillez choisir entre oui (o) et non (n))")
            return continuer(argent)
        else:
            if (rep == "o"):
                return True
            else:
                return False
    else:
        print("Malheureuxement vous n'avez plus d'argent")
        return False

def parite(nbr):
    if (ceil(nbr) % 2 == 0):
        return True
    else:
        return False
    
def success(s, bis, argent):
    argent += ceil(s+s*bis)-ceil(s)
    print(f"Vous avez gagné un total de : {s+s*bis} $")
    print(f"Votre porte feuille est actuellement à {argent} $")
    return argent

def failed(s, argent):
    solde = float(argent) - float(s)
    print(f"Votre porte feuille est actuellement à {argent} $")
    return solde
    
def alea():
    return randrange(50)

def start(argent):
    num = choix()
    s = somme(argent)
    success_num = alea()

    if(success_num == num):
        print(f"Vous avez eu le numéro gagnant qui est {success_num}! Félicitation")
        argent = success(s, 3, argent)
        if(continuer(argent)):
            start(argent)
        else:
            print("Merci d'avoir jouer")
        

    elif(parite(num) == parite(success_num)):
        print(f"Vous n'avez pas eu le numéro gagnant qui est {success_num}, mais vous avez la meme couleur que ce dernier")
        argent = success(s, 2, argent)
        if(continuer(argent)):
            start(argent)
        else:
            print("Merci d'avoir jouer")

    else:
        print(f"Désolé, le numéro gagnant est {success_num} vous avez perdu :( ")
        argent = failed(s, argent)
        if(continuer(argent)):
            start(argent)
        else:
            print("Merci d'avoir jouer")


argent = argent_total()
start(argent)

os.system("pause")
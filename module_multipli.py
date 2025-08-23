"""Module de multiplication"""
import os

def table(nbr, max=10):
    if max <= 0:
        print("Paramètre invalide!")
        return
    for i in range(max + 1):
        print(f"{nbr} * {i} = {nbr * i}")

def chaine(max=10):
    if max <= 0:
        print("Paramètre invalide!")
        return
    for i in range(max + 1):
        print(f"{i} * {i} = {i * i}")

#testons la fonction table pour voir
if __name__ == "__main__":
    nbr = int(input("Entrez un nombre : "))
    print("Sa table de multiplication est :\n")
    table(nbr, 12)
    os.system("pause")

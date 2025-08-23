# -*-coding:Latin-1 -*
import os

a = input("Entrez une année : ")

a = int(a)
    
bissextile = False

if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
    bissextile = True

if bissextile:
    print(f"L'année {a} est bissextile.")
else:
    print(f"L'année {a} n'est pas bissextile.")

os.system("pause")
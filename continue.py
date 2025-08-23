i = 0

while i < 20:
    if (i % 3 == 0):
        i += 4
        print(f"On incrémente i de 4 et on obtient {i}")
        continue #on retourne au debut, sans exécute la suite du code
    print(f"La variable i est de : {i}")
    i += 1
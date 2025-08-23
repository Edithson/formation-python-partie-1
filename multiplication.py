nbr = int(input("Entrez un nombre : "))

print("Sa table de multiplication est :\n")

max = 12

def multiplication(nbr, max=10):
    if max <= 0:
        print("Paramètre invalide!")
        return
    for i in range(max + 1):
        print(f"{nbr} * {i} = {nbr * i}")

    """Voici la donc de la foncion"""
# i = 0
# while i <= max:
#     print(f"{nbr} * {i} = {nbr*i}")
#     i+=1

multiplication(nbr, max)
def Niveau1():
    print("Bienvenue sur le célèbre jeu du juste prix, tu dois deviner le prix auquel je pense, il se situe entre 1 et 100")
    import random
    x = 14
    nombre_choisi = random.randint(1,100)
    nombre = int(input("Entrez une proposition : "))
    if (nombre < nombre_choisi):
        print("C'est plus")
    if (nombre == nombre_choisi):
        print("C'est ça")
    if (nombre > nombre_choisi):
        print("C'est moins")

if __name__ == '__main__':
    Niveau1()
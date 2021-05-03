A FINIR !

def wait():
    import time
    time.sleep(5)


def Niveau2():
    print("Bienvenue sur le célèbre jeu du juste prix, tu dois deviner le prix auquel je pense, il se situe entre 1 et 100")
    import random
    nombre_choisi = random.randint(1,10)
    n=0
    wait()
    while(wait()):
        while(n<=4):
            nombre = int(input("Entrez une proposition : "))
            if (nombre < nombre_choisi):
                print("C'est plus")
                n=n+1
            if (nombre > nombre_choisi):
                print("C'est moins")
                n=n+1
            if (nombre == nombre_choisi):
                print("C'est ça")
                print("Gagné")
                break

        if (nombre_choisi < nombre):
            print("Perdu")
        if (nombre_choisi > nombre):
            print("Perdu")
    print("Trop tard !")

if __name__ == '__main__':
    Niveau2()

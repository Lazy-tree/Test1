import random as rnd
import time as t

argent_initial = rnd.randint(500, 3001)

def affichage(r, num, m):
    t.sleep(0.5)
    for _ in range(3):
        print(".")  
        t.sleep(0.1)
    print("...?")
    t.sleep(0.7)


    rep = [
        ["DING! DING! DING!", "Domage!", "WOMP WOMP..."],
        [f"C'était le {num}!!!", f"C'était le {num}", f"C'était le {num}..."],
        [f"Vous avez une remise de {m*3} € !!!\n", f"Vous avez une remise de {m*0.5} €\n", f"Vous avez perdu {-m} € ...\n"],
        [3, 0.5, 0]
    ]

    if r == 0 or rnd.randrange(0, 100)<20:
        print("?!")
        t.sleep(0.7)
        print("!!!!!!!!!!!")
        t.sleep(0.7)
    
    print(rep[0][r])
    print(rep[1][r])
    t.sleep(1)
    print(rep[2][r])
    return m*rep[3][r]


def roulette(mise):
    numero = rnd.randrange(0, 50)
    print(numero)
    couleur = numero%2
    # pari = int(input("Sur quel numéro (0 à 49) pariez vous ? :  "))

    pari = -1
    while pari not in range(50):
        try:
            pari = int(input("Sur quel numéro (0 à 49) pariez vous ? :  "))
            if pari in range(50):
                break
            else:
                raise ValueError
        except ValueError:
            print("Veuillez entrer 0 ou 49.")


    if pari == numero:
        res = 0
    elif pari%2 == couleur:
        res = 1
    else:
        res = 2
    
    print(f"Mise de {mise} € pour le numéro {pari}")
    return affichage(res, numero, mise)

def partie(argent):
    bTotal, aMax, nbPartie= 0, argent, 1
    print("\n\nBienvenue au ZCasino")
    t.sleep(1)
    continuer = 1

    print(f"Vous avez {argent} €")
    t.sleep(2)
    while continuer == 1:
        print(f"\n\nPartie {nbPartie}:")
        nbPartie += 1
        # bMise = False
        # while not bMise:
        #     mise_partie = int(input("\n\nQuelle somme souhaitez-vous miser ? :  "))
        #     bMise = mise_partie <= argent
        #     if not bMise:
        #         print("Argent insuffisant")
        while True:
            try:
                mise_partie = int(input("Quelle somme souhaitez-vous miser ? : "))
                if 0 < mise_partie <= argent:
                    break
                print("Mise invalide ou argent insuffisant.")
            except ValueError:
                print("\nVeuillez entrer un entier valide.")

        benefice_partie = roulette(mise_partie)
        t.sleep(1)
        argent += benefice_partie - mise_partie

        if argent > aMax:
            print("Vous avez atteint un nouveau maximum")
            t.sleep(0.5)
            aMax = argent
        if benefice_partie > 0:
            bTotal += benefice_partie
        
        if argent <= 0:
            print("Banqueroute!!!!")
            t.sleep(1)
            break
        
        # continuer = -1
        # while continuer not in range(0, 2):
        #    try:
        #        continuer = int(input(f"Vous avez {argent} €, souhaitez vous continuer ? (1 = oui, 0 = non) : "))
        #    except ValueError:
        #        print("Veuillez entrer 0 ou 1.")

        while True:
            try:
                continuer = int(input(f"Vous avez {argent} €, souhaitez vous continuer ? (1 = oui, 0 = non) : "))
                if continuer in range(0, 2):
                    break
                else:
                    raise ValueError
            except ValueError:
                print("\nVeuillez entrer 0 ou 1.")                

        #     continuer = input(f"Vous avez {argent} €, souhaitez vous continuer ? (1 si oui, 0 si non) :  ") == "1"
        # # if not continuer:
        #     # break
    
    print(f"\n\nD'un finnancement d'origne de {argent} €, vous avez gagné au total {bTotal} € et atteint un maximum de {aMax} €\n")
    t.sleep(0.7)
    print("Merci de vore viste chez ZCasino. Bonne journée!\n\n\n")
    t.sleep(2)

partie(argent_initial)

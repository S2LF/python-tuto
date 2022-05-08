import random
import sys

nb_mys = random.randint(1, 100)

left_try = 5
print("*** Le jeu du nombre mystère ***")
while left_try > 0 :
    try_text = print(f"Il vous reste {left_try} essai{'s' if left_try > 1 else ''} 🤞")
    trial = input('👉  Devinez le nombre mystère : ')
    if trial.isdigit() :
        trial = int(trial)
        if trial == nb_mys:
            print('Bravo ! 🏆 Vous avez trouvé le nombre mystère ! 🎉🎉🎉')
            print(f"Vous avez trouvé en {6-left_try} essai{'s' if left_try > 1 else ''} 😎")
            print('Fin du jeu.')    
            sys.exit()
        else:
            left_try -= 1
            if left_try == 0:
                print('👎 Vous avez perdu ! 😢')
                print(f'Le nombre mystère était : {nb_mys}')
                print('Fin du jeu.')
                sys.exit()
            if trial > nb_mys:
                print(f'C\'est moins que {trial} !')
            else:
                print(f'C\'est plus que {trial} !')
    else :
        print('Veuillez entrer un nombre valide. 😉')

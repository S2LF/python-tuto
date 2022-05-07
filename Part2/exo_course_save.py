import os
import sys
import json

chemin = r"C:\laragon\www\python\Part2\Fichiers\courses.json"

CUR_DIR = os.path.dirname(__file__)
LISTE_PATH = os.path.join(CUR_DIR, "Fichiers", "courses.json")

if os.path.exists(LISTE_PATH):
    # Ouverture du fichier en mode lecture
    with open(chemin, "r", encoding='utf-8') as f:
        liste = json.load(f)
else :
    liste = []

choice = 0

while choice != 5 :
     print('')
     print('Choisissez parmi les 5 options suivantes :')
     print('1: Ajouter un élément à la liste')
     print('2: Retirer un élément de la liste')
     print('3: Afficher la liste')
     print('4: Vider la liste')
     print('5: Quitter')
     print('')
     choice = input('\U0001F449  Votre choix : ')

     if choice.isdigit():
        if int(choice) == 1 :
            addElement = input("Entrez le nom de l'élément à ajouter à la liste de course : ")
            liste.append(addElement)
            print(f"L'élément {addElement} a bien été ajouté à la liste")
        elif int(choice) == 2 :
            removeElement = input("Entrez le nom de l'élément à retirer de la liste de course : ")
            if not removeElement in liste :
                    print(f"L'élément {removeElement} n'est pas dans la liste")
            else :
                liste.remove(removeElement)
                print(f"L'élément {removeElement} a bien été retiré de la liste")
        elif int(choice) == 3 :
            print('Voici le contenu de votre liste :')
            if len(liste) == 0 :
                    print('Votre liste est vide')
            else :
                for i, el in enumerate(liste, 1) :
                    print(f'{i}. {el}')
        elif int(choice) == 4 :
            liste.clear()
            print('La liste de course a bien été vidé')
        elif int(choice) == 5 :
            print('')
            print('À bientôt !')
            # Ouverture du fichier en mode écriture (écrase le fichier)
            with open(LISTE_PATH, "w", encoding='utf-8') as f:
                json.dump(liste, f, indent=4)
            sys.exit()
        else :
            print('Veuillez choisir un choix existant.')
     else :
        print('Veuillez choisir un choix existant.')

     print('')
     print('-' *50)
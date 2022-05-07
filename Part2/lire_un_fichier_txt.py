chemin = r"C:\laragon\www\python\Part2\Fichiers\fichier.txt"

# Ouverture du fichier en mode lecture
with open(chemin, "r", encoding='utf-8') as f:
    # contenu1 = f.read() # retour à la ligne interprété
    # contenu2 = repr(f.read()) # retour à la ligne non interprété
    # contenu = f.readlines() # met le contenu dans une liste met /n à la fin
    contenu = f.read().splitlines() # met le contenu dans une liste 
    print(contenu)


# Ouverture du fichier en mode écriture (écrase le fichier)
# with open(chemin, "w", encoding='utf-8') as f:
#     f.write("Ceci est un fichier écrit en Python")

# Ouverture du fichier en mode écriture (ajoute à la fin du fichier)
with open(chemin, "a", encoding='utf-8') as f:
    f.write("\nCeci est un fichier écrit en Python")

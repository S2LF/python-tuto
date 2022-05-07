import json

chemin = r"C:\laragon\www\python\Part2\Fichiers\fichier.json"

# Ouverture du fichier en mode lecture
with open(chemin, "r", encoding='utf-8') as f:
    liste = json.load(f)
    print(type(liste))
    print(liste)

liste.append(4)

# Ouverture du fichier en mode écriture (écrase le fichier)
with open(chemin, "w", encoding='utf-8') as f:
    json.dump(liste, f, indent=4)
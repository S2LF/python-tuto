from pathlib import Path
import re

inFile = Path("C:\\laragon\\www\\python\\Part2\\Fichiers\\nom_bordel.txt")
outDir = Path("C:\\laragon\\www\\python\\Part2\\Fichiers")

liste_alpha = []

with open(inFile, "r", encoding='utf-8') as f:
    liste = f.read()
    liste2 = re.split(r"\n|, | |  ", liste)
    for prenom in liste2:
        prenom2 = prenom.strip()
        if prenom2 != "":
            liste_alpha.append(prenom2)
    liste_alpha.sort()
print(liste_alpha)


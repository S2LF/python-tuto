# C:\laragon\www\python\Part2\Fichiers\file_error\readme.txt
# C:\laragon\www\python\Part2\Fichiers\file_error\fichier_invalide.abc

chemin = input('Entrez le chemin du fichier à lire : ')

try :
    with open(chemin, "r", encoding='utf-8') as f:
        contenu = f.read()

except FileNotFoundError :
    print("Fichier introuvable")
except UnicodeDecodeError:
    print("Impossible d'ouvrir le fichier.")
else :
    print(contenu)


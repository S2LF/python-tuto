from pathlib import Path
import shutil

#  Dossier User
print(Path().home())

# Dossier courant (current sorking diretory)
print(Path().cwd())

p = Path("C:\\laragon\\www\\python\\Part2\\Fichiers")
print (p)

# Récupérer le dossier parent
print (p.parent)

home = Path.home()
print(home)

print(home / "Part2" / "Fichiers")

print(home.joinpath("Part2", "Fichiers", "fichier.txt"))

print(home.joinpath("Part2", "Fichiers", "fichier.txt").suffix)

print(home.joinpath("Part2", "Fichiers", "fichier.txt").name)
print(home.joinpath("Part2", "Fichiers", "fichier.txt").parent)
print(home.joinpath("Part2", "Fichiers", "fichier.txt").stem)
print(home.joinpath("Part2", "Fichiers", "fichier.txt").suffix)
print(home.joinpath("Part2", "Fichiers", "fichier.txt").suffixes)
print(home.joinpath("Part2", "Fichiers", "fichier.txt").exists())
print(home.joinpath("Part2", "Fichiers", "fichier.txt").is_dir())
print(Path().home().parent.parent.joinpath("laragon", "www", "python", "Part2", "Fichiers", "fichier.txt").is_file())

dossier = Path("C:\\laragon\\www\\python\\Part2\\Dossier_test")

# Créer un dossier
dossier.mkdir(exist_ok=True)

# Création d'une arborescence de dossiers
dossier.joinpath("1", "2", "3").mkdir(parents=True, exist_ok=True)

# Création / Suppression de fichiers
dossier.joinpath("readme.txt").touch()
dossier.joinpath("readme.txt").unlink()

# Pas possible de supprimer plusieurs dossier (car pas vide)
# dossier.joinpath("1", "2").rmdir()

shutil.rmtree(dossier.joinpath("1"))


# Lire & écrire dans un fichier
dossier.joinpath("readme.txt").touch()
dossier.joinpath("readme.txt").write_text("Hello World !")
print(dossier.joinpath("readme.txt").read_text())

# Scanner un dossier
for f in Path().home().iterdir():
    home_dirs = [f for f in Path().home().iterdir() if f.is_dir()]
    print(home_dirs)

p = Path("C:\\laragon\\www\\python")

# Afficher tout les fichiers d'un dossier rglob pour le recursif
for f in p.joinpath("Part1").glob("*.py"):
    print(f.name)

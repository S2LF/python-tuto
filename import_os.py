import os

chemin = "C:/laragon/www/python"

dossier = os.path.join(chemin, "dossier", "test")

# création de dossiers
os.makedirs(dossier, exist_ok=True)

# suppression de dossiers
# if os.path.exists(dossier):
#     os.removedirs(dossier)




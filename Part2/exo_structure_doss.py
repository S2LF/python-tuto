from pathlib import Path

d = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]}

path = Path("C:\\laragon\\www\\python\\Part2\\Fichiers\\arborescence")

for key, item in d.items():
    for i in item:
        Path(path.joinpath(key, i)).mkdir(exist_ok=True, parents=True)
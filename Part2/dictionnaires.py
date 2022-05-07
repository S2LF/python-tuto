films = {
    "Le Seigneur des Anneaux" : 12,
    "Harry Potter" : 9,
    "Blade Runner" : 7.5
}

prix = 0

for f in films:
    prix += films[f]

print(str(prix) + "€")

d = {
    "prenom" : "John",
    "nom" : "Doe",
    "profession": "Ingénieur",
    "age" : 42
}

# supprimer clé
if "age" in d:
    del d["age"]

print(d)

print(d.items())
for cle, valeur in d.items():
    print(cle, valeur)
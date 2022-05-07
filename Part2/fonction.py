def nom_de_la_fonction():
    print("Ceci est une fonction")
    return "Ceci est un exemple de fonction"

print(nom_de_la_fonction())

def fonction_avec_parametre(parametre):
    print("Ceci est une fonction avec un paramètre :", parametre)

fonction_avec_parametre('blablabla')


def multiplicateur_mot(mot, mult=5):
	return mot * mult

mot_multiplie = multiplicateur_mot(mot="Bonjour")
print(mot_multiplie)

def add(a: int, b: int) -> int:
    return int(a + b)

print(add(5, 10))
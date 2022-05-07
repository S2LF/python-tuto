a = 5
b = 10
# b = 0

try:
    result = a/b
except ZeroDivisionError:
    print("Division par zéro impossible.")
except TypeError:
    print("La variable b n'est pas du bon type.")
except NameError as e:
    print("La variable b n'existe pas.")
    print("Erreur :", e)
else:
    print("Le résultat est :", result)
from os import remove


liste = []

print(liste)


liste.append(1)
liste.extend([2, 3, 4, 5])

print(liste)
# Le 5eme element de la liste est le 4eme element de la liste 
print(liste[4])
# Le dernier (dernier index)
print(liste[-1])
# Les 2 premiers (0 et 1)
print(liste[0:2])
# Un sur 2 en partant du début
print(liste[::2])
# Un sur 2 en partant du 1er
print(liste[1::2])
# inversé la liste
print(liste[::-1])
liste.remove(5)
print(liste)

liste.clear()
print(liste)

employes = ['Carlos', "Max", "Jean", "Pierre", "Paul", "Jacques", "Max"]

resultat = employes.index("Max")

print(resultat)
print(employes.count("Max"))

sorte = sorted(employes)
print(sorte)

employes.reverse()
print(employes)

element = employes.pop(-1)
print(element)
print(employes)

join = " ".join(employes)
print(join)

courses = "Riz, Steack, Pate, Oignon, Tomate, Sauce, Pomme"
courses = courses.split(", ")
print(courses)

print('Riz' in courses)
print('Riz' not in courses)

if 'Pomme' in courses:
    courses.remove('Pomme')

print(courses)
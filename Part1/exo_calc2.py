a = b = ""

while not (a.isdigit() and b.isdigit()):
    a = input("Entrez un premier nombre : ")
    b = input("Entrez un deuxième nombre : ")
    if not a.isdigit() and b.isdigit():
        print("Veuillez entrer deux nombres valides")

print(f"Le résultat de l'addition de {a} avec {b} est égal à {int(a) + int(b)}")
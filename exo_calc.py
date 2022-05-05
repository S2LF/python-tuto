n1 = input('Entrez un premier nombre : ')

if not n1.isdigit():
    print('Veuillez entrer un nombre')
    n1 = input('Entrez un premier nombre : ')

n2 = input('Entrez un deuxième nombre : ')

if not n2.isdigit():
    print('Veuillez entrer un nombre')
    n2 = input('Entrez un deuxième nombre : ')

print(f"Le résultat de l'addition de {n1} avec {n2} est égal à {int(n1) + int(n2)}")
a = "J'ai une classe de " + str(30) + " élèves"
b = str(10) + " + 5 est égal à " + str(10 + 5)
c = 10 + int(5)
d = "J'ai " + str(31) + " ans"


print(a)
print(b)
print(c)
print(d)

# nombre = input("Entrez un nombre: ")
# print(nombre)

print("Bonjour".upper())
print("Bonjour".lower())
print("Bonjour tout le monde".capitalize())
print("bonjour tout le monde".title())
print("Bonjour".swapcase())
print("Bonjour".replace("jour", "soir"))
print("   bonjour   ".strip())
print("bon jour".strip())
print("bonjour".strip(" ujor"))

print("   bonjour   ".rstrip())
print("   bonjour   ".lstrip())

print("1, 2, 3, 4, 5".split(", "))
print(", ".join(['1', '2', '3', '4', '5']))

print("9".zfill(2))

# for i in range(1, 15):
#     print(str(i).zfill(2))

print("bonjour".islower())
print('bonjour'.isupper())

print('50'.isdigit())
print('50a'.isdigit())

name = "Sylvain"
age = 31
print(f"Bonjour {name}, tu as {age}ans")

if age >= 18:
    majeur = True
else:
    majeur = False

majeur = True if age >= 18 else False

print(f"Bonjour {name}, tu as {age}ans. Tu es majeur: {majeur}")
class Vehicule:
    def avance(self):
        print("Le véhicule avance.")

class Voiture(Vehicule):
    def avance(self):
        super().avance()
        print("La voiture roule.")

class Avion(Vehicule):
    def avance(self):
        super().avance()
        print("L'avion vol.")

v = Voiture()
a = Avion()

print(v.avance())
print(a.avance())
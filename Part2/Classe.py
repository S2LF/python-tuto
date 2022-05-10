class Voiture:
    voiture_crees = 0
    def __init__(self, marque, modele, couleur):
        Voiture.voiture_crees += 1
        self.marque = marque
        self.modele = modele
        self.couleur = couleur


    # methode de classe
    @classmethod
    def lamborghni(cls):
        return cls("Lamborghini", "Aventador", "rouge")
    
    @classmethod
    def ferrari(cls):
        return cls("Ferrari", "F12", "rouge")

    # methode statique
    @staticmethod
    def afficher_nombre_voitures():
        print(f"Il y a {Voiture.voiture_crees} voitures dans votre garage.")

    def __str__(self) -> str:
        return (f"Voiture de marque {self.marque}, modèle {self.modele} et de couleur {self.couleur}.")

voiture1 = Voiture("Renault", "Clio", "Blanc")
print(voiture1.marque, voiture1.modele, voiture1.couleur)

lambo = Voiture.lamborghni()
ferrari = Voiture.ferrari()

print(lambo.marque)
print(Voiture.afficher_nombre_voitures())

affichage = str(voiture1)
print(affichage)
print(voiture1)
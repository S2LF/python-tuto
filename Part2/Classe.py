class Voiture:

    def __init__(self, marque, modele, couleur):
        self.marque = marque
        self.modele = modele
        self.couleur = couleur


voiture1 = Voiture("Renault", "Clio", "Blanc")
print(voiture1.marque, voiture1.modele, voiture1.couleur)
projets = ["pr_GameOfThrones", "HarryPotter", "pr_Avengers"]

class Utilisateur:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def __str__(self) -> str:
        return f"Utilsateur {self.nom} {self.prenom}"

    def afficher_projet(self):
        for projet in projets:
            print(f" - {projet}")

class Junior(Utilisateur):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)

    def afficher_projet(self):
        for projet in projets:
            if not projet.startswith("pr_"):
                print(f" - {projet}")

paul = Junior("Paul", "Dupont")
paul.afficher_projet()
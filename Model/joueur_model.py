
class Joueur:
    def __init__(self, nom, prenom, date_de_naissance, sexe, classement, points=0):
        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.sexe = sexe
        self.classement = classement
        self.points = points

    def __repr__(self):
        return f"{self.prenom} {self.nom}"

    def gagne(self):
        self.points += 1

    def egalite(self):
        self.points += 0.5

    def perd(self):
        self.points += 0
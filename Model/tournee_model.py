class Tournee:
    def __init__(self, nom, liste_matchs):
        self.nom = nom
        self.liste_matchs = liste_matchs

    def __repr__(self):
        return self.nom

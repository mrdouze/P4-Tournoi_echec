class Tournee:
    def __init__(self, nom, date_tournee, liste_matchs):
        self.nom = nom
        self.date_tournee = date_tournee
        self.liste_matchs = liste_matchs

    def __repr__(self):
        return self.nom

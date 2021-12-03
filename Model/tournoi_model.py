from model.tournee_model import Tournee

class Tournoi:
    def __init__(self, nom, lieu, date, controle_de_temps, description, nombre_de_tour=4, tournees=None, joueurs=None):
        if tournees is None:
            tournees = list()
        if joueurs is None:
            joueurs = list()
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.nombre_de_tour = nombre_de_tour
        self.tournees = tournees
        self.joueurs = joueurs
        self.controle_de_temps = controle_de_temps
        self.description = description

    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)

    @classmethod
    def generer_paires_tour1(cls, liste_joueur):
        """
        récupère une liste de joueurs et renvoie une liste de paires basée sur le classement
        :param liste_joueur:
        :return:
        """
        # premiere tournee du tournoi#
        liste_joueur = sorted(liste_joueur, key=lambda j: j.classement, reverse=True)
        moitie = len(liste_joueur) // 2
        moitie_superieur = liste_joueur[moitie:]
        moitie_inferieure = liste_joueur[:moitie]
        paires_tour1 = list(zip(moitie_superieur, moitie_inferieure))
        return paires_tour1

    @classmethod
    def generer_paires_autes_tours(cls, liste_joueur):
        """
        recupere une liste de joueur et renvoie une liste de paires basée sur le nombre de points gagnés dans le tournoi
        :param liste_joueur:
        :return:
        """
        return cls.generer_paires_tour1(liste_joueur)
        # pour les tournee de 2 a 4
        compteur_tour = 0
        paires_autres_tours = []
        joueur_1 = 0
        joueur_2 = 1
        liste_joueur = sorted(liste_joueur, key=lambda i: i.points)

        while compteur_tour < 4:
            ##
            # implémenter un test si paires deja jouees
            ##
            paires_autres_tours = (liste_joueur[joueur_1], liste_joueur[joueur_2])
            paires_autres_tours.append(paires_autres_tours)
            joueur_1 += 2
            joueur_2 += 2
            compteur_tour += 1

        return paires_autres_tours

    def generate_first_round(self):
        liste_paires = self.generer_paires_tour1(self.joueurs)
        tournee = Tournee("Tournee 1", liste_paires)
        self.tournees.append(tournee)
        return tournee

    def generate_others_rounds(self):
        liste_paires = self.generer_paires_autes_tours(self.joueurs)
        tournee = Tournee("Tournee " + str(len(self.tournees) + 1), liste_paires)
        self.tournees.append(tournee)
        return tournee

    def generer_prochaine_tournee(self):
        nb_tournees = len(self.tournees)
        if nb_tournees == 0:
            return self.generate_first_round()
        elif nb_tournees >= self.nombre_de_tour:
            return None
        else:
            return self.generate_others_rounds()

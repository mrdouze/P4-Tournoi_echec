from model.tournee_model import Tournee
import datetime


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

    def __repr__(self):
        return f"{self.nom} {self.date}"

    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)
        return

    def classement_par_rang(self):
        return sorted(self.joueurs, key=lambda j: j.classement, reverse=True)

    def generer_paires_tour1(self):
        """
        genere des pairs sur un critère de classement
        :return:
        """
        liste_joueur = self.classement_par_rang()
        moitie = len(liste_joueur) // 2
        moitie_superieur = liste_joueur[moitie:]
        moitie_inferieure = liste_joueur[:moitie]
        paires_tour1 = list(zip(moitie_superieur, moitie_inferieure))
        return paires_tour1

    def classement_par_points(self):
        return sorted(self.joueurs, key=lambda i: (i.points, i.classement), reverse=True)

    def ont_deja_joues(self, joueur1, joueur2):
        """
        chercher dans l'historique des matchs si cette paire existe
        :param joueur1:
        :param joueur2:
        :return:
        """
        for tournee in self.tournees:
            for match in tournee.liste_matchs:
                if match[0] == joueur1 and match[1] == joueur2:
                    return True
                if match[0] == joueur2 and match[1] == joueur1:
                    return True
        return False

    def trouve_adversaire(self, joueur, candidats):
        """
        trouver un joueur parmis la liste des candidats qui n'a jamais joué avec le prmeier joueur
        :param joueur:
        :param candidats:
        :return:
        """
        for candidat in candidats:
            if not self.ont_deja_joues(candidat, joueur):
                return candidat
        return candidats[0]

    def generer_paires_autes_tours(self):
        """
        générer les paires de joueurs pour les tours autre que le premier
        :return:
        """

        liste_joueurs = self.classement_par_points()
        list_matchs = list()
        while len(liste_joueurs) > 1:
            premier_joueur = liste_joueurs.pop(0)
            deuxieme_joueur = self.trouve_adversaire(premier_joueur, liste_joueurs)
            liste_joueurs.remove(deuxieme_joueur)
            list_matchs.append([premier_joueur, deuxieme_joueur])
        return list_matchs

    def generate_first_round(self):
        liste_paires = self.generer_paires_tour1()
        tournee = Tournee("Tournee 1", datetime.date, liste_paires)
        self.tournees.append(tournee)
        return tournee

    def generate_others_rounds(self):
        liste_paires = self.generer_paires_autes_tours()
        tournee = Tournee("Tournee " + str(len(self.tournees) + 1), datetime.date, liste_paires)
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

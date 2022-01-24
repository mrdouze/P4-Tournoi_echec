import controller.main_controller
from model.joueur_model import Joueur
from model.tournoi_model import Tournoi
from view.joueur_view import JoueurView
from view.tournoi_view import TournoiView
from view.tournee_view import TourneeView
from controller.database_controller import Database
import random


class GenererTournoi:
    @classmethod
    def lancer_tournoi(cls):
        tournoi = cls.creation_tournoi()
        cls.lancer_les_tournees(tournoi)

    @classmethod
    def creation_tournoi(cls):
        # TODO: partie ci dessous a retirer
        reponse = input('voulez vous utiliser le tournoi par defaut o/n? ')
        if reponse == 'o':
            nom_du_tournoi = 'tournoi numéro:' + str(random.randrange(1, 10000))
            date_tournoi = str(random.randrange(1, 30)) + "/" + str(random.randrange(1, 12)) + "/" + str(
                random.randrange(1960, 2010))
            tournoi = Tournoi(
                nom_du_tournoi,
                "Paris",
                date_tournoi,
                "bullet",
                "Description du tournoi !"
            )
            joueur = Joueur('Cassin', 'Marc', '19/12/90', 'm', '8', 0)
            tournoi.ajouter_joueur(joueur)
            joueur_serialise = Database.serialiser_joueur(joueur)
            Database.inserer_joueur(joueur_serialise)
            joueur = Joueur('Duff', 'John', '12/04/78', 'm', '7', 0)
            tournoi.ajouter_joueur(joueur)
            joueur_serialise = Database.serialiser_joueur(joueur)
            Database.inserer_joueur(joueur_serialise)
            joueur = Joueur('Zeblouse', 'Agathe', '12/12/89', 'f', '6', 0)
            tournoi.ajouter_joueur(joueur)
            joueur_serialise = Database.serialiser_joueur(joueur)
            Database.inserer_joueur(joueur_serialise)
            joueur = Joueur('Lacaisse', 'Alphonse', '06/04/78', 'm', '5', 0)
            tournoi.ajouter_joueur(joueur)
            joueur_serialise = Database.serialiser_joueur(joueur)
            Database.inserer_joueur(joueur_serialise)
            joueur = Joueur('Penflam', 'Kathy', '06/06/90', 'f', '4', 0)
            tournoi.ajouter_joueur(joueur)
            joueur_serialise = Database.serialiser_joueur(joueur)
            Database.inserer_joueur(joueur_serialise)
            joueur = Joueur('Honeth', 'Camille', '01/02/98', 'f', '3', 0)
            tournoi.ajouter_joueur(joueur)
            joueur_serialise = Database.serialiser_joueur(joueur)
            Database.inserer_joueur(joueur_serialise)
            joueur = Joueur('Fonfek', 'Sophie', '23/08/64', 'f', '2', 0)
            tournoi.ajouter_joueur(joueur)
            joueur_serialise = Database.serialiser_joueur(joueur)
            Database.inserer_joueur(joueur_serialise)
            joueur = Joueur('Celere', 'Jacques', '19/06/65', 'm', '1', 0)
            tournoi.ajouter_joueur(joueur)
            joueur_serialise = Database.serialiser_joueur(joueur)
            Database.inserer_joueur(joueur_serialise)
            tournoi_serialise = Database.serialiser_tournoi(tournoi)
            Database.inserer_tournoi(tournoi_serialise)

        else:
            info_tournoi = TournoiView.creer_tournoi()
            tournoi = Tournoi(
                nom=info_tournoi[0],
                lieu=info_tournoi[1],
                date=info_tournoi[2],
                nombre_de_tour=info_tournoi[3],
                controle_de_temps=info_tournoi[4],
                description=info_tournoi[5]
            )
            tournoi_serialise = Database.serialiser_tournoi(tournoi)
            Database.inserer_tournoi(tournoi_serialise)
            nb_joueurs = JoueurView.entrer_nb_joueur()

            for i in range(nb_joueurs):
                info_joueurs = JoueurView.recuperer_info_joueurs()
                joueur = Joueur(
                    nom=info_joueurs[0],
                    prenom=info_joueurs[1],
                    date_de_naissance=info_joueurs[2],
                    sexe=info_joueurs[3],
                    classement=info_joueurs[4],
                )

                tournoi.ajouter_joueur(joueur)
                joueur_serialise = Database.serialiser_joueur(joueur)
                Database.inserer_joueur(joueur_serialise)

        return tournoi

    @classmethod
    def lancer_les_tournees(cls, tournoi):
        """
        lance les tournées et attribue les points
        :param tournoi:
        :return:
        """
        for i in range(int(tournoi.nombre_de_tour)):
            print("lancement du round " + str(i + 1))
            tournee = tournoi.generer_prochaine_tournee()
            print('tournee ', tournee)
            for match in tournee.liste_matchs:
                reponse = TourneeView.entrer_score(match)
                if reponse == '1':
                    match[0].gagne()
                    match[1].perd()
                elif reponse == '2':
                    match[1].gagne()
                    match[0].perd()
                elif reponse == '3':
                    match[0].egalite()
                    match[1].egalite()
                else:
                    raise ValueError("mauvaise entrée")
                # tournoi_serialise = Database.serialiser_tournoi(tournoi)
                # Database.update_tournoi(tournoi_serialise)
            tournoi_serialise = Database.serialiser_tournoi(tournoi)
            Database.update_tournoi(tournoi_serialise)
            input('tapez entree pour tournee suivante ')
        controller.main_controller.MenuPrincipal.debut()

from model.joueur_model import Joueur
from model.tournoi_model import Tournoi
from view.joueur_view import JoueurView
from view.tournoi_view import TournoiView
from view.tournee_view import TourneeView


class GenererTournoi:
    @classmethod
    def lancer_tournoi(cls):
        tournoi = cls.creation_tournoi()
        cls.lancer_les_tournees(tournoi)

    @classmethod
    def creation_tournoi(cls):

        #TODO: partie ci dessous a retirer
        reponse = input ('voulez vous utiliser le tournoi par defaut o/n? ')
        if reponse == 'o':
            tournoi = Tournoi(
                "Tournoi par défaut",
                "Paris",
                "20-10-2022",
                "bullet",
                "Description du tournoi !"
            )
            tournoi.ajouter_joueur(Joueur('Cassin','Marc','19/12/90','m','8'))
            tournoi.ajouter_joueur(Joueur('Duff','John','12/04/78','m', '7'))
            tournoi.ajouter_joueur(Joueur('Zeblouse','Agathe','12/12/89','f','6'))
            tournoi.ajouter_joueur(Joueur('Lacaisse','Alphonse','06/04/78','m','5'))
            tournoi.ajouter_joueur(Joueur('Penflam','Kathy','06/06/90','f','4'))
            tournoi.ajouter_joueur(Joueur('Honeth','Camille','01/02/98','f','3'))
            tournoi.ajouter_joueur(Joueur('Fonfek','Sophie','23/08/64','f','2'))
            tournoi.ajouter_joueur(Joueur('Célère','Jacques','19/06/65','m','1'))
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

            nb_joueurs = JoueurView.entrer_nb_joueur()

            for i in range(nb_joueurs):
                info_joueurs = JoueurView.recuperer_info_joueurs()
                joueur = Joueur(
                    nom=info_joueurs[0],
                    prenom=info_joueurs[1],
                    date_de_naissance=[2],
                    sexe=[3],
                    classement=[4],
                    points=[5],
                )
                tournoi.ajouter_joueur(joueur)
                print(joueur)
        return tournoi

    @classmethod
    def lancer_les_tournees(cls, tournoi):
        for i in range(tournoi.nombre_de_tour):
            print("lancement du round" + str(i+1))
            tournee = tournoi.generer_prochaine_tournee()
            print('tournee ',tournee)
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
            print(tournoi.classement_par_points())
            input('tapez entree pour tournee suivante ')




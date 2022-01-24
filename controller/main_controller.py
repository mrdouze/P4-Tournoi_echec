from view.reporting_view import ReportingView
import sys
import os


from controller.tournoi_controller import GenererTournoi
from view.main_view import View
from view.tournoi_view import TournoiView


class MenuPrincipal:

    @classmethod
    def debut(cls):
        """
        gestion des entrées du menu principal
        :return:
        """
        menu_input = View.afficher_menu()
        if menu_input == "1":
            print('choix 1')
            GenererTournoi.lancer_tournoi()
        elif menu_input == "2":
            cls.reporting()
        elif menu_input == "3":
            print("Vous quittez le programme")
            os.system('clear')
            sys.exit()
            pass
        else:
            print("entree non valide")
            cls.debut()

    @classmethod
    def reporting(cls):
        """
        gestion des entrées du menu reporting
        :return:
        """
        menu_input = TournoiView.choix_reportings_tournois()
        if menu_input == "1":
            ReportingView.tri_joueur_alpha()
            cls.reporting()
        elif menu_input == "2":
            ReportingView.tri_joueur_classement()
            cls.reporting()
        elif menu_input == "3":
            index_tableau = ReportingView.tri_joueur_tournoi(menu_input)
            ReportingView.tri_joueur_tournoi(index_tableau)
            cls.reporting()
        elif menu_input == "4":
            index_tableau = ReportingView.tri_joueur_tournoi(menu_input)
            ReportingView.tri_joueur_tournoi(index_tableau)
            cls.reporting()
            pass
        elif menu_input == "5":
            ReportingView.reporting_liste_tournoi()
            cls.reporting()
        elif menu_input == "6":
            ReportingView.liste_tournees()
            cls.reporting()
        elif menu_input == "7":
            pass
        elif menu_input == "8":
            cls.debut()
        else:
            cls.reporting()

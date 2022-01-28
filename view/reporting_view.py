import pandas as pd
from controller.database_controller import Database
import controller.main_controller


pd.set_option('display.max_columns', None)


class ReportingView:
    @classmethod
    def tri_joueur_alpha(cls):
        """
        affichage table joueur en utilisant panda, tri alpha
        :return:
        """
        table_joueur = Database.database.table('table_joueur')
        vue_joueur_alpha = Database.extraire_joueur(table_joueur)
        tableau_joueur = pd.DataFrame(vue_joueur_alpha)
        tableau_joueur_alpha = tableau_joueur.sort_values(by='nom', key=lambda x: x.str.lower())
        print('---------------------------------------------')
        print('classement des joueurs par ordre alphabétique')
        print('---------------------------------------------')
        print(tableau_joueur_alpha)
        input('Appuyez sur une touche pour revenir à la selection')
        controller.main_controller.MenuPrincipal.reporting()

    @classmethod
    def tri_joueur_classement(cls):
        """
        affichage table joueur en utilisant panda, tri par le champs classement
        :return:
        """
        table_joueur = Database.database.table('table_joueur')
        vue_joueur_classement = Database.extraire_joueur(table_joueur)
        tableau_joueur = pd.DataFrame(vue_joueur_classement)
        tableau_joueur_classement = tableau_joueur.sort_values(by='classement')
        print('----------------------------------------------')
        print('classement des joueurs par ordre de classement')
        print('----------------------------------------------')
        print(tableau_joueur_classement)
        input('Appuyez sur une touche pour revenir à la selection')
        controller.main_controller.MenuPrincipal.reporting()

    @classmethod
    def reporting_liste_tournoi(cls):
        """
        option 5 du menu reporting, affichage de la liste des tournois triés par date
        :return:
        """
        table_tournoi = Database.database.table('table_tournoi')
        vue_tournois = Database.extraire_tournois(table_tournoi)
        tableau = pd.DataFrame(vue_tournois)
        tableau_liste_tournois = tableau.sort_values(by='date')
        print(tableau_liste_tournois)
        print('---------------------------------')
        print('liste des tournois triés par date')
        print('---------------------------------')
        # print(tableau_liste_tournois.style.hide_columns(['tournees', 'joueurs']))
        print(tableau_liste_tournois.drop(columns=['tournees', 'joueurs', 'description']))
        input('Appuyez sur une touche pour revenir à la selection')
        controller.main_controller.MenuPrincipal.reporting()

    @classmethod
    def tri_joueur_tournoi(cls, menu_input):
        """
        option 3 et 4 du menu reporting. affichage des joueurs d'un tournoi, tri en fonction de l'entrée du menu.
        :param menu_input:
        :return:
        """
        table_tournoi = Database.database.table('table_tournoi')
        vue_tournois = Database.extraire_tournois(table_tournoi)
        tableau = pd.DataFrame(vue_tournois)
        tableau_liste_tournois = tableau.sort_values(by='date')
        print('------------------')
        print('liste des tournois')
        print('------------------')
        print(tableau_liste_tournois.drop(columns=["tournees", "joueurs", "description"]))
        index_tournoi = input('selectionnez un tournoi :')
        liste_joueurs = tableau_liste_tournois.iloc[int(index_tournoi), 5]
        joueurs_a_trier = pd.DataFrame(liste_joueurs)
        if menu_input == '3':
            print(joueurs_a_trier.sort_values(by='nom'))
        elif menu_input == '4':
            print(joueurs_a_trier.sort_values(by='classement'))
        input('Appuyez sur une touche pour revenir à la selection')
        controller.main_controller.MenuPrincipal.reporting()

    @classmethod
    def liste_tournees(cls):
        """
        option 6 du menu reporting. affichage des tournées d'un tournoi
        :return:
        """
        table_tournoi = Database.database.table('table_tournoi')
        vue_tournois = Database.extraire_tournois(table_tournoi)
        tableau = pd.DataFrame(vue_tournois)
        tableau_liste_tournois = tableau.sort_values(by='date')
        print('------------------')
        print('liste des tournois')
        print('------------------')
        print(tableau_liste_tournois.drop(columns=["tournees", "joueurs", "description"]))
        index_tournoi = input('selectionnez un tournoi :')
        liste_tournees = tableau_liste_tournois.iloc[int(index_tournoi), 4]
        # reporting_tournees = pd.DataFrame(liste_tournees)
        for element in liste_tournees:
            reporting_tournees = pd.DataFrame(liste_tournees)
            print(reporting_tournees[element])
            for j in reporting_tournees:
                liste_match = pd.DataFrame(reporting_tournees)
                print(liste_match[j])

        input('Appuyez sur une touche pour revenir à la selection')
        controller.main_controller.MenuPrincipal.reporting()

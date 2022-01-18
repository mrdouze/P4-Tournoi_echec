import pandas as pd
import jinja2
from controller.database_controller import Database
pd.set_option('display.max_columns', None)


class ReportingView:
    @classmethod
    def tri_joueur_alpha(cls):
        table_joueur = Database.database.table('table_joueur')
        vue_joueur_alpha = Database.extraire_joueur(table_joueur)
        tableau_joueur = pd.DataFrame(vue_joueur_alpha)
        tableau_joueur_alpha = tableau_joueur.sort_values(by='nom', key=lambda x: x.str.lower())
        print('---------------------------------------------')
        print('classement des joueurs par ordre alphabétique')
        print('---------------------------------------------')
        print(tableau_joueur_alpha)
        input()

    @classmethod
    def tri_joueur_classement(cls):
        table_joueur = Database.database.table('table_joueur')
        vue_joueur_classement = Database.extraire_joueur(table_joueur)
        tableau_joueur = pd.DataFrame(vue_joueur_classement)
        tableau_joueur_classement = tableau_joueur.sort_values(by='classement')
        print('----------------------------------------------')
        print('classement des joueurs par ordre de classement')
        print('----------------------------------------------')
        print(tableau_joueur_classement)
        input()

    @classmethod
    def reporting_liste_tournoi(cls):
        table_tournoi = Database.database.table('table_tournoi')
        vue_tournois = Database.extraire_tournois(table_tournoi)
        tableau = pd.DataFrame(vue_tournois)
        tableau_liste_tournois = tableau.sort_values(by='date')
        print (tableau_liste_tournois)
        #tableau_liste_tournois = tableau.style.hide_columns(['tournees', 'joueurs'])
        print('---------------------------------')
        print('liste des tournois triés par date')
        print('---------------------------------')
        #print(tableau_liste_tournois.style.hide_columns(['tournees', 'joueurs']))
        print(tableau_liste_tournois.drop(columns=['tournees', 'joueurs']))
        input()

    @classmethod
    def tri_joueur_tournoi(cls):
        table_tournoi = Database.database.table('table_tournoi')
        vue_tournois = Database.extraire_tournois(table_tournoi)
        tableau = pd.DataFrame(vue_tournois)
        tableau_liste_tournois =tableau.sort_values(by='date')
        print('------------------')
        print('liste des tournois')
        print('------------------')
        print(tableau_liste_tournois.drop(columns=["tournees", "joueurs"]))
        index_tournoi = input('selectionnez un tournoi :')
        ligne_liste_joueurs = tableau_liste_tournois.iloc[int(index_tournoi)]
        print(ligne_liste_joueurs)
        return index_tournoi

    @classmethod
    def liste_joueurs_tournoi_alpha(cls, index_tournoi):
        table_tournoi = Database.database.table('table-tournoi')
        vue_tournoi = Database.extraire_tournois(table_tournoi)
        tableau = pd.DataFrame(vue_tournoi)
        tournoi = tableau.index.values
        print(vue_tournoi)
        input()

    @classmethod
    def liste_joueurs_tournoi_classement(cls, index_tournoi):
        table_tournoi = Database.database.table('table-tournoi')
        vue_tournoi = Database.extraire_tournois(table_tournoi)
        print(vue_tournoi)
        input()
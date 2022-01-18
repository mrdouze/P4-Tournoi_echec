from view.joueur_view import JoueurView
#from controller.tournoi_controller import GenererTournoi


class TournoiView:
    @staticmethod
    def creer_tournoi():
        info_tournoi = list()
        print("---------------------------------------")
        print("Création de tournoi")
        info_tournoi.append(input("nom :"))
        info_tournoi.append(input("lieu :"))
        info_tournoi.append(input("date jj/mm/aa:"))
        info_tournoi.append(input("nombre de tour :"))
        controle_de_temps = input("controle de temps a:bullet. b:blitz. c:coups rapide :")
        if controle_de_temps == "a":
            info_tournoi.append("bullet")
        elif controle_de_temps == "b":
            info_tournoi.append("blitz")
        elif controle_de_temps == "c":
            info_tournoi.append("coups rapide")
        else:
            info_tournoi.append(controle_de_temps)
        info_tournoi.append(input("description :"))
        return info_tournoi

    @staticmethod
    def choix_reportings_tournois():
        print("------------------------------------------------------")
        print('1-liste de tous les joueurs: alphabétique')
        print('2-liste de tous les joueurs: classement')
        print("3-liste de tous les joueurs d'un tournoi: alphabétique")
        print("4-liste de tous les joueurs d'un tournoi: classement")
        print("5-liste de tous les tournois")
        print("6-listes des tours d'un tournoi")
        print("7-listes des matchs d'un tournoi")
        print("8-revenir au menu principal")
        print("-------------------------------------------------------")
        return input('Entrez Votre Choix:')
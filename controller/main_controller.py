import sys
import os


from controller.tournoi_controller import GenererTournoi
from view.main_view import View


class MenuPrincipal:

    @classmethod
    def debut(cls):
        menu_input = View.afficher_menu()
        if menu_input == "1":
            print ('choix 1')
            GenererTournoi.lancer_tournoi()
        elif menu_input == "2":
            pass
        elif menu_input == "3":
            print ("Vous quittez le programme")
            os.system('clear')
            sys.exit()
            pass
        else:
            print("entree non valide")
            cls.debut()

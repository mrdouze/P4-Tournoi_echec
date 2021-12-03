

class View(object):
    @classmethod
    def afficher_menu(cls):
        print('----------------')
        print("1. Creer tournoi")
        print("2. Creer rapport")
        print("3. Quitter")
        print('----------------')
        return input('Entrez 1, 2 ou 3: ')

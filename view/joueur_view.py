class JoueurView:
    @classmethod
    def recuperer_info_joueurs(cls):
        info_joueurs = list()
        print('-----------------------------')

        print('recuperer informations joueurs:')
        info_joueurs.append(input('nom ='))
        info_joueurs.append(input('prenom ='))
        info_joueurs.append(input('date de naissance jjmmaa ='))
        info_joueurs.append(input('sexe m/f ='))
        # info_joueurs.append(input('classement ='))
        classement_joueur = input('classement =')
        while not classement_joueur.isdigit():
            classement_joueur = input('Classement (entier) = ')
        info_joueurs.append(classement_joueur)

        print('-----------------------------')
        return info_joueurs

    @classmethod
    def entrer_nb_joueur(cls):
        print('-------------------------------------')
        print('initialisation des joueurs du tournoi')
        print('-------------------------------------')

        nb_joueurs = int(input("combien de joueurs voulez-vous insérer ?"))
        return nb_joueurs

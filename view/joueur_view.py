class JoueurView:
    @classmethod
    def recuperer_info_joueurs(cls):
        info_joueurs = list()
        print('-----------------------------')

        print('recuperer informations joueurs:')
        info_joueurs.append(input('nom ='))
        info_joueurs.append(input('prenom ='))
        info_joueurs.append(input('date de naissance jj/mm/aa ='))
        info_joueurs.append(input('sexe m/f ='))
        info_joueurs.append(input('classement ='))

        print('-----------------------------')
        return info_joueurs

    @classmethod
    def entrer_nb_joueur(cls):
        print('-------------------------------------')
        print('initialisation des joueurs du tournoi')
        print('-------------------------------------')

        nb_joueurs = int(input("combien de joueurs voulez-vous insérer ?"))
        return nb_joueurs

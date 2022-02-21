class TourneeView:

    @staticmethod
    def creer_tournee():
        info_tournee = list()
        info_tournee.append = (input('nom tournée :'))
        info_tournee.append = input()

    @staticmethod
    def entrer_score(match):
        print("joueur 1: ", match[0].prenom, match[0].nom, "Cl :", match[0].classement, "Pts :", match[0].points)
        print("joueur 2: ", match[1].prenom, match[1].nom, "Cl :", match[1].classement, "Pts :", match[1].points)
        reponse = ""
        possible_values = "1", "2", "3"
        while reponse not in possible_values:
            reponse = input("joueur 1> 1,  joueur 2> 2, egalité> 3 :")
        return reponse

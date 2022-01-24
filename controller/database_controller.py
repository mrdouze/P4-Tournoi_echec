from tinydb import TinyDB, Query
from model.tournoi_model import Tournoi


class Database:
    database = TinyDB("./database/database_tournoi.json")

    @classmethod
    def serialiser_joueur(cls, joueur):
        """
        serialisation joueur pour table joueur
        :param joueur:
        :return:
        """
        joueur_serialise = {
            'nom': joueur.nom,
            'prenom': joueur.prenom,
            'date_de_naissance': joueur.date_de_naissance,
            'sexe': joueur.sexe,
            'classement': joueur.classement,
        }
        return joueur_serialise

    @classmethod
    def serialiser_joueur_pour_tournoi(cls, joueur):
        """
        serialisation des données joueurs pour objet tournoi
        :param joueur:
        :return:
        """
        joueur_serialise = {
            'nom': joueur.nom,
            'prenom': joueur.prenom,
            'date_de_naissance': joueur.date_de_naissance,
            'sexe': joueur.sexe,
            'classement': joueur.classement,
            'points': joueur.points
        }
        return joueur_serialise

    @classmethod
    def inserer_joueur(cls, joueur_serialise):
        """
        insérertin joueurs dans la table joueur
        :param joueur_serialise:
        :return:
        """
        table_joueur = cls.database.table('table_joueur')
        table_joueur.insert(joueur_serialise)
        return

    @classmethod
    def serialiser_liste_matchs(cls, liste_matchs):
        """
        sérialisation de la liste des matchs, pour le champs tournée.
        :param liste_matchs:
        :return:
        """
        liste_de_matchs_serialisee = {
            'joueur0': cls.serialiser_joueur_pour_tournoi(liste_matchs[0]),
            'joueur1': cls.serialiser_joueur_pour_tournoi(liste_matchs[1])
        }
        return liste_de_matchs_serialisee

    @classmethod
    def serialiser_tournees(cls, tournees):
        """
        serialisation des tournées pour la table tournoi.
        :param tournees:
        :return:
        """
        tournee_serialisee = {
            'nom': tournees.nom,
            'liste_matchs': [cls.serialiser_liste_matchs(m) for m in tournees.liste_matchs]
        }
        return tournee_serialisee

    @classmethod
    def update_tournoi(cls, tournoi):
        """
        MAJ du tournoi dans la table tournoi (dans tinydb)
        :param tournoi:
        :return:
        """
        table_tournoi = cls.database.table('table_tournoi')
        if type(tournoi) is Tournoi:
            serialized = cls.serialiser_tournoi(tournoi)
        else:
            serialized = tournoi
        table_tournoi.update({'tournees': serialized['tournees']}, Query().nom == serialized.get('nom'))
        table_tournoi.update({'joueurs': serialized['joueurs']}, Query().nom == serialized.get('nom'))

        return

    @classmethod
    def serialiser_tournoi(cls, tournoi):
        """
        serialisation des éléments de tournoi
        :param tournoi:
        :return:
        """
        tournoi_serialise = {
            'nom': tournoi.nom,
            'lieu': tournoi.lieu,
            'date': tournoi.date,
            'nombre_de_tours': tournoi.nombre_de_tour,
            'tournees': [cls.serialiser_tournees(t) for t in tournoi.tournees],
            'joueurs': [cls.serialiser_joueur_pour_tournoi(j) for j in tournoi.joueurs],
            'controle_de_temps': tournoi.controle_de_temps,
            'description': tournoi.description
        }
        return tournoi_serialise

    @classmethod
    def inserer_tournoi(cls, tournoi_serialise):
        """
        insertion dans la table tournoi
        :param tournoi_serialise:
        :return:
        """
        table_tournoi = cls.database.table('table_tournoi')
        table_tournoi.insert(tournoi_serialise)
        return

    @classmethod
    def extraire_joueur(cls, table_joueur):
        """
        extraction de la table joueur serialisé.
        :param table_joueur:
        :return:
        """
        joueurs_serialises = table_joueur.all()
        return joueurs_serialises


    @classmethod
    def extraire_tournois(cls, table_tournoi):
        """
        extraction de la table tournoi, sous forme serialisée
        :param table_tournoi:
        :return:
        """
        tournoi_serialise = table_tournoi.all()
        return tournoi_serialise

from tinydb import TinyDB, Query

from model.tournoi_model import Tournoi


class Database:
    database = TinyDB("./database/database_tournoi.json")

    @classmethod
    def serialiser_joueur(cls, joueur):
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
        table_joueur = cls.database.table('table_joueur')
        table_joueur.insert(joueur_serialise)
        return

    @classmethod
    def serialiser_liste_matchs(cls, liste_matchs):
        liste_de_matchs_serialisee = {
            'joueur0': liste_matchs[0],
            'joueur1': liste_matchs[1]
        }
        return liste_de_matchs_serialisee

    @classmethod
    def serialiser_tournees(cls, tournees):
        tournee_serialisee = {
            'nom': tournees.nom,
            'liste_matchs': [cls.serialiser_liste_matchs(m) for m in tournees.liste_matchs]
        }
        return tournee_serialisee

    @classmethod
    def update_tournoi(cls, tournoi):
        table_tournoi = cls.database.table('table_tournoi')
        if type(tournoi) is Tournoi:
            serialized = cls.serialiser_tournoi(tournoi)
        else:
            serialized = tournoi
        input('ERREUR !!!!')
        table_tournoi.upsert(serialized, Query().nom == serialized.get('nom'))
        return

    @classmethod
    def serialiser_tournoi(cls, tournoi):
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
        table_tournoi = cls.database.table('table_tournoi')
        table_tournoi.insert(tournoi_serialise)
        return

    @classmethod
    def extraire_joueur(cls, table_joueur):
        joueurs_serialises = table_joueur.all()
        return joueurs_serialises

    # @classmethod
    # def reporting_tournoi_joueur(cls, index_tableau):
    #     liste_joueurs = []
    #     requete = Query()
    #     table_tournoi = cls.database.table('table_tournoi')
    #     tournoi_serialise = cls.extraire_tournois(table_tournoi)
    #
    #     return liste_joueurs

    @classmethod
    def extraire_tournois(cls, table_tournoi):
        tournoi_serialise = table_tournoi.all()
        return tournoi_serialise

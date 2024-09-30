from datetime import datetime

from models.match import Match
from utils.constants import *
from utils.input_validator import InputValidator
from views.tournaments_views import TournamentsViews
from models.tournament import Tournament
from models.round import Round


class TournamentManager:
    def __init__(self, menu_manager):
        self.menu_manager = menu_manager
        self.data = INPUTS_TOURNAMENT

    def create_tournament(self):
        tournaments_views = TournamentsViews()

        # Affichage et récupération des inputs de la vue
        self.data = tournaments_views.view_create(self.data)

        # Validation de ses données
        self.data = InputValidator(self.data).validate()


        # Vérification que tous les input_data['valid'] soit True
        if all(input_data['valid'] for input_data in self.data):
            tournament_class = Tournament()
            response = tournament_class.create(self.data)

            if response['success']:
                tournaments_views.message_user(VALIDATION_TOURNAMENT)
        else:
            # Gestion des erreurs des inputs
            for input_data in self.data:
                if not input_data['valid']:
                    print(f"Erreur: {input_data.get('error', 'Invalide')}")
                    self.create_tournament()

    def list_tournaments(self, active_menu=True):
        tournaments_data = Tournament().read()

        headers = list(tournaments_data[0].keys())
        body = [list(tournament.values()) for tournament in tournaments_data]
        TournamentsViews().view_list(headers, body)

        if active_menu:
            self.menu_manager.submenu_init()

    #TODO: A controller j'ai modifié la fonction get_tournament_by_name
    def get_info_tournament(self):
        self.list_tournaments(active_menu=False)
        name_tournament = TournamentsViews().input_info_tournament()
        return self.get_tournament_by_name(name_tournament)

    def get_dates_tournament(self):
        data_tournament = self.get_info_tournament()
        TournamentsViews().view_info_tournament(data_tournament)

        self.menu_manager.submenu_init()

    def get_players_by_tournament(self):
        data_tournament = self.get_info_tournament()
        TournamentsViews().view_players_tournament(data_tournament)

        self.menu_manager.submenu_init()

    # On commence le tournoi ou on passe au round suivant
    @staticmethod
    def start_tournament():
        tournaments_views = TournamentsViews()
        name_tournament = tournaments_views.view_start_tournament()

        tournament_data = TournamentManager.get_tournament_by_name(name_tournament)
        if tournament_data is not False:
            round_class = Round(tournament_data)

            if 'status' in tournament_data and 'rounds' in tournament_data['status']:
                TournamentManager.start_round(round_class, name_tournament)
            else:
                # Création des rounds, matchs, et classement
                round_class.create()
                TournamentManager.start_round(round_class, name_tournament)

        else:
            tournaments_views.message_user('Le tournoi n\'existe pas')
            TournamentManager.start_tournament()

    @staticmethod
    def start_round(round_class, name_tournament):
        tournaments_views = TournamentsViews()

        # Envoi des données à la views
        data_matches = round_class.read()
        current_round = data_matches['status']['current_round']
        response = False

        for match in data_matches['status']['rounds'][current_round - 1]['matches']:
            tournaments_views.message_user(match['name'])

            # Retour de la view
            response = TournamentManager.get_result_match(match, round_class)

        if response:
            # Increment le round
            data_matches['status']['current_round'] += 1

            # Mise a jour des datas dans le fichier JSON
            tournament_manager = Tournament()
            tournament_manager.update(name_tournament, data_matches)
        else:
            tournaments_views.message_user('Tous les matchs ont été joués, le tournoi est terminé')
            ranking = data_matches['status']['ranking']
            match_class = Match(data_matches)
            match_class.get_name_by_id_chess(ranking)

            # on affiche les premiers du classement
            max_score = max(player['score'] for player in ranking)
            top_players = [player for player in ranking if player['score'] == max_score]
            title = 'Vainqueurs' if len(top_players) > 1 else 'Vainqueur'

            tournaments_views.message_user(f'{title} du tournoi ')
            for player_data in top_players:
                name = match_class.get_name_by_id_chess(player_data['id_player'])
                print(f'- {name}')

    @staticmethod
    def get_result_match(match, round_class):
        tournaments_views = TournamentsViews()
        result_match = tournaments_views.result_match(match['match'])
        choices = ['0', '0.5', '1']

        if result_match in choices:
            # Get id winner
            winner = []

            if result_match == '0':
                winner.append(match['match'][1])
            elif result_match == '0.5':
                winner.append(match['match'][0])
                winner.append(match['match'][1])
            else:
                winner.append(match['match'][0])

            # Date du match
            now = datetime.now()
            date_match = now.strftime("%d/%m/%Y")

            data_result = {
                'name': match['name'],
                'winner': winner,
                'date_match': date_match,
                'players': match['match']
            }

            # Mise à jour du round
            round_class.update(data_result)
            return True
        else:
            tournaments_views.message_user('La valeur entrée doit être 0, 0.5 ou 1')
            TournamentManager.get_result_match(match, round_class)

    # On récupére des données du tournoi avec le nom de celui ci si il existe
    @staticmethod
    def get_tournament_by_name(name_tournament):
        list_tournament = Tournament().read()

        for tournament in list_tournament:
            if tournament['name'] == name_tournament:
                return tournament
        return False

    def menu_back(self):
        self.menu_manager.main_menu()

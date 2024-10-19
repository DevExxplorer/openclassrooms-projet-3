from datetime import datetime
from random import sample

from models.match import Match
from utils.constants import INPUTS_TOURNAMENT, VALIDATION_TOURNAMENT
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
            self.data.append({
                'name': 'Id du tournoi',
                'slug': 'id_tournament',
                'type': 'id_tournament',
                'valid': True,
                'value': self.generate_id_tournament()
            })
            response = tournament_class.create(self.data)

            if response['success']:
                tournaments_views.message_user(VALIDATION_TOURNAMENT)

                self.menu_manager.submenu_init()
        else:
            # Gestion des erreurs des inputs
            for input_data in self.data:
                if not input_data['valid']:
                    print(f"Erreur: {input_data.get('error', 'Invalide')}")
                    self.create_tournament()

    def list_tournaments(self, active_menu=True):
        tournaments_data = Tournament().read()
        body = []
        headers = ['Nom', 'Lieu', 'Description', 'Id']

        for tournament in tournaments_data:
            if (
                    'name' in tournament
                    and 'place' in tournament
                    and 'description' in tournament
                    and 'id_tournament' in tournament
            ):
                body.append([
                    tournament['name'],
                    tournament['place'],
                    tournament['description'],
                    tournament['id_tournament']
                ])
        TournamentsViews().view_list(headers, body)

        if active_menu:
            self.menu_manager.submenu_init()

    def get_info_tournament(self):
        self.list_tournaments(active_menu=False)
        id_tournament = TournamentsViews().input_info_tournament()
        if self.get_tournament_by_name(id_tournament):
            return self.get_tournament_by_name(id_tournament)
        else:
            return False

    def get_dates_tournament(self):
        data_tournament = self.get_info_tournament()
        TournamentsViews().view_info_tournament(data_tournament)

        self.menu_manager.submenu_init()

    def get_players_by_tournament(self):
        data_tournament = self.get_info_tournament()

        if data_tournament:
            TournamentsViews().view_players_tournament(data_tournament)
        else:
            TournamentsViews().message_user('Le tournoi n\'existe pas')

        self.menu_manager.submenu_init()

    # On commence le tournoi ou on passe au round suivant
    def start_tournament(self):
        tournament_data = self.get_info_tournament()

        if tournament_data is not False:
            round_class = Round(tournament_data)

            if 'status' in tournament_data and 'rounds' in tournament_data['status']:
                self.start_round(round_class, tournament_data)
            else:
                # Création des rounds, matchs, et classement
                round_class.create()
                self.start_round(round_class, tournament_data)

        else:
            TournamentsViews().message_user('Le tournoi n\'existe pas')
            self.start_tournament()

    def start_round(self, round_class, tournament_data):
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
            tournament_manager.update(tournament_data, data_matches)
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

        self.menu_manager.submenu_init()

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

    # On récupére des données du tournoi avec l'id de celui ci si il existe
    @staticmethod
    def get_tournament_by_name(id_tournament):
        list_tournament = Tournament().read()

        for tournament in list_tournament:
            if isinstance(id_tournament, int) and tournament['id_tournament'] == int(id_tournament):
                return tournament
        return False

    def menu_back(self):
        self.menu_manager.main_menu()

    def list_rounds(self):
        tournament_data = self.get_info_tournament()

        if tournament_data is not False:
            if 'status' in tournament_data and 'rounds' in tournament_data['status']:
                for round_data in tournament_data['status']['rounds']:
                    TournamentsViews().message_user(round_data['name'])

                    if round_data['matches']:
                        list_keys = ['Match', 'Date', 'Joueurs', 'Gagnant']
                        list_body = []

                        for match_data in round_data['matches']:
                            winner = ''
                            match_players = (
                                    match_data['match'][0]['name_player']
                                    + ' vs '
                                    + match_data['match'][1]['name_player']
                            )

                            # Vérification si c'est un match nul
                            if len(match_data['winner']) == 1:
                                winner = match_data['winner'][0]['name_player']
                            elif len(match_data['winner']) == 2:
                                winner = "Match nul"

                            date_match = match_data['date'] if match_data['date'] else 'En cours ou à venir'
                            list_body.append([
                                match_data['name'],
                                date_match,
                                match_players,
                                winner
                            ])

                        headers = list(list_keys)
                        TournamentsViews().view_list(headers, list_body)
                    else:
                        TournamentsViews().message_user('Les matchs ont déjà tous été joués')
            else:
                TournamentsViews().message_user('Le tournoi n\'as pas encore débuté')
                self.menu_manager.submenu_init()
        else:
            TournamentsViews().message_user('Le tournoi n\'existe pas')
            self.list_rounds()

        self.menu_manager.submenu_init()

    def generate_id_tournament(self):
        tournament_class = Tournament()
        tournaments = tournament_class.read()
        id_tournament = sample(range(1, 100), 1)

        for tournament in tournaments:
            if tournament.get('id_tournament') and tournament['id_tournament'] == id_tournament:
                self.generate_id_tournament()

        return id_tournament[0]

from utils.constants import *
from utils.input_validator import InputValidator
from views.tournaments_views import TournamentsViews
from models.tournament import Tournament


class TournamentManager:
    def __init__(self, menu_manager):
        self.menu_manager = menu_manager
        self.data = INPUTS_TOURNAMENT

    def create_tournament(self):
        tournaments_views = TournamentsViews()
        self.data = tournaments_views.view_create(self.data)
        self.data = InputValidator(self.data).validate()

        if all(input_data['valid'] for input_data in self.data):
            response = Tournament().create(self.data)
            if response['success']:
                tournaments_views.message_user(VALIDATION_TOURNAMENT)

        else:
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

    def get_info_tournament(self):
        self.list_tournaments(active_menu=False)
        name_tournament = TournamentsViews().input_info_tournament()
        return Tournament().get_tournament_by_name(name_tournament)

    def get_dates_tournament(self):
        data_tournament = self.get_info_tournament()
        TournamentsViews().view_info_tournament(data_tournament)

        self.menu_manager.submenu_init()

    def get_players_by_tournament(self):
        data_tournament = self.get_info_tournament()
        TournamentsViews().view_players_tournament(data_tournament)

        self.menu_manager.submenu_init()

    def menu_back(self):
        self.menu_manager.main_menu()


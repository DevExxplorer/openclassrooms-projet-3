from utils.constants import *
from utils.input_validator import InputValidator
from views.tournaments_views import TournamentsViews
from models.tournament import Tournament


class TournamentManager:
    def __init__(self, menu_manager):
        self.menu_manager = menu_manager
        self.data = INPUTS_TOURNAMENT

    def create_tournament(self):
        self.data = TournamentsViews(self.data).view_create()
        self.data = InputValidator(self.data).validate()

        if all(input_data['valid'] for input_data in self.data):
            Tournament(self.data).create()
        else:
            for input_data in self.data:
                if not input_data['valid']:
                    print(f"Erreur: {input_data.get('error', 'Invalide')}")
                    self.create_tournament()


    """
    def view_tournament(self):
        self.menu_manager.submenu_init()

    def menu_back(self):
        self.menu_manager.main_menu()
    tournament_return = Tournament().create(new_data)

    if tournament_return:
        TournamentsViews().message_user(VALIDATION_TOURNAMENT)
    """
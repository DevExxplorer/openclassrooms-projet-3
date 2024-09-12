from utils.constants import *
from views.tournaments_views import TournamentsViews
from models.tournament import Tournament


class TournamentManager:
    def __init__(self, menu_manager):
        self.menu_manager = menu_manager

    def create_tournament(self):
        new_data = TournamentsViews().tournaments_view_create()
        tournament_return = Tournament().create(new_data)

        if tournament_return:
            TournamentsViews().message_user(VALIDATION_TOURNAMENT)

        self.menu_manager.submenu_init()

    def view_tournament(self):
        self.menu_manager.submenu_init()

    def menu_back(self):
        self.menu_manager.main_menu()
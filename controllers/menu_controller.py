from utils.constants import *
from views.menus_views import MenusView
from views.players_views import PlayersViews
from views.tournaments_views import TournamentsViews
from models.player import Player
from models.tournament import Tournament


class MenuController:
    def __init__(self):
        self.menu = MENUS
        self.menu_selected = ''

    def display_main_menu(self):
        menus_view = MenusView(self.menu)

        while True:
            try:
                self.menu_selected = menus_view.view_main_menu()
                self.display_submenu()
                return
            except KeyError:
                menus_view.view_error()

    def display_submenu(self):
        menus_view = MenusView(self.menu[self.menu_selected]['submenu'])
        submenu_selected = menus_view.view_main_menu()
        action_submenu = self.menu[self.menu_selected]['submenu'][submenu_selected]['action']
        method = getattr(self, action_submenu)
        return method()

    def view_players(self):
        players_data = Player().read()
        PlayersViews().players_view_list(players_data)

        self.display_submenu()

    def create_player(self):
        new_data = PlayersViews().players_view_create()
        Player().create(new_data)
        self.display_submenu()

    def create_tournament(self):
        new_data = TournamentsViews().tournaments_view_create()
        tournament_return = Tournament().create(new_data)

        if tournament_return:
            TournamentsViews().message_user(VALIDATION_TOURNAMENT)

        self.display_submenu()

    def menu_back(self):
        self.display_main_menu()



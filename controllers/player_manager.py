from views.players_views import PlayersViews
from models.player import Player


class PlayerManager:
    def __init__(self, menu_manager):
        self.menu_manager = menu_manager

    def create_player(self):
        new_data = PlayersViews().players_view_create()
        Player().create(new_data)
        self.menu_manager.submenu_init()

    def view_players(self):
        players_data = Player().read()
        PlayersViews().players_view_list(players_data)
        self.menu_manager.submenu_init()

    def menu_back(self):
        self.menu_manager.main_menu()

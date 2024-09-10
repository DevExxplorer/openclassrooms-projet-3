from utils.constants import *
from views.menus_views import MenusView
from views.players_views import PlayersViews
from models.player import Player


class MenuController:
    def __init__(self):
        self.menu = MENUS

    def display_main_menu(self):
        menus_view = MenusView(self.menu)

        while True:
            try:
                menu_selected = menus_view.view_main_menu()
                self.display_submenu(menu_selected)
                return
            except KeyError:
                menus_view.view_error()

    def display_submenu(self, menu_selected):
        menus_view = MenusView(self.menu[menu_selected]['submenu'])
        submenu_selected = menus_view.view_main_menu()
        action_submenu = self.menu[menu_selected]['submenu'][submenu_selected]['action']
        method = getattr(self, action_submenu)
        return method()

    @staticmethod
    def view_players():
        players_data = Player().read()
        PlayersViews().players_view_list(players_data)

        # TODO: Retourner au menu précédent à prévoir

    @staticmethod
    def create_player():
        data_new_player = PlayersViews().players_view_create()
        print(data_new_player)

    def menu_back(self):
        self.display_main_menu()



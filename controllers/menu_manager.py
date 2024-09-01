from utils.constants import *
from views.players_view import PlayersView


class MenuManager:
    def __init__(self):
        self.success = False
        self.message_error = {}
        self.number_menu_valid = 0

    def check_value_submit(self, menu_selected, total_options):
        try:
            if int(menu_selected) and int(menu_selected) <= total_options:
                self.success = True
                self.number_menu_valid = int(menu_selected)
            else:
                self.message_error = 'La valeur séléctionnée doit être un nombre existant'
                return self.message_error
        except ValueError:
            self.message_error = 'La valeur séléctionné doit être un nombre'
            return self.message_error

    def redirect_method(self, method_option):
        method = getattr(self, method_option)
        return method()

    @staticmethod
    def create_player():
        PlayersView.add_new_player()

    @staticmethod
    def view_players():
        PlayersView.list_players_views()

    @staticmethod
    def menu_back():
        return 'menu_back'

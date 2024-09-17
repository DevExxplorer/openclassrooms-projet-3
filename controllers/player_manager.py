from views.players_views import PlayersViews
from models.player import Player
from datetime import datetime
from utils.constants import *
import re


class PlayerManager:
    def __init__(self, menu_manager):
        self.menu_manager = menu_manager
        self.success = False
        self.errors_message = []

    def create_player(self):
        player_view = PlayersViews()
        data_new_player = player_view.players_view_create()
        self.check_birthday_date(data_new_player['birthday'])
        self.check_chess_id(data_new_player['chess_id'])

        if not self.success:
            for error in self.errors_message:
                player_view.message_player('error', error)
            self.errors_message.clear()
            self.create_player()
        else:
            data = Player().create(data_new_player)
            type_message = 'validate' if data['success'] else 'error'
            player_view.message_player(type_message, data['message'])

            self.menu_manager.submenu_init()

    def check_birthday_date(self, birthday_date):
        try:
            datetime.strptime(birthday_date, '%d/%m/%Y')
            self.success = True
            return
        except ValueError:
            self.errors_message.append("Erreur: le format de la date est incorrect. Utilisez JJ/MM/AAAA.")

    def check_chess_id(self, chess_id):
        try:
            check_chess_id = re.search("^[A-Z]{2}[0-9]{5}$", chess_id)
            if check_chess_id:
                self.success = True
                return
            else:
                self.errors_message.append('Erreur: L\'Identifiant national d’échecs doit avoir deux lettres et 5 chiffres')
        except ValueError:
            self.errors_message.append('Erreur: L\'Identifiant national d’échecs doit avoir deux lettres et 5 chiffres')

    def view_players(self, active_menu=True):
        players_data = Player().read()

        headers = []
        keys = list(players_data[0].keys())
        for key in keys:
            if key in TRANSLATE:
                headers.append(TRANSLATE[key])
        body = [list(player.values()) for player in players_data]
        PlayersViews().players_view_list(headers, body)

        if not active_menu:
            self.menu_manager.submenu_init()

    def menu_back(self):
        self.menu_manager.main_menu()

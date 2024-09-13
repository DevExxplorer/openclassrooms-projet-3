from tabulate import tabulate
from utils.constants import *


class PlayersViews:
    @staticmethod
    def players_view_list(headers, body):
        print(tabulate(body, headers=headers, tablefmt="double_grid"))

    @staticmethod
    def players_view_create():
        print(NEW_PLAYER)
        lastname = input('Nom: ')
        firstname = input('Prénom: ')
        birthday = input('Date d\'anniversaire (format: JJ/MM/AAAA): ')
        chess_id = input('Identifiant national d’échecs: ')

        return {
            'lastname': lastname,
            'firstname': firstname,
            'birthday': birthday,
            'chess_id': chess_id
        }

    @staticmethod
    def message_player(type_message, message):
        color_message = GREEN if type_message == 'validate' else RED
        print(f'{color_message}{BOLD}{message}{RESET}')

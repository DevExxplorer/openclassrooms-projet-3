from tabulate import tabulate
from utils.constants import *
from controllers.player_manager import PlayerManager


class PlayersView:
    @staticmethod
    def list_players_views():
        data = PlayerManager.get_list_players()
        print(tabulate(data['body'], headers=data['header'], tablefmt="double_grid"))

    @staticmethod
    def add_new_player():
        print(NEW_PLAYER)
        lastname = input(f'\nNom: ')
        firstname = input('Prénom: ')
        birthday = input('Date d\'anniversaire: ')
        chess_id = input('Identifiant national d’échecs: ')

        message_validate = PlayerManager().create_player(lastname, firstname, birthday, chess_id)

        if message_validate['success']:
            print(f'{GREEN}Le nouveau joueur a bien été ajouté{RESET}')
        else:
            print(message_validate)
            for error in message_validate['errors']:
                print(f'{RED}{error}{RESET}')

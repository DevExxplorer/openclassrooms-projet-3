from tabulate import tabulate
from utils.constants import *
from datetime import datetime


class PlayersViews:
    @staticmethod
    def players_view_list(players_data):
        header = list(players_data[0].keys())
        body = [list(player.values()) for player in players_data]
        print(tabulate(body, headers=header, tablefmt="double_grid"))

    @staticmethod
    def players_view_create():
        print(NEW_PLAYER)
        lastname = input(f'\nNom: ')
        firstname = input('Prénom: ')

        while True:
            birthday = input('Date d\'anniversaire (format JJ/MM/AAAA): ')
            try:
                datetime.strptime(birthday, '%d/%m/%Y')
                break
            except ValueError:
                print("Erreur: le format de la date est incorrect. Utilisez JJ/MM/AAAA.")

        chess_id = input('Identifiant national d’échecs: ')

        return {
            'lastname': lastname,
            'firstname': firstname,
            'birthday': birthday,
            'chess_id': chess_id
        }
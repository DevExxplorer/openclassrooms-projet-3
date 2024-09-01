import re
from models.player import Player


class PlayerManager:
    def __init__(self):
        self.form_valid = True
        self.message_error = []

    @staticmethod
    def get_list_players():
        players = Player.read()

        header = list(players[0].keys())
        body = [list(player.values()) for player in players]

        return {'header': header, 'body': body}

    def create_player(self, lastname, firstname, birthday, chess_id):
        self.check_birthday(birthday)
        self.check_chess_id(chess_id)

        if self.form_valid:
            Player.create(
                lastname,
                firstname,
                birthday,
                chess_id
            )
            return {'success': True}
        else:
            return {'success': False, 'errors': self.message_error}

    def check_birthday(self, birthday):
        regex_birthday = re.search("^[0-9]{2}/[0-9]{2}/[0-9]{4}$", birthday)
        if not regex_birthday:
            self.form_valid = False
            self.message_error.append('La date d\'anniversaire doit correspondre au format DD/MM/AAAA')

    def check_chess_id(self, chess_id):
        check_chess_id = re.search("^[A-Z]{2}[0-9]{5}$", chess_id)
        if not len(chess_id) == 7 and not check_chess_id:
            self.form_valid = False
            self.message_error.append('L\'Identifiant national d’échecs doit avoir deux lettres et 5 chiffres')


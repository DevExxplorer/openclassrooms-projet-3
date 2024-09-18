from utils.constants import *
from datetime import datetime
from models.player import Player
import re


class InputValidator:
    def __init__(self, data):
        self.data = data

    def validate(self):
        validators = {
            'date': self.validate_date,
            'number': self.validate_number,
            'list': self.validate_list,
        }

        for input_data in self.data:
            # Attribue la valeur par défaut de 4 si elle est vide
            if input_data['type'] == 'number' and not input_data.get('value'):
                input_data['value'] = 4

            if 'value' in input_data and input_data['value']:
                validator = validators.get(input_data['type'])
                if validator:
                    validator(input_data)
                else:
                    input_data['valid'] = True
            else:
                input_data['error'] = 'Vous n\'avez pas rempli le champs'

        return self.data

    @staticmethod
    def validate_date(input_data):
        dates_event = input_data['value'].replace(' ', '').split(',')
        try:
            date1 = datetime.strptime(dates_event[0], '%d/%m/%Y')
            date2 = datetime.strptime(dates_event[1], '%d/%m/%Y')
            if date1 > date2:
                input_data['valid'] = False
                input_data['error'] = 'Erreur: La date de fin se termine avant la date de début'
            else:
                input_data['valid'] = True
                input_data['value'] = dates_event
        except ValueError:
            input_data['error'] = 'Erreur: le format des dates est incorrect. Utilisez JJ/MM/AAAA.'

        return input_data

    @staticmethod
    def validate_number(input_data):
        try:
            input_data['value'] = int(input_data['value'])
            input_data['valid'] = True
        except ValueError:
            input_data['error'] = 'La champs doit être un nombre'

        return input_data

    @staticmethod
    def validate_list(input_data):
        list_players_check = []
        list_players_input = input_data['value'].replace(' ', '').split(',')

        for player in list_players_input:
            check_chess_id = InputValidator.check_chess_id(player)
            if player not in list_players_check and check_chess_id['success']:
                name_player = Player.get_name_by_id_chess(player)
                list_players_check.append(name_player)

        if list_players_check:
            input_data['value'] = list_players_check
            input_data['valid'] = True

        return input_data

    @staticmethod
    def check_chess_id(chess_id):
        data = {
            'success': False,
            'message': ERROR_MSG['chess_id']
        }

        try:
            check_chess_id = re.search("^[A-Z]{2}[0-9]{5}$", chess_id)
            if check_chess_id:
                data['success'] = True
        except ValueError:
            data['message'] = ERROR_MSG['chess_id']

        return data

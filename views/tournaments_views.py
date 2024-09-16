from utils.constants import *
from datetime import datetime


class TournamentsViews:
    def __init__(self, data):
        self.data = data

    def view_create(self):
        print(NEW_TOURNAMENT)

        for input_data in self.data:
            if not input_data['valid']:
                input_data['value'] = self.get_user_input(input_data['name'])

        return self.data

    @staticmethod
    def get_user_input(field_name):
        return input(f'{field_name}: ').strip()

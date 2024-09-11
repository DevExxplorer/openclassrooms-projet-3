from utils.constants import *
from datetime import datetime


class TournamentsViews:
    def __init__(self):
        pass

    @staticmethod
    def tournaments_view_create():
        print(NEW_TOURNAMENT)

        name = input(f'\nNom du tournoi: ')
        place = input(f'Lieu du tournoi: ')

        start_date = TournamentsViews.input_date("Entrez la date de début (DD-MM-YYYY): ")
        end_date = TournamentsViews.input_date("Entrez la date de fin (DD-MM-YYYY): ")

        # TODO: Controller la date de debut et de fin

        return {
            'name': name,
            'place': place,
            'start_date': TournamentsViews.datetime_to_str(start_date),
            'end_date': TournamentsViews.datetime_to_str(end_date)
        }

    @staticmethod
    def input_date(message):
        while True:
            date_str = input(message)
            try:
                return datetime.strptime(date_str, '%d-%m-%Y')
            except ValueError:
                print("Format incorrect. Veuillez entrer une date au format DD-MM-YYYY.")

    @staticmethod
    def datetime_to_str(date_event):
        return date_event.strftime('%d-%m-%Y')

    @staticmethod
    def message_user(message):
        print(f'{message}')

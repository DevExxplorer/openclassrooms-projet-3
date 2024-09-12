import json
import os

FILENAME = "tournaments.json"


class Tournament:
    def __init__(self):
        self.list_players = [
            {
                'name': 'Clément',
                'score': 0,
                'already_played': ['Pierre']
            },
            {
                'name': 'Pierre',
                'score': 0,
                'already_played': ['Clément', 'Jacques']
            },
            {
                'name': 'Loic',
                'score': 0,
                'already_played': []
            },
            {
                'name': 'Jacques',
                'score': 0,
                'already_played': ['Pierre']
            },
            {
                'name': 'Philippe',
                'score': 0,
                'already_played': []
            },
            {
                'name': 'Manon',
                'score': 0,
                'already_played': []
            },
        ]
        self.number_round = 4
        self.current_round = 1

    @staticmethod
    def read():
        if os.path.exists("data/" + FILENAME):
            with open("data/" + FILENAME, "r", encoding="utf-8") as file:
                tournament_json = sorted(json.load(file), key=lambda x: x['name'])
        else:
            tournament_json = []

        return tournament_json

    @staticmethod
    def create(new_data):
        if not os.path.isdir('data'):
            os.mkdir('data')

        list_tournaments = Tournament.read()
        list_tournaments.append(new_data)

        with open("data/" + FILENAME, "w", encoding="utf-8") as file:
            json.dump(list_tournaments, file, ensure_ascii=False, indent=4)

        return True

    """
    def start_tournament(self):
        while self.current_round <= self.number_round:
            print(f'\nTour {self.current_round}:\n')

            round_tournament = Round(self.list_players)
            round_tournament.start_round()
            round_tournament.end_round()

            input('\nPasser au prochain round (Appuyer sur n\'importe qu\'elle touche: ')
            self.current_round = self.current_round + 1
    """
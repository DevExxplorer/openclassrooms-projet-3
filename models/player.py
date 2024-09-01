import json
import os

FILENAME = "players.json"


class Player:
    def __init__(self):
        self.list_players = self.read()

    def create(self, lastname, firstname, birthday, chess_id):
        if not os.path.isdir('data'):
            os.mkdir('data')

        self.list_players.append({
            "lastname": lastname,
            "firstname": firstname,
            "birthday": birthday,
            "chess_id": chess_id
        })

        with open("data/" + FILENAME, "w", encoding="utf-8") as file:
            json.dump(self.list_players, file, ensure_ascii=False, indent=4)

    @staticmethod
    def read():
        if os.path.exists("data/" + FILENAME):
            with open("data/" + FILENAME, "r", encoding="utf-8") as file:
                players_json = sorted(json.load(file), key=lambda player: player['lastname'])
        else:
            players_json = []

        return players_json

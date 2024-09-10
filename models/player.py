import json
import os

FILENAME = "players.json"


class Player:
    @staticmethod
    def read():
        if os.path.exists("data/" + FILENAME):
            with open("data/" + FILENAME, "r", encoding="utf-8") as file:
                players_json = sorted(json.load(file), key=lambda player: player['lastname'])

        return players_json

    @staticmethod
    def create(new_data):
        if not os.path.isdir('data'):
            os.mkdir('data')

        list_players = Player.read()
        list_players.append(new_data)

        with open("data/" + FILENAME, "w", encoding="utf-8") as file:
            json.dump(list_players, file, ensure_ascii=False, indent=4)

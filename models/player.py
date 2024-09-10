import json
import os

FILENAME = "players.json"


class Player:
    def __init__(self):
        pass

    @staticmethod
    def read():
        if os.path.exists("data/" + FILENAME):
            with open("data/" + FILENAME, "r", encoding="utf-8") as file:
                players_json = sorted(json.load(file), key=lambda player: player['lastname'])

        return players_json

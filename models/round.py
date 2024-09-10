import random
from models.match import Match


class Round:
    def __init__(self, list_players):
        self.list_players = list_players

    def start_round(self):
        self.list_players = self.list_player_by_score()
        match_number = 1

        for i in range(0, len(self.list_players), 2):
            if i + 1 < len(self.list_players):
                match = Match(self.list_players, self.list_players[i], self.list_players[i + 1], match_number)
                match.play()
                match_number += 1

    def list_player_by_score(self):
        return sorted(self.list_players, key=lambda x: x['score'], reverse=True)

    def mix_players(self):
        return random.sample(self.list_players, len(self.list_players))

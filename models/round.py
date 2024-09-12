"""
import random
from models.match import Match


class Round:
    def __init__(self, list_players):
        self.list_players = list_players

    def start_round(self):
        self.create_matches()
        self.list_players = self.list_player_by_score()

    def end_round(self):
        self.list_players = self.list_player_by_score()
        self.display_score()

    def create_matches(self):
        unpaired_players = [player['name'] for player in self.list_players]



        unpaired_players = [player['name'] for player in self.list_players]
        for i in range(0, len(self.list_players), 2):
            if i + 1 < len(self.list_players):
                player1 = self.list_players[i]
                player2 = self.list_players[i + 1]

                if player1['name'] in player2['already_played']:
                    player2 = random.choice(unpaired_players)
                    print(f'Déjà joué contre {player2}')

    def list_player_by_score(self):
        return sorted(self.list_players, key=lambda x: x['score'], reverse=True)

    def mix_players(self):
        return random.sample(self.list_players, len(self.list_players))

    def display_score(self):
        print('Classement:')
        for pos in range(len(self.list_players)):
            print(f'{pos} - {self.list_players[pos]['name']} avec {self.list_players[pos]['score']} point(s)')

            
                     # match = Match(self.list_players)
                    # match.play()

                    # match_number = 1
                    for i in range(0, len(self.list_players), 2):
                        if i + 1 < len(self.list_players):
                            match = Match(self.list_players, self.list_players[i], self.list_players[i + 1], match_number)
                            match.play()
                            match_number += 1
"""

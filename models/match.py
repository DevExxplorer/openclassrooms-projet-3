import random


class Match:
    def __init__(self, list_players, player1, player2, match_number):
        self.list_players = list_players
        self.player1 = player1
        self.player2 = player2
        self.match = (self.player1, self.player2)
        self.match_number = match_number
        self.winner = ''

    def play(self):
        self.winner = self.get_winner()
        self.update_list_players()
        print(f'Match {self.match_number}: ({self.player1['player']} vs {self.player2['player']}) Le joueur {self.winner[0]['player']} a gagné le match')

    def get_winner(self):
        return random.sample(self.match, 1)

    def update_list_players(self):
        for player in self.list_players:
            if player['player'] == self.winner[0]['player']:
                player['score'] = player['score'] + 1

            if player['player'] == self.player1['player']:
                player['already_played'].append(self.player2['player'])

            if player['player'] == self.player2['player']:
                player['already_played'].append(self.player1['player'])


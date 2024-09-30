from pprint import pprint

from models.player import Player


class Match:
    def __init__(self, data):
        self.data = data

    def create(self, ranking):
        matches = []
        pairs = self.generate_match_pairwise(ranking)
        for pair_index in range(len(pairs)):
            match = {
                'name': 'Match ' + str(pair_index + 1),
                'date': '',
                'match': pairs[pair_index],
                'winner': ''
            }
            matches.append(match)

        return matches

    def read(self):
        return self.data

    def update(self, result):
        winner = result['winner']
        if len(winner) == 1:
            point = 1.0
            players = [winner[0]['id_player']]
        else:
            point = 0.5
            players = [winner[0]['id_player'], winner[1]['id_player']]

        # Mise à jour des données du match
        self.update_data_match(result)
        print(result)
        # Mise à jour des données de ranking
        self.increment_score(self, players, point)
        self.add_already_played(result['players'])

    def update_data_match(self, result):
        current_round = self.data['status']['current_round'] - 1
        for match in self.data['status']['rounds'][current_round]['matches']:
            if match['name'] == result['name']:
                match['date'] = result['date_match']
                match['winner'] = result['winner']

    @staticmethod
    def increment_score(self, players, point):
        for rank in self.data['status']['ranking']:
            for player in players:
                if rank['id_player'] == player:
                    rank['score'] += point
                    break

    def add_already_played(self, players):
        for player_index in range(len(self.data['status']['ranking'])):
            if self.data['status']['ranking'][player_index]['id_player'] == players[0]['id_player']:
                self.data['status']['ranking'][player_index]['already_played'].append(players[1]['id_player'])

            if self.data['status']['ranking'][player_index]['id_player'] == players[1]['id_player']:
                self.data['status']['ranking'][player_index]['already_played'].append(players[0]['id_player'])

    # Genere des paires de joueurs
    def generate_match_pairwise(self, data):
        remaining_players = data[:]
        pairs = []

        # Création des pairs
        while remaining_players:
            player = remaining_players.pop(0)
            opponent = self.find_opponent(player, remaining_players)

            if opponent:
                pairs.append([
                    {
                        'id_player': player['id_player'],
                        'name_player': self.get_name_by_id_chess(player['id_player']),
                    },
                    {
                        'id_player': opponent['id_player'],
                        'name_player': self.get_name_by_id_chess(opponent['id_player']),
                    }
                ])
                remaining_players.remove(opponent)

        return pairs

    @staticmethod
    def find_opponent(player, players_list):
        for opponent in players_list:
            if opponent['id_player'] not in player['already_played']:
                return opponent
        return None

    @staticmethod
    def get_name_by_id_chess(chess_id):
        list_players = Player.read()

        for player in list_players:
            if player['chess_id'] == chess_id:
                return player['lastname'] + ' ' + player['firstname']
        return "Joueur introuvable"
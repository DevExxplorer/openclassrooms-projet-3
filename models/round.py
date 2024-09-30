import random

from models.match import Match


class Round:
    def __init__(self, data):
        self.data = data

    def create(self):
        ranking = self.generate_ranking()

        # Création des matchs du premier round
        match_class = Match(self.data)
        matches = match_class.create(ranking)

        # Création des rounds a venir
        rounds_list = []
        for index in range(self.data['number_round']):
            rounds_list.append({
                'name': 'Round ' + str(index + 1),
                'matches': matches if index == 0 else []
            })

        # Creation du tableau contenant les données du tournoi
        new_data = dict()
        new_data['status'] = {
            'current_round': 1,
            'rounds': rounds_list,
            'ranking': ranking
        }

        # Ajout des données
        self.data.update(new_data)

    def read(self):
        return self.data

    def update(self, result_match):
        match_class = Match(self.data)
        match_class.update(result_match)
        self.order_ranking()
        self.generate_next_round(match_class)
        return self.data

    def generate_next_round(self, match_class):
        ranking = self.data['status']['ranking']
        next_round = self.data['status']['current_round']

        self.data['status']['rounds'][next_round]['matches'] = match_class.create(ranking)

    # Génére le tableau de classement du tournoi
    def generate_ranking(self):
        data = []
        for player_index in range(len(self.data['players'])):
            data.append({
                'id_player': self.data['players'][player_index],
                'score': 0.0,
                'already_played': []
            })
        return data

    # Retourne une liste des joueurs mélangés aléatoirement
    @staticmethod
    def mix_players(players):
        return random.sample(players, len(players))

    # Mise a jour des classement
    def order_ranking(self):
        sorted_results = sorted(self.data['status']['ranking'], key=lambda x: x['score'], reverse=True)
        self.data['status']['ranking'] = sorted_results

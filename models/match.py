from models.player import Player


class Match:
    """
        Class permettant de gérer les matchs

        Attributes

        data(Array): Données du round
    """
    def __init__(self, data):
        """
            Constructs

            Parameters

            data(Array): Données du round
        """
        self.data = data

    def create(self, ranking):
        """
            Création d'un match après avoir générer des pairs
        """
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
        """
            Lire les données du match

            Returns
                data(Array): Donnée du match
        """
        return self.data

    def update(self, result):
        """
            Mise à jour d'un match

            Parameters

            result(Array): Resultat du match
        """
        winner = result['winner']
        if len(winner) == 1:
            point = 1.0
            players = [winner[0]['id_player']]
        else:
            point = 0.5
            players = [winner[0]['id_player'], winner[1]['id_player']]

        # Mise à jour des données du match
        self.update_data_match(result)
        # Mise à jour des données de ranking
        self.increment_score(self, players, point)
        self.add_already_played(result['players'])

    def update_data_match(self, result):
        """
            Mise à jour des données du match

            Parameters

            result(Array): Resultat du match
        """
        current_round = self.data['status']['current_round'] - 1
        for match in self.data['status']['rounds'][current_round]['matches']:
            if match['name'] == result['name']:
                match['date'] = result['date_match']
                match['winner'] = result['winner']

    @staticmethod
    def increment_score(self, players, point):
        """
            Gestion du score de chaques joueurs apres que le round soit terminé

            Parameters

            players(Array): Liste des joueurs
            point(Number): score du match
        """
        for rank in self.data['status']['ranking']:
            for player in players:
                if rank['id_player'] == player:
                    rank['score'] += point
                    break

    def add_already_played(self, players):
        """
            Après un match ajoute l'id du joueur dans un tableau

            Parameters

            players(Array): Liste des joueurs
        """
        for player_index in range(len(self.data['status']['ranking'])):
            if self.data['status']['ranking'][player_index]['id_player'] == players[0]['id_player']:
                self.data['status']['ranking'][player_index]['already_played'].append(players[1]['id_player'])

            if self.data['status']['ranking'][player_index]['id_player'] == players[1]['id_player']:
                self.data['status']['ranking'][player_index]['already_played'].append(players[0]['id_player'])

    # Genere des paires de joueurs
    def generate_match_pairwise(self, data):
        """
           Génération des pairs

           Parameters

           data(Array): Données du round
       """
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
        """
            Trouver un adversaire

            Parameters
                player(Array) : Donnée du joueur
                players_list(Array): Liste des joueurs

            Returns
                opponent(Array) : Donnée joueur adverse
        """
        for opponent in players_list:
            if opponent['id_player'] not in player['already_played']:
                return opponent
        return None

    @staticmethod
    def get_name_by_id_chess(chess_id):
        """
           Retrouve un nom de joueur avec son ID d'échec

           Parameters
               chess_id(str) : ID joueur

           Returns
               player(str) : Nom et prénom joueur
       """
        list_players = Player.read()

        for player in list_players:
            if player['chess_id'] == chess_id:
                return player['lastname'] + ' ' + player['firstname']
        return "Joueur introuvable"

from models.round import Round


class Tournament:
    def __init__(self):
        self.list_players = [
            {
                'player': 'player1',
                'score': 0,
                'already_played': []
            },
            {
                'player': 'player2',
                'score': 0,
                'already_played': []
            },
            {
                'player': 'player3',
                'score': 0,
                'already_played': []
            },
            {
                'player': 'player4',
                'score': 0,
                'already_played': []
            },
            {
                'player': 'player5',
                'score': 0,
                'already_played': []
            },
            {
                'player': 'player6',
                'score': 0,
                'already_played': []
            },
        ]
        self.number_round = 4
        self.current_round = 1

    def start_tournament(self):
        while self.current_round <= self.number_round:
            print(f'\nTour {self.current_round}:\n')

            Round(self.list_players).start_round()

            self.current_round = self.current_round + 1

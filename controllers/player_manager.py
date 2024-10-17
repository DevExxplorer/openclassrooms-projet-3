from views.players_views import PlayersViews
from utils.input_validator import InputValidator
from models.player import Player
from utils.constants import INPUTS_PLAYERS, VALIDATION_PLAYER


class PlayerManager:
    def __init__(self, menu_manager):
        self.menu_manager = menu_manager
        self.data = INPUTS_PLAYERS

    def create_player(self):
        player_view = PlayersViews()

        # Affichage et récupération des inputs de la vue
        self.data = player_view.players_view_create(self.data)

        # Validation de ses données
        self.data = InputValidator(self.data).validate()

        # Vérification que tous les input_data['valid'] soit True
        if all(input_data['valid'] for input_data in self.data):
            tournament_class = Player()
            response = tournament_class.create(self.data)

            if response['success']:
                player_view.message_player('validate', VALIDATION_PLAYER)

                self.menu_manager.submenu_init()
        else:
            # Gestion des erreurs des inputs
            for input_data in self.data:
                if not input_data['valid']:
                    print(f"Erreur: {input_data.get('error', 'Invalide')}")
                    self.create_player()

    def view_players(self, active_menu=True):
        players_data = Player().read()

        headers = []
        for input_player in INPUTS_PLAYERS:
            headers.append(input_player['name'])
        body = [list(player.values()) for player in players_data]
        PlayersViews().players_view_list(headers, body)

        if active_menu:
            self.menu_manager.submenu_init()

    @staticmethod
    def get_list_players_by_tournament(data_tournament):
        data = []
        players_data = Player().read()

        for player_tournament in data_tournament['players']:
            for player in players_data:
                if player['chess_id'] == player_tournament:
                    data.append(player)

        return data

    def menu_back(self):
        self.menu_manager.main_menu()

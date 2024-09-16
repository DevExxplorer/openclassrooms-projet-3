from utils.input_validator import InputValidator
from views.tournaments_views import TournamentsViews


class TournamentManager:
    def __init__(self, menu_manager):
        self.menu_manager = menu_manager
        self.data = [
            {'name': 'Nom', 'slug': 'name', 'value': '', 'valid': False},
            {'name': 'Lieu', 'slug': 'place', 'value': '', 'valid': False},
            {'name': 'Date de début / Date de fin (DD/MM/YYYY,DD/MM/YYYY)', 'slug': 'date_event', 'value': '', 'valid': False},
            # {'name': 'Nombre de tour (par default: 4)', 'slug': 'round_number', 'value': '', 'valid': False},
            # {'name': 'Ajouter des joueurs (Séparer les joueurs par une  virgule)'
            # , 'slug': 'players', 'value': '', 'valid': False},
            # {'name': 'Description', 'slug': 'description', 'value': '', 'valid': False},
        ]

    def create_tournament(self):
        self.data = TournamentsViews(self.data).view_create()
        self.data = InputValidator(self.data).validate()

        if all(input_data['valid'] for input_data in self.data):
            print('ok')
        else:
            for input_data in self.data:
                if not input_data['valid']:
                    print(f"Erreur: {input_data.get('error', 'Invalide')} pour {input_data['name']}")
                    self.create_tournament()


    """
    def view_tournament(self):
        self.menu_manager.submenu_init()

    def menu_back(self):
        self.menu_manager.main_menu()
    tournament_return = Tournament().create(new_data)

    if tournament_return:
        TournamentsViews().message_user(VALIDATION_TOURNAMENT)
    """
from tabulate import tabulate
from utils.constants import NEW_PLAYER, BOLD, RESET, RED, GREEN


class PlayersViews:
    """
        Vue des différents choix du menu Joueur
    """
    @staticmethod
    def players_view_list(headers, body):
        """
            Affichage de la liste des joueurs
        """
        print(tabulate(body, headers=headers, tablefmt="double_grid"))

    @staticmethod
    def players_view_create(data):
        """
            Affichage des champs pour la création d'un nouveau joueur
        """
        print(NEW_PLAYER)

        for input_data in data:
            if not input_data['valid']:
                input_data['value'] = input(f'{input_data["name"]}: ').strip()

        return data

    @staticmethod
    def message_player(type_message, message):
        """
            Affichage d'un message personnalisé

            Si 'validate' sera vert sinon rouge
        """
        color_message = GREEN if type_message == 'validate' else RED
        print(f'{color_message}{BOLD}{message}{RESET}')

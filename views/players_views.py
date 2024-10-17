from tabulate import tabulate
from utils.constants import NEW_PLAYER, BOLD, RESET, RED, GREEN


class PlayersViews:
    @staticmethod
    def players_view_list(headers, body):
        print(tabulate(body, headers=headers, tablefmt="double_grid"))

    @staticmethod
    def players_view_create(data):
        print(NEW_PLAYER)

        for input_data in data:
            if not input_data['valid']:
                input_data['value'] = input(f'{input_data["name"]}: ').strip()

        return data

    @staticmethod
    def message_player(type_message, message):
        color_message = GREEN if type_message == 'validate' else RED
        print(f'{color_message}{BOLD}{message}{RESET}')

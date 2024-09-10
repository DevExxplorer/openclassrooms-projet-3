from utils.constants import *
from controllers.menu_controller import MenuController

from models.tournament import Tournament


def main():
    print(f'{BLUE}{BOLD}{UNDERLINE}{MESSAGE_MENU}{RESET}')
    MenuController().display_main_menu()

    # tournament = Tournament()
    # tournament.start_tournament()


if __name__ == '__main__':
    main()

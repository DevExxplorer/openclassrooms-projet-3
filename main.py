from utils.constants import BLUE, BOLD, UNDERLINE, MESSAGE_MENU, RESET, MAIN_MENU
from controllers.menu_manager import MenuManager


def main():
    print(f'{BLUE}{BOLD}{UNDERLINE}{MESSAGE_MENU}{RESET}\n')
    MenuManager(MAIN_MENU).main_menu()


if __name__ == '__main__':
    main()

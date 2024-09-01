from views.menu_view import MenuView
from utils.constants import *


def main():
    print(f'{BLUE}{BOLD}{UNDERLINE}{MESSAGE_MENU}{RESET}')
    MenuView().view_main_menu()


if __name__ == '__main__':
    main()

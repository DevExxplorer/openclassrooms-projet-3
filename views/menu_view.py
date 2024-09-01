from utils.constants import *
from controllers.menu_manager import MenuManager


class MenuView:
    def __init__(self):
        self.main_menu = MAIN_MENU
        self.menus = ALL_MENUS

    def view_main_menu(self):
        self.view_all_menus(self.main_menu)
        menu_selected = input(SELECTED_MESSAGE)
        menu_manager = MenuManager()
        menu_manager.check_value_submit(menu_selected, len(self.main_menu))

        if not menu_manager.success:
            print(f'{RED}{menu_manager.message_error}{RESET}\n')
            self.view_main_menu()
        else:
            self.view_menus(self.menus[menu_manager.number_menu_valid])

    def view_menus(self, menu_options):
        self.view_all_menus(menu_options)
        menu_selected = input(SELECTED_MESSAGE)
        menu_manager = MenuManager()
        menu_manager.check_value_submit(menu_selected, len(menu_options))

        if not menu_manager.success:
            print(f'{RED}{menu_manager.message_error}{RESET}\n')
            self.view_menus(menu_options)
        else:
            redirect = menu_manager.redirect_method(menu_options[menu_manager.number_menu_valid]['method'])
            if redirect == 'menu_back':
                self.view_main_menu()

    @staticmethod
    def view_all_menus(options):
        for option in options:
            print(f'{option} - {options[option]['text']}')



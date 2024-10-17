from utils.constants import SELECTED_MESSAGE, ERROR_MENU


class MenusView:
    def __init__(self, menu):
        self.menu = menu

    def view_main_menu(self):
        self.template_menu()
        menu_selected = input(SELECTED_MESSAGE)
        return menu_selected

    def template_menu(self):
        for option in self.menu:
            print(f'{self.menu[option]["text"]}')

    @staticmethod
    def view_error():
        print(ERROR_MENU)

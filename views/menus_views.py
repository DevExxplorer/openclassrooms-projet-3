from utils.constants import SELECTED_MESSAGE, ERROR_MENU


class MenusView:
    """
        Vues des différents menus
    """
    def __init__(self, menu):
        """
            Construct

            Parameters

            Menu(Array) : Données du menu
        """
        self.menu = menu

    def view_main_menu(self):
        """
            Vue du menu principal
        """
        self.template_menu()
        menu_selected = input(SELECTED_MESSAGE)
        return menu_selected

    def template_menu(self):
        """
            Vue du choix du menu séléctionné a afficher
        """
        for option in self.menu:
            print(f'{self.menu[option]["text"]}')

    @staticmethod
    def view_error():
        """
           Affichage des messages d'erreurs
        """
        print(ERROR_MENU)

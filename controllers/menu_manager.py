from views.menus_views import MenusView
from controllers.player_manager import PlayerManager
from controllers.tournament_manager import TournamentManager


class MenuManager:
    def __init__(self, menu):
        self.menu = menu
        self.selected_main_menu = ''

    def main_menu(self):
        menus_view = MenusView(self.menu)
        self.selected_main_menu = menus_view.view_main_menu()

        if self.selected_main_menu in self.menu:
            self.submenu_init()
        else:
            menus_view.view_error()
            return self.main_menu()

    def submenu_init(self):
        submenu = self.menu[self.selected_main_menu]['submenu']
        menus_view = MenusView(submenu)
        submenu_selected = menus_view.view_main_menu()

        if submenu_selected in submenu:
            action_menu = submenu[submenu_selected]['action']

            slug_menu = self.menu[self.selected_main_menu]['slug']
            if slug_menu == 'player':
                player_manager = PlayerManager(self)
                return getattr(player_manager, action_menu)()
            elif slug_menu == 'tournament':
                tournament_manager = TournamentManager(self)
                return getattr(tournament_manager, action_menu)()
            else:
                print('Erreur dans la class MenuManager')
        else:
            menus_view.view_error()
            return self.submenu_init()

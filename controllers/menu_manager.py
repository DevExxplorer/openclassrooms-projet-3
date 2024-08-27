from views.players_view import players_view, add_new_player


class MenuManager:
    def __init__(self, number_menu):
        self.number_menu = number_menu
        self.choice_valid = True
        self.message_error = ''
        self.execute_choice()

    def execute_choice(self):
        list_choices = {
            1: self.get_players,
            2: self.get_tournaments,
            3: self.get_tournament,
            4: self.players_by_tournament,
            5: self.infos_tournament,
            6: self.add_player
        }

        if self.number_menu in list_choices:
            return list_choices[self.number_menu]()
        else:
            self.choice_valid = False
            self.message_error = 'Erreur: Le nombre séléctionné ne fait pas partit des choix'

    @staticmethod
    def get_players():
        players_view()

    @staticmethod
    def get_tournaments():
        print("Liste de tous les tournois")
        # return 'get_tournament'

    @staticmethod
    def get_tournament():
        pass

    @staticmethod
    def players_by_tournament():
        pass

    @staticmethod
    def infos_tournament():
        pass

    @staticmethod
    def add_player():
        add_new_player()

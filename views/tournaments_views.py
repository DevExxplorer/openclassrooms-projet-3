from utils.constants import NEW_TOURNAMENT, MAIN_MENU, INPUTS_PLAYERS
from controllers.player_manager import PlayerManager
from tabulate import tabulate


class TournamentsViews:
    """
        Vue des différents choix du menu Tournoi
    """
    @staticmethod
    def view_list(headers, body):
        """
            Affichage de la liste des tournois
        """
        print(tabulate(body, headers=headers, tablefmt="double_grid"))

    def view_create(self, data):
        """
            Affichage des champs pour la création d'un tournoi
        """
        print(NEW_TOURNAMENT)

        for input_data in data:
            if 'slug' in input_data and input_data['slug'] == 'players':
                PlayerManager(MAIN_MENU).view_players(False)

            if not input_data['valid']:
                input_data['value'] = self.get_user_input(input_data['name'])

        return data

    @staticmethod
    def get_user_input(field_name):
        return input(f'{field_name}: ').strip()

    def input_info_tournament(self):
        """
            Affichage d'un champs input
        """
        return self.get_user_input('Id du tournoi à afficher')

    @staticmethod
    def view_info_tournament(data_tournament):
        """
            Affichage des infos du tournoi
        """
        print(f'\n{data_tournament["name"]}')
        print(
            f'Le tournoi se déroulera à {data_tournament["place"]} '
            f'du {data_tournament["dates"][0]} au {data_tournament["dates"][1]}\n'
        )

    @staticmethod
    def view_players_tournament(data_tournament):
        """
            Affichage de la liste des joueurs d'un tournoi
        """
        data = PlayerManager.get_list_players_by_tournament(data_tournament)
        headers = []
        for input_player in INPUTS_PLAYERS:
            headers.append(input_player['name'])
        body = [list(player.values()) for player in data]
        print(tabulate(body, headers=headers, tablefmt="double_grid"))

    @staticmethod
    def view_start_tournament():
        """
            Affichage d'un input pour selectionné l'id d'un tournoi
        """
        name_tournament = input('Id du tournoi que vous souhaitez démarrer ou passer au round suivant: ')
        return name_tournament

    @staticmethod
    def view_data_tournament():
        name_tournament = input('Id du tournoi que vous souhaitez afficher: ')
        return name_tournament

    @staticmethod
    def view_round(data_current_round):
        """
            Affichage nom du round
        """
        print(f'\nRound {data_current_round} \n')

    @staticmethod
    def message_user(message):
        """
            Affichage message personnalisé

            Parameters

            message(str): Texte à afficher
        """
        print(message)

    @staticmethod
    def result_match(players):
        """
            Affichage du match
            et input pour séléctionner le resultat du match
        """
        print(f'{players[0]["name_player"]} vs {players[1]["name_player"]}')
        result = input(f"Résultat du joueur {players[0]['name_player']} [1: Victoire / 0.5: Match nul / 0: Défaite]: ")
        return result

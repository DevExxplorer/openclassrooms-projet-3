BLUE = '\033[34m'
RED = '\033[31m'
GREEN = '\033[32m'
BOLD = '\033[1m'
RESET = '\033[0m'
UNDERLINE = '\033[4m'

MESSAGE_MENU = f'{BLUE}{BOLD}{UNDERLINE}Bienvenue sur notre application d\'échecs{RESET}\n'
SELECTED_MESSAGE = f'\n{BLUE}{BOLD}Veuillez séléctionner votre choix parmi les numéros ci-dessus: {RESET}'
NEW_PLAYER = f'\n{UNDERLINE}Ajout d\'un nouveau joueur{RESET}'

MAIN_MENU = {
    1: {'text': 'Accéder aux menus des joueurs'},
    2: {'text': 'Accéder aux menus des tournois'},
}

ALL_MENUS = {
    1: {
        1: {'text': 'Création d\'un nouveau joueur', 'method': 'create_player'},
        2: {'text': 'Liste de tous les joueurs par ordre alphabétique', 'method': 'view_players'},
        3: {'text': 'Retour au menu précédent', 'method': 'menu_back'}
    },
    2: {
        1: {'text': 'Création d\'un nouveau tournoi', 'method': ''},
        2: {'text': 'Liste de tous les tournois', 'method': ''},
        3: {'text': 'Nom et dates d’un tournoi donné', 'method': ''},
        4: {'text': 'Liste des joueurs du tournoi par ordre alphabétique', 'method': ''},
        5: {'text': 'Liste de tous les tours du tournoi et de tous les matchs du tour', 'method': ''},
        6: {'text': 'Retour au menu précédent', 'method': 'menu_back'},
    },
}
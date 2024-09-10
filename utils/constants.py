BLUE = '\033[34m'
RED = '\033[31m'
GREEN = '\033[32m'
BOLD = '\033[1m'
RESET = '\033[0m'
UNDERLINE = '\033[4m'

MESSAGE_MENU = f'{BLUE}{BOLD}{UNDERLINE}Bienvenue sur notre application d\'échecs{RESET}\n'
ERROR_MENU = f'\n {RED}{BOLD}Erreur: La valeur séléctionnée doit être un numéro du menu {RESET}\n'
SELECTED_MESSAGE = f'\n{BLUE}{BOLD}Veuillez séléctionner votre choix parmi les numéros ci-dessus: {RESET}'
NEW_PLAYER = f'\n{UNDERLINE}Ajout d\'un nouveau joueur{RESET}'
MENUS = {
    '1': {
                'text': '1 - Accéder aux menus des joueurs',
                'submenu': {
                    '1': {
                        'text': '1 - Création d\'un nouveau joueur',
                        'action': 'create_player'
                    },
                    '2': {
                        'text': '2 - Liste de tous les joueurs par ordre alphabétique',
                        'action': 'view_players'
                    },
                    '3': {
                        'text': '3 - Retour au menu précédent',
                        'action': 'menu_back'
                    }
                }
            },
    '2': {
                'text': '2 - Accéder aux menus des tournois',
                'submenu':  {
                    '1': {
                        'text': '1 - Création d\'un nouveau tournoi',
                        'action': 'create_tournament'
                    },
                    '2': {
                        'text': '2 - Liste de tous les tournois',
                        'action': ''
                    },
                    '3': {
                        'text': '3 - Nom et dates d’un tournoi donné',
                        'action': ''
                    },
                    '4': {
                        'text': '4 - Liste des joueurs du tournoi par ordre alphabétique',
                        'action': ''
                    },
                    '5': {
                        'text': '5 - Liste de tous les tours du tournoi et de tous les matchs du tour',
                        'action': ''
                    },
                    '6': {
                        'text': '6 - Retour au menu précédent',
                        'action': 'menu_back'
                    },
                }
            }
}


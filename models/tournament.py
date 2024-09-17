import json
import os

FILENAME = "tournaments.json"


class Tournament:
    def __init__(self, data):
        self.data = data

    def create(self):
        if not os.path.isdir('data'):
            os.mkdir('data')

        list_tournament = self.read()

        result = {tournament['slug']: tournament['value'] for tournament in self.data}
        list_tournament.append(result)

        try:
            with open("data/" + FILENAME, "w", encoding="utf-8") as file:
                json.dump(list_tournament, file, ensure_ascii=False, indent=4)
                return {'success': True, 'message': 'Le nouveau tournoi a bien été créé'}
        except Exception as e:
            return {'success': False, 'message': f'Erreur : {e}'}

    @staticmethod
    def read():
        file_path = os.path.join("data", FILENAME)

        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    return sorted(json.load(file), key=lambda tournament: tournament['name'])
            except json.JSONDecodeError:
                print(f"Erreur : Le fichier {FILENAME} contient des données JSON non valides.")
        else:
            print(f"Erreur : Le fichier {FILENAME} n'existe pas.")

        return []

    
    """  
        def start_tournament(self):
            while self.current_round <= self.number_round:
                print(f'\nTour {self.current_round}:\n')
    
                round_tournament = Round(self.list_players)
                round_tournament.start_round()
                round_tournament.end_round()
    
                input('\nPasser au prochain round (Appuyer sur n\'importe qu\'elle touche: ')
                self.current_round = self.current_round + 1
    """
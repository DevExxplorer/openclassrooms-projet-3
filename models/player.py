import json
import os

FILENAME = "players.json"


class Player:
    @staticmethod
    def read():
        file_path = os.path.join("data", FILENAME)

        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    return sorted(json.load(file), key=lambda player: player['lastname'])
            except json.JSONDecodeError:
                print(f"Erreur : Le fichier {FILENAME} contient des données JSON non valides.")
        else:
            print(f"Erreur : Le fichier {FILENAME} n'existe pas.")

        return []

    @staticmethod
    def create(new_data):
        if not os.path.isdir('data'):
            os.mkdir('data')

        list_players = Player.read()
        list_players.append(new_data)

        try:
            with open("data/" + FILENAME, "w", encoding="utf-8") as file:
                json.dump(list_players, file, ensure_ascii=False, indent=4)
                return {'success': True, 'message': 'Le nouveau joueur a bien été créé'}
        except Exception as e:
            return {'success': False, 'message': f'Erreur : {e}'}

    @staticmethod
    def get_name_by_id_chess(chess_id):
        list_players = Player.read()

        for player in list_players:
            if player['chess_id'] == chess_id:
                return player['lastname']
        return "Joueur introuvable"

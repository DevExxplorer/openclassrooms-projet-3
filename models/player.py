import json
import os

FILENAME = "players.json"


class Player:
    """
        Class Player pour gérer l'envoi des données au fichier Json player.json
    """
    @staticmethod
    def read():
        """
            Lecture des données JSON
        """
        file_path = os.path.join("data", FILENAME)

        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    return sorted(json.load(file), key=lambda player: player['lastname'])
            except json.JSONDecodeError:
                print(f"Erreur : Le fichier {FILENAME} contient des données JSON non valides.")

        return []

    @staticmethod
    def create(data):
        """
            Création/Ajout des données JSON

            Parameters

            data(Array): Données à ajouter au fichier json
        """
        file_path = os.path.join("data", FILENAME)
        if not os.path.exists(file_path):
            os.mkdir('data')

        list_players = Player.read()
        result = {player['slug']: player['value'] for player in data}
        list_players.append(result)

        try:
            with open("data/" + FILENAME, "w", encoding="utf-8") as file:
                json.dump(list_players, file, ensure_ascii=False, indent=4)
                return {'success': True, 'message': 'Le nouveau joueur a bien été créé'}
        except Exception as e:
            return {'success': False, 'message': f'Erreur : {e}'}

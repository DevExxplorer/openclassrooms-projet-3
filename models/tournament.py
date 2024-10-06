import json
import os


FILENAME = "tournaments.json"


class Tournament:
    def create(self, data):
        # Vérifie que le dossier data existe
        if not os.path.isdir('data'):
            os.mkdir('data')

        list_tournament = self.read()
        result = {tournament['slug']: tournament['value'] for tournament in data}
        list_tournament.append(result)
        print(list_tournament)
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

    def update(self, name_tournament, new_data):
        list_tournament = self.read()
        updated = False

        # Parcours de la liste des tournois pour trouver celui à mettre à jour
        for tournament in list_tournament:
            if tournament['name'] == name_tournament:
                tournament.update(new_data)
                updated = True
                break

        if updated:
            try:
                # Mise à jour du fichier JSON avec les nouvelles données
                with open("data/" + FILENAME, "w", encoding="utf-8") as file:
                    json.dump(list_tournament, file, ensure_ascii=False, indent=4)
                return {'success': True, 'message': 'Le tournoi a bien été mis à jour'}
            except Exception as e:
                return {'success': False, 'message': f'Erreur lors de la mise à jour : {e}'}
        else:
            return {'success': False, 'message': 'Le tournoi spécifié n\'existe pas'}


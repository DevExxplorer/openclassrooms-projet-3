from datetime import datetime


class InputValidator:
    def __init__(self, data):
        self.data = data

    def validate(self):
        for input_data in self.data:
            if input_data['value'] != '':
                if input_data['slug'] in 'date_event':
                    self.validate_date(input_data)
                else:
                    input_data['valid'] = True
            else:
                input_data['error'] = 'Vous n\'avez pas rempli le champs'

        return self.data

    @staticmethod
    def validate_date(input_data):
        dates_event = input_data['value'].replace(' ', '').split(',')
        try:
            date1 = datetime.strptime(dates_event[0], '%d/%m/%Y')
            date2 = datetime.strptime(dates_event[1], '%d/%m/%Y')
            if date1 > date2:
                input_data['valid'] = False
                input_data['error'] = 'Erreur: La date de fin se termine avant la date de début'
            else:
                input_data['valid'] = True
        except ValueError:
            input_data['error'] = 'Erreur: le format des dates est incorrect. Utilisez JJ/MM/AAAA.'

        return input_data

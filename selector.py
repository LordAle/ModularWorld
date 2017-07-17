import random
import catalog

class Selector:

    def __init__(self, selection):
        self.selection = selection.copy()  # Note: This copy is shallow, e.i. objects inside it are references to the original
        self.remove_error()

    def simple(self):
        selection_list = list(self.selection.values())
        return random.choice(selection_list)

    def weighted(self, total_odds):
        random_nb = random.randint(1, total_odds)
        for key, value in self.selection.items():
            random_nb = random_nb - value.odds
            if random_nb <= 0:
                return value
        self.error_message()
        raise Exception  # Should never get here during execution

    def building_kind(self, city_pop):
        total_odds = 0
        to_delete = []
        for key, value in self.selection.items():
            if value.min_pop > city_pop:
                to_delete.append(key)
            else:
                total_odds = total_odds + value.odds
        for key in to_delete:
            del self.selection[key]
        return self.weighted(total_odds)

    def minority_culture(self, main_culture):
        self.selection = {name: self.selection[name] for name in main_culture.other_cultures}
        total_odds = 0
        for key, value in self.selection.items():
            total_odds = total_odds + value.other_cultures_odds
        return self.weighted(total_odds)

    def remove_error(self):
        if 'Error' in self.selection:
            del self.selection['Error']
        if 'Default' in self.selection:
            del self.selection['Default']

    def error_message(self):
        print('Selector has encountered an error')

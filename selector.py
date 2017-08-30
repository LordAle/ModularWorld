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

    def profession(self, odds, in_city):
        total_odds = 0
        ok_prof = []
        prof_odds = []
        for index, item in enumerate(self.selection):
            if item not in in_city.taken_jobs and self.check_geography(item, in_city):
                ok_prof.append(item)
                prof_odds.append(odds[index])
                total_odds += odds[index]

        random_nb = random.randint(1, total_odds)
        for index, item in enumerate(ok_prof):
            random_nb = random_nb - prof_odds[index]
            if random_nb <= 0:
                return item
        self.error_message()
        raise Exception  # Should never get here during execution

    def check_geography(self, prof, in_city):
        if not prof.geo_restric:
            return True
        else:
            if prof.geo_restric == 'Forest' and in_city.forest:
                return True
            elif prof.geo_restric == 'Plain' and in_city.plain:
                return True
            elif prof.geo_restric == 'River' and in_city.river:
                return True
            elif prof.geo_restric == 'Sea' and in_city.sea:
                return True
            elif prof.geo_restric == 'Mountain' and in_city.mountain:
                return True
            elif prof.geo_restric == 'Mine' and in_city.mine:
                return True
            elif prof.geo_restric == 'Water':
                if in_city.sea or in_city.river:
                    return True
            else:
                return False

    def social_group(self, character):
        incompatible = []
        for key, value in self.selection.items():
            if value.strict_inheritance:  # Remove all social groups with strict inheritance
                incompatible.append(key)
                continue
            if value.gender and value.gender != character.gender:  # If there is a gender condition, check character gender
                incompatible.append(key)
                continue
            if value.wealth:  # Check if character wealth is in correct range
                if not self.check_wealth(character.wealth, value.wealth):
                    incompatible.append(key)
                    continue
            if value.attributes:
                if not self.check_attributes(character.attributes, value.attributes):
                    incompatible.append(key)
                    continue
            if value.moralities:
                if not self.check_moralities(character.moralities, value.moralities):
                    incompatible.append(key)
                    continue
            if value.cultures:
                if not self.check_culture(character.culture, value.cultures):
                    incompatible.append(key)
                    continue

        for key in incompatible:
            del self.selection[key]
        try:
            return random.choice(list(self.selection.values()))
        except:
            print('Error in social group selection, no compatible choice were available')

    @staticmethod
    def check_wealth(wealth, target):
        if '<' in target:
            check_tuple = target.partition('<')
            if wealth < float(check_tuple[2]):
                return True
            else:
                return False
        elif '>' in target:
            check_tuple = target.partition('>')
            if wealth > float(check_tuple[2]):
                return True
            else:
                return False
        else:
            print('Error in wealth prerequisite of social group')
            return True

    @staticmethod
    def check_attributes(attributes, targets):  # Definitely not optimized...
        for target in targets:
            print(target)
            if '<' in target:
                check_list = list(target.partition('<'))
                for index, item in enumerate(check_list):
                    check_list[index] = item.strip()
                for index, item in enumerate(catalog.attributes):
                    if item.name == check_list[0]:
                        attr_index = index
                        break
                try:
                    if attributes[attr_index] < float(check_list[2]):
                        return True
                    else:
                        return False
                except:
                    print('Error in attributes prerequisite of social group')
                    return True
            if '>' in target:
                check_list = list(target.partition('>'))
                for index, item in enumerate(check_list):
                    check_list[index] = item.strip()
                for index, item in enumerate(catalog.attributes):
                    if item.name == check_list[0]:
                        attr_index = index
                        break
                try:
                    if attributes[attr_index] > float(check_list[2]):
                        return True
                    else:
                        return False
                except:
                    print('Error in attributes prerequisite of social group')
                    return True

    @staticmethod
    def check_moralities(moralities, targets):
        for target in targets:
            if '<' in target:
                check_list = list(target.partition('<'))
                for index, item in enumerate(check_list):
                    check_list[index] = item.strip()
                for index, item in enumerate(catalog.moralities):
                    if item.name == check_list[0]:
                        attr_index = index
                        break
                try:
                    if moralities[attr_index] < float(check_list[2]):
                        return True
                    else:
                        return False
                except:
                    print('Error in moralities prerequisite of social group')
                    return True
            if '>' in target:
                check_list = list(target.partition('>'))
                for index, item in enumerate(check_list):
                    check_list[index] = item.strip()
                for index, item in enumerate(catalog.moralities):
                    if item.name == check_list[0]:
                        attr_index = index
                        break
                try:
                    if moralities[attr_index] > float(check_list[2]):
                        return True
                    else:
                        return False
                except:
                    print('Error in moralities prerequisite of social group')
                    return True

    @staticmethod
    def check_culture(culture, target):
        target_list = target.split(',')
        for index, item in enumerate(target_list):
            target_list[index] = item.strip()
        if culture.name in target_list:
            return True
        else:
            return False

    def remove_error(self):
        if 'Error' in self.selection:
            del self.selection['Error']
        if 'Default' in self.selection:
            del self.selection['Default']

    def error_message(self):
        print('Selector has encountered an error')

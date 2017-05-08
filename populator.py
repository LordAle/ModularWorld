import character
import family
import catalogs_character
import db_connector
import random
import math

class Populator():
    """ Use this object to automatically populate a building with random characters. Uses compatible floating
    characters if available """

    def __init__(self,  core_dict, in_building, in_building_id, in_city, in_city_id, loader):
        self.loader = loader
        self.in_city = in_city
        self.in_city_id = in_city_id
        self.in_building = in_building
        self.in_building_id = in_building_id
        self.traveller_city_id = self.get_traveller_id()
        self.traveller_floating_id = self.get_floating_building_id(self.traveller_city_id)
        self.floating_id = self.get_floating_building_id(self.in_city_id)
        self.core_dict = core_dict
        self.core_character = character.Character(in_city=self.in_city, in_building=self.in_building)
        self.core_character_id = None
        self.constructor_info = catalogs_character.profession[in_building.kind][in_building.subkind]
        self.role = []
        self.profession = []
        self.floating_characters = []
        self.new_characters = []

    def populate(self):
        self.build_structure()
        self.extract_floating_characters(self.floating_id)
        self.extract_floating_characters(self.traveller_floating_id)
        self.set_core()
        self.purge_structure('Master')
        self.set_others()
        self.rename_building()

    def build_structure(self):
        for data in self.constructor_info:
            amount = self.get_number(data['Quantity'][0], data['Quantity'][1])
            possible_profession = self.build_profession_list(data)
            for x in range(amount):
                self.role.append(data['Role'])
                if data['Role'] == 'Master' and self.core_dict['profession'] != 'Random':
                    self.profession.append(self.core_dict['profession'])
                else:
                    self.profession.append(random.choice(possible_profession))

                if data['Role'] == 'Unique':
                    possible_profession = self.remove_values_from_list(possible_profession, self.profession[-1])
                if possible_profession is False:
                    break

    def purge_structure(self, purged_role):
        to_purge = None
        purged = False
        while purged is False:
            for index, role in enumerate(self.role):
                if role == purged_role:
                    to_purge = index
            if type(to_purge) is int:
                del self.role[to_purge]
                del self.profession[to_purge]
                to_purge = None
            else:
                purged = True

    def extract_floating_characters(self, floating_id):
        connector = db_connector.Character_Connector(self.loader)
        self.floating_characters = self.floating_characters + connector.load_from_db('building_id', floating_id)
        connector.close_session()

    def get_floating_building_id(self, city_id):
        connector = db_connector.Building_Connector(self.loader)
        floating_list = connector.load_from_db('kind', 'Floating')
        connector.close_session()
        for floating in floating_list:
            if floating.city_id == city_id:
                return floating.id
            else:
                continue
        return Exception  # possibility to add method call to create floating building in city

    def get_traveller_id(self):
        connector = db_connector.City_Connector(self.loader)
        traveller_city = connector.load_from_db('kind', 'Traveller')
        connector.close_session()
        traveller_city_id = traveller_city[0].id

        return traveller_city_id

    def set_core(self):
        existing_core = self.search_for_core()
        if existing_core is character.Character:
            self.core_character = existing_core
            self.core_character.set_building_id(self.in_building_id)
            self.update_character(self.core_character.id, 'Master', self.in_building_id, new_city_id=self.in_city_id)
        else:
            profession = self.profession[self.get_core_index()]
            self.core_character.set_core_from_dialog(self.core_dict, profession)
            self.core_character.set_building_id(self.in_building_id)
            self.core_character.set_city_id(self.in_city_id)
            new_family_id = self.add_family(self.core_character.fname)
            self.core_character.set_family_id(new_family_id)
            self.core_character_id = self.add_character(self.core_character)

    def set_others(self):
        for added_role, added_profession in zip(self.role, self.profession):
            added_character = None
            existing_character = None
            if added_role == 'Spouse':
                existing_character = self.search_for_spouse(added_profession)
            elif added_role != 'Child':
                existing_character = self.search_for_other(added_profession)

            if type(existing_character) is character.Character:
                self.update_character(existing_character.id, added_role, self.in_building_id, new_city_id=self.in_city_id)
                self.floating_characters.remove(existing_character)

            else:
                added_character = character.Character(in_city=self.in_city, in_building=self.in_building,
                                                      core=self.core_character)
                added_character.set_autopopulate(added_role, added_profession)

                # Check if child are still at home or have left
                if added_role == 'Child' and added_character.age >= catalogs_character.ages[added_character.race][0] \
                        and random.randint(1,10) != 1:
                    if random.randint(1,5) == 1:
                        added_character.set_building_id(self.traveller_floating_id)
                    else:
                        added_character.set_building_id(self.floating_id)
                else:
                    added_character.set_building_id(self.in_building_id)

                # Set correct city_id
                if added_character.building_id == self.traveller_floating_id:
                    added_character.set_city_id(self.traveller_city_id)
                else:
                    added_character.set_city_id(self.in_city_id)

                if added_role == 'Child':
                    added_character.set_family_id(self.core_character.family_id)

                self.add_character(added_character)

    def get_number(self, distribution, value):
        if distribution == 'One':
            if random.random() <= value:
                return 1
            else:
                return 0
        elif distribution == 'Flat':
            return random.randint(value[0],value[1])
        elif distribution == 'Normal':
            return max(0, math.ceil(random.gauss(value[0],value[1])))
        else:
            return Exception

    def build_profession_list(self, data):
        profession_list = []
        for x in range(len(data['Profession'])):
            for y in range(data['Weight'][x]):
                if self.test_geography(data['Geography'][x]):
                    profession_list.append(data['Profession'][x])
                else:
                    break
        return profession_list

    def test_geography(self, feature):
        if feature == 'Plains':
            return self.in_city.plains
        elif feature == 'Forest':
            return self.in_city.forests
        elif feature == 'River':
            return self.in_city.river
        elif feature == 'Sea':
            return self.in_city.sea
        elif feature == 'Mountains':
            return self.in_city.mountains
        elif feature == 'Mines':
            return self.in_city.mines
        elif feature == 'Water':
            if self.in_city.river or self.in_city.sea:
                return True
            else:
                return False
        else:
            return True

    def remove_values_from_list(self, a_list, val):
        return [value for value in a_list if value != val]

    def search_for_core(self):
        core_index = self.get_core_index()
        for looking_at in self.floating_characters:
            if looking_at.profession == self.profession[core_index]:
                return looking_at
            else:
                continue
        return False

    def get_core_index(self):
        try:
            core_index = self.role.index('Master')
            return core_index
        except:
            return Exception

    def search_for_spouse(self, profession):
        for looking_at in self.floating_characters:
            if (looking_at.profession == profession) and (looking_at.race == self.core_character.race):
                if looking_at.gender != self.core_character.gender:
                    return looking_at
                else:
                    continue
            else:
                continue
        return False

    def search_for_other(self, profession):
        for looking_at in self.floating_characters:
            if looking_at.profession == profession:
                return looking_at
            else:
                continue
        return False

    def update_character(self, character_id, new_role, new_building_id, new_city_id=None):
        connector = db_connector.Character_Connector(self.loader)
        connector.update_entry(character_id, 'role', new_role)
        connector.update_entry(character_id, 'building_id', new_building_id)
        if new_city_id:
            connector.update_entry(character_id, 'city_id', new_city_id)
        connector.close_session()

    def add_character(self, added_character):
        connector = db_connector.Character_Connector(self.loader)
        new_character_id = connector.write_to_db(added_character)
        connector.close_session()
        return new_character_id

    def rename_building(self):
        new_name = self.core_character.name + ' ' + self.core_character.fname + ' ' + self.in_building.kind
        connector = db_connector.Building_Connector(self.loader)
        connector.update_entry(self.in_building_id, 'name', new_name)
        connector.close_session()

    def add_family(self, family_name):
        new_family = family.Family(family_name)

        connector = db_connector.Family_Connector(self.loader)
        family_id = connector.write_to_db(new_family)
        connector.close_session()
        return family_id

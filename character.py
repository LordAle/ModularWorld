import random
import math
import catalogs_character
import catalogs_character_names
import catalogs_profession
import catalogs_building
import role_professions


class Character():

    names_list = ['Id', 'Name', 'Family', 'Race', 'Gender', 'Age', 'Role', 'Profession', 'Wealth', 'Class', 'Level',
                  'Family', 'Building', 'City', 'Visiting']

    def __init__(self, in_city=None, in_building=None, core=None):
        self.id = None
        self.name = 'Default name'
        self.fname = 'Default fname'
        self.race = 'Default race'
        self.gender = 'Default gender'
        self.age = 0
        self.role = 'Default role'
        self.profession = 'Default profession'
        self.wealth = 'Default Wealth'
        self.classe = 'Default class'
        self.level = 0
        self.family_id = None
        self.city_id = None
        self.building_id = None
        self.visiting_id = None
        self.in_city = in_city
        self.in_building = in_building
        self.core = core
        self.update_value_list()

    def set_from_dialog(self, param):
        # Generic function to add character from dialog
        self.set_role(param['role'])
        self.set_race(param['race'])
        self.set_gender(param['gender'])
        self.set_name(param['name'])
        self.set_fname(param['fname'])
        self.set_age(param['age'])
        self.set_profession(param['profession'])
        self.set_wealth(param['wealth'])
        self.set_class(param['class'])
        self.set_level(param['level'])

    def set_core_from_dialog(self, param, profession):
        # Method used to create first character in a building
        self.set_role(param['role'])
        self.set_race(param['race'])
        self.set_gender(param['gender'])
        self.set_name(param['name'])
        self.set_fname(param['fname'])
        self.set_age(param['age'])
        self.set_profession(profession)
        self.set_wealth(param['wealth'])
        self.set_class(param['class'])
        self.set_level(param['level'])

    def set_autopopulate(self, role, profession):
        # Method used to create a character during autopopulate process
        self.set_role(role)
        self.set_race('Random')
        self.set_gender('Random')
        self.set_name('Random')
        self.set_fname('Random')
        self.set_age('Random')
        self.set_profession(profession)
        self.set_wealth('Random')
        self.set_class('Random')
        self.set_level('Random')

    def set_role(self, role):
        self.role = role

    def set_race(self, race):
        try:
            self.race = race
            if self.race not in catalogs_character.races:
                if self.role == 'Spouse' or self.role == 'Child' or self.in_city.main_race not in catalogs_character.races:
                    self.race = self.core.race
                else:
                    is_main_race = random.randrange(10)
                    if is_main_race != 9:
                        self.race = self.in_city.main_race
                    else:
                        self.race = random.choice(catalogs_character.races)
        except:
            self.race = 'Error'

    def set_gender(self, gender):
        try:
            self.gender = gender
            if self.gender not in catalogs_character.genders:
                if self.role == 'Spouse':
                    if self.core.gender == 'Male':
                        self.gender = 'Female'
                    elif self.core.gender == 'Female':
                        self.gender = 'Male'
                else:
                    self.gender = random.choice(catalogs_character.genders)
        except:
            self.gender = 'Error'

    def set_name(self, name):
        try:
            self.name = name
            if self.name == 'Random' or self.name == 'random':
                self.name = random.choice(catalogs_character_names.names[self.gender][self.race])
        except:
            self.name = 'Error'

    def set_fname(self, fname):
        try:
            self.fname = fname
            if self.fname == 'Random' or self.fname == 'random':
                if self.role == 'Spouse' or self.role == 'Child':
                    self.fname = self.core.fname
                else:
                    self.fname = random.choice(catalogs_character_names.fnames[self.race])
        except:
            self.fname = 'Error'

    def set_age(self, age):
        try:
            self.age = age
            if self.age == 'Random' or self.age == 'random':
                if self.role == 'Spouse':
                    self.age = max(catalogs_character.ages[self.race][0], self.core.age + math.floor(random.gauss(0, 5)))
                elif self.role == 'Child':
                    self.age = max(0, self.core.age - max(catalogs_character.ages[self.race][0], math.floor(random.gauss(
                        catalogs_character.ages[self.race][0]+5, 5))))
                else:
                    self.age = max(catalogs_character.ages[self.race][0] + random.randint(0, 4), math.floor(random.gauss(
                        catalogs_character.ages[self.race][1]/2, catalogs_character.ages[self.race][0])))
            self.age = int(self.age)
        except:
            self.age = -1

    def set_profession(self, profession):
        try:
            self.profession = profession
            if self.profession == 'Random' or self.profession == 'random':
                profession_list = self.construct_profession(self.in_building, self.in_city, self.role)
                self.profession = random.choice(profession_list)
            if self.profession == 'Same':
                self.profession = self.core.profession
        except:
            self.profession = 'Error'

    def set_wealth(self, wealth):
        try:
            self.wealth = wealth
            if self.wealth == 'Random' or self.wealth == 'random':
                wealth_odds = [x for x in catalogs_profession.professions if x.name == self.profession]
                wealth_odds = wealth_odds[0].wealth
                if (wealth_odds % 1) >= random.random():
                    wealth_odds = math.ceil(wealth_odds)
                else:
                    wealth_odds = math.floor(wealth_odds)
                self.wealth = catalogs_character.wealth[int(wealth_odds)]
        except:
            self.wealth = 'Error'

    def set_class(self, classe):
        try:
            self.classe = classe
            if self.classe == 'Random' or self.classe == 'random':
                class_list = self.construct_class_list(self.profession)
                self.classe = random.choice(class_list)
        except:
            self.classe = 'Error'

    def set_level(self, level):
        try:
            self.level = level
            if self.level == 'Random' or self.level == 'random':
                self.level = random.paretovariate(2)
                self.level = math.floor(self.level)
            self.level = int(self.level)
        except:
            self.level = -1

    def set_building_id(self, building_id):
        self.building_id = building_id

    def set_city_id(self, city_id):
        self.city_id = city_id

    def set_family_id(self, family_id):
        self.family_id = family_id

    def set_visiting_id(self, visiting_id):
        self.visiting_id = visiting_id

    def set_from_db(self, base_character):
        self.id = base_character.id
        self.name = base_character.name
        self.fname = base_character.fname
        self.race = base_character.race
        self.gender = base_character.gender
        self.age = base_character.age
        self.role = base_character.role
        self.profession = base_character.profession
        self.wealth = base_character.wealth
        self.classe = base_character.classe
        self.level = base_character.level
        self.family_id = base_character.family_id
        self.city_id = base_character.city_id
        self.building_id = base_character.building_id
        self.visiting_id = base_character.visiting_id
        self.update_value_list()

    def update_value_list(self):
        self.values_list = [self.id, self.name, self.fname, self.race, self.gender, self.age, self.role,
                            self.profession, self.wealth, self.classe, self.level, self.family_id, self.city_id,
                            self.building_id, self.visiting_id]

    def construct_profession(self, in_building, in_city, role):
        good_preset = None
        preset_list = [x.groups for x in catalogs_building if x.name == in_building.subkind]
        for preset in preset_list:
            if preset.role == role:
                good_preset = preset
                break
            else:
                continue
        if type(good_preset) is role_professions.RoleProfessions:
            possible_job = good_preset.professions
            odds = good_preset.odds
            profession_list = []
            for x in range(len(possible_job)):
                required_feature = [x for x in catalogs_profession.professions if x == possible_job[x]]
                required_feature = required_feature[0].geo_restric
                for y in range(odds[x]):
                    if self.test_geography(required_feature, in_city):
                        profession_list.append(possible_job[x].name)
                    else:
                        break
        else:
            profession_list = ['No preset profession available']
        return profession_list

    def construct_class_list(self, profession):
        class_list = []
        profession_object = next((x for x in catalogs_profession.professions if x.name == profession), [])
        for x in range(len(profession_object.class_list)):
            for y in range(profession_object.class_odds[x]):
                class_list.append(profession_object.class_list[x])
        return class_list



    def test_geography(self, feature, in_city):
        if feature == 'Plains':
            return in_city.plains
        elif feature == 'Forest':
            return in_city.forests
        elif feature == 'River':
            return in_city.river
        elif feature == 'Sea':
            return in_city.sea
        elif feature == 'Mountains':
            return in_city.mountains
        elif feature == 'Mines':
            return in_city.mines
        elif feature == 'Water':
            if in_city.river or in_city.sea:
                return True
            else:
                return False
        else:
            return True



import random
import math
import catalogs_character
import catalogs_character_names


class Character():

    names_list = ['Id', 'Name', 'Family', 'Race', 'Gender', 'Age', 'Role', 'Profession', 'Wealth', 'Class', 'Level',
                  'Parent', 'Building', 'City', 'Visiting']

    def __init__(self):
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
        self.parent_id = None
        self.city_id = None
        self.building_id = None
        self.visiting_id = None
        self.update_value_list()

    def set_from_dialog(self, param, core, in_building, in_city):
        # Generic function to add character from dialog

        self.role = param['role']

        self.race = param['race']
        if self.race == 'Random':
            if self.role == 'Child' or in_city.main_race not in catalogs_character.races:
                self.race = core.race
            else:
                is_main_race = random.randrange(10)
                if is_main_race != 9:
                    self.race = in_city.main_race
                else:
                    self.race = random.choice(catalogs_character.races)

        self.gender = param['gender']
        if self.gender == 'Random':
            if self.role == 'Spouse':
                if core.gender == 'Male':
                    self.gender = 'Female'
                elif core.gender == 'Female':
                    self.gender = 'Male'
            else:
                self.gender = random.choice(catalogs_character.genders)

        self.name = param['name']
        if self.name == 'Random':
            self.name = random.choice(catalogs_character_names.names[self.gender][self.race])

        self.fname = param['fname']
        if self.fname == 'Random':
            if self.role == 'Spouse' or 'Child':
                self.fname = core.fname
            else:
                self.fname = random.choice(catalogs_character_names.fnames[self.race])

        self.age = param['age']
        if self.age == 'Random':
            if self.role == 'Spouse':
                self.age = max(18, core.age + random.randint(-5, 15))
            elif self.role == 'Child':
                self.age = max(0, core.age - random.randint(20, 40))
            else:
                self.age = random.randint(catalogs_character.ages[self.race][0], catalogs_character.ages[self.race][1])
            #  Change to normal distribution?
        self.age = int(self.age)

        self.profession = param['profession']
        if self.profession == 'Random':
            profession_list = self.construct_profession(in_building, in_city, self.role)
            self.profession = random.choice(profession_list)


        self.wealth = param['wealth']
        if self.wealth == 'Random':
            try:
                wealth_odds = catalogs_character.profession_info[self.profession]['Wealth']
                if (wealth_odds % 1) >= random.random():
                    wealth_odds = math.ceil(wealth_odds)
                else:
                    wealth_odds = math.floor(wealth_odds)
                self.wealth = catalogs_character.wealth[int(wealth_odds)]
            except:
                self.wealth = 'Error'

        self.classe = param['class']
        if self.classe == 'Random':
            self.classe = 'Random class (placeholder)'

        self.level = param['level']
        if self.level == 'Random':
            self.level = random.paretovariate(2)
            self.level = math.floor(self.level)
        self.level = int(self.level)

        if self.role == 'Child':
            self.parent_id = core.id

    def set_core_from_dialog(self, param, profession, in_building, in_city):
        #Function used to create first character in a building

        self.role = param['role']

        self.race = param['race']
        if self.race == 'Random':
            is_main_race = random.randrange(10)
            if is_main_race != 9:
                self.race = in_city.main_race
        if in_city.main_race not in catalogs_character.races:
            self.race = random.choice(catalogs_character.races)

        self.gender = param['gender']
        if self.gender == 'Random':
            self.gender = random.choice(catalogs_character.genders)

        self.name = param['name']
        if self.name == 'Random':
            self.name = random.choice(catalogs_character_names.names[self.gender][self.race])

        self.fname = param['fname']
        if self.fname == 'Random':
            self.fname = random.choice(catalogs_character_names.fnames[self.race])

        self.age = param['age']
        if self.age == 'Random':
            self.age = random.randint(catalogs_character.ages[self.race][0],catalogs_character.ages[self.race][1])  #
            #  Change to normal distribution?
        self.age = int(self.age)

        self.profession = profession

        self.wealth = param['wealth']
        if self.wealth == 'Random':
            try:
                wealth_odds = catalogs_character.profession_info[self.profession]['Wealth']
                if (wealth_odds % 1) >= random.random():
                    wealth_odds = math.ceil(wealth_odds)
                else:
                    wealth_odds = math.floor(wealth_odds)
                self.wealth = catalogs_character.wealth[int(wealth_odds)]
            except:
                self.wealth = 'Error'

        self.classe = param['class']
        if self.classe == 'Random':
            self.classe = 'Random class (placeholder)'

        self.level = param['level']
        if self.level == 'Random':
            self.level = random.paretovariate(2)
            self.level = math.floor(self.level)
        self.level = int(self.level)

    def set_autopopulate(self, role, profession, core, in_building, in_city):
        # Method used to create a character during autopopulate process

        self.role = role

        if self.role == 'Spouse' or self.role == 'Child' or in_city.main_race not in catalogs_character.races:
            self.race = core.race
        else:
            is_main_race = random.randrange(10)
            if is_main_race != 9:
                self.race = in_city.main_race
            else:
                self.race = random.choice(catalogs_character.races)

        if self.role == 'Spouse':
            if core.gender == 'Male':
                self.gender = 'Female'
            elif core.gender == 'Female':
                self.gender = 'Male'
        else:
            self.gender = random.choice(catalogs_character.genders)

        self.name = random.choice(catalogs_character_names.names[self.gender][self.race])

        if self.role == 'Spouse' or self.role == 'Child':
            self.fname = core.fname
        else:
            self.fname = random.choice(catalogs_character_names.fnames[self.race])

        if self.role == 'Spouse':
            self.age = max(18, core.age + random.randint(-5,15))
        elif self.role == 'Child':
            self.age = max(0, core.age - random.randint(20,40))
        else:
            self.age = random.randint(catalogs_character.ages[self.race][0], catalogs_character.ages[self.race][1])

        self.profession = profession
        if self.profession == 'Same':
            self.profession = core.profession

        try:
            wealth_odds = catalogs_character.profession_info[self.profession]['Wealth']
            if (wealth_odds % 1) >= random.random():
                wealth_odds = math.ceil(wealth_odds)
            else:
                wealth_odds = math.floor(wealth_odds)
            self.wealth = catalogs_character.wealth[int(wealth_odds)]
        except:
            self.wealth = 'Error'

        self.classe = 'Placeholder'

        self.level = random.paretovariate(2)
        self.level = math.floor(self.level)

    def set_building_id(self, building_id):
        self.building_id = building_id

    def set_city_id(self, city_id):
        self.city_id = city_id

    def set_parent_id(self, parent_id):
        self.parent_id = parent_id

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
        self.parent_id = base_character.parent_id
        self.city_id = base_character.city_id
        self.building_id = base_character.building_id
        self.visiting_id = base_character.visiting_id
        self.update_value_list()

    def update_value_list(self):
        self.values_list = [self.id, self.name, self.fname, self.race, self.gender, self.age, self.role,
                            self.profession, self.wealth, self.classe, self.level, self.parent_id, self.city_id,
                            self.building_id, self.visiting_id]

    def construct_profession(self, in_building, in_city, role):
        good_preset = None
        for preset in catalogs_character.profession[in_building.kind][in_building.subkind]:
            if preset['Role'] == role:
                good_preset = preset
                break
            else:
                continue
        if type(good_preset) is dict:
            possible_job = good_preset['Profession']
            weight = good_preset['Weight']
            geography = good_preset['Geography']
            profession_list = []
            for x in range(len(possible_job)):
                for y in range(weight[x]):
                    if self.test_geography(geography[x], in_city):
                        profession_list.append(possible_job[x])
                    else:
                        break
        else:
            profession_list = ['No preset profession available']
        return profession_list

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



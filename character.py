from constructor import Constructor
import math
import random
import copy
import catalog
import db_connector
import family
import family_role
import associator
import selector


class Character(Constructor):

    def __init__(self):
        self.id = None
        self.name = 'Default'
        self.family = family.Family()
        self.spouse_family = family.Family()
        self.culture = catalog.cultures['Default']
        self.race = catalog.races['Default']
        self.gender = 'Default'
        self.age = -1
        self.social_group = catalog.social_groups['Default']
        self.profession = catalog.professions['Default']
        self.wealth = -1
        self.attributes = []
        for x in catalog.attributes:
            self.attributes.append(0)
        self.moralities = []
        for x in catalog.moralities:
            self.moralities.append(0)
        self.family_role = family_role.Family_Role()
        self.groups = []

        self.master_char = None

    # -------------------------- Association methods -------------------------------- Begin

    def basic_associate(self, city_id, building_id, param={'live': True, 'work': True}):
        if param['live']:
            live_id = building_id
        else:
            live_id = None
        if param['work']:
            work_id = building_id
        else:
            work_id = None
        new_associator = associator.Associator(self)
        new_associator.associate(city_id=city_id, live_id=live_id, work_id=work_id)

    def associate_building(self, live_id, work_id, visit_id):
        new_associator = associator.Associator(self)
        new_associator.associate(live_id=live_id, work_id=work_id, visit_id=visit_id)

    # -------------------------- Association methods -------------------------------- End

    # ------------------ Preset base information from parameter dictionary  ---------------- Begin

    def set_base(self, param):
        # Take a param dict to set predefined information before searching for compatible characters
        self.set_base_family_role(param['family role'])
        self.set_base_culture(param['culture'])
        self.set_base_race(param['race'])
        self.set_base_gender(param['gender'])
        self.set_base_name(param['name'])
        self.set_base_family(param['fname'])
        self.set_spouse_family()
        self.set_base_age(param['age'])
        self.set_base_social_group(param['social group'])
        self.set_base_profession(param['profession'])
        self.set_base_wealth(param['wealth'])

    def set_base_family_role(self, role):
        if role != 'None':
            if role == 'Master':
                self.family_role.role = family_role.master.role
            if role == 'Spouse':
                self.family_role.role = family_role.spouse.role
            if role == 'Child':
                self.family_role.role = family_role.child.role
        if self.family_role.role == family_role.spouse.role or self.family_role.role == family_role.child.role:
            self.set_master()

    def set_master(self):
        new_associator = associator.Associator(self)
        new_associator.master()

    def set_base_culture(self, culture):
        if culture != 'Random':
            try:
                self.culture = catalog.cultures[culture]
            except:
                self.culture = catalog.cultures['Error']

    def set_base_race(self, race):
        if race != 'Random':
            try:
                self.race = catalog.races[race]
            except:
                self.race = catalog.races['Error']

    def set_base_gender(self, gender):
        if gender != 'Random':
            try:
                self.gender = gender
            except:
                self.gender = 'Error'

    def set_base_name(self, name):
        if name!= 'Random':
            self.name = name

    def set_base_family(self, fname):
        if self.family_role.role == family_role.child.role:
            new_associator = associator.Associator(self)
            new_associator.family(self.master_char.family.id)
        elif fname != 'Random':
            self.family.name = fname

    def set_spouse_family(self):
        if self.family_role.role == family_role.spouse.role:
            new_associator = associator.Associator(self)
            new_associator.spouse_family(self.master_char.family.id)

    def set_base_age(self, age):
        if age != 'Random':
            try:
                self.age = int(age)
            except:
                self.age = -2

    def set_base_social_group(self, s_group):
        if s_group != 'Random':
            try:
                self.social_group = catalog.social_groups[s_group]
            except:
                self.social_group = catalog.social_groups['Error']
        elif self.family_role.role == family_role.child.role:  # Unless otherwise specified by user, children of strict_inheritance social group are always the same as master_char
            if self.master_char.social_group.strict_inheritance:
                self.social_group = self.master_char.social_group

    def set_base_profession(self, profession):
        if profession != 'Random':
            try:
                self.profession = catalog.professions[profession]
            except:
                self.profession = catalog.professions['Error']

    def set_base_wealth(self, wealth):
        if wealth != 'Random':
            try:
                self.wealth = int(wealth)
            except:
                self.wealth = -2

    # ------------------ Preset base information from parameter dictionary  ---------------- End

    # ------------------ Search existing character for compatible ones --------------------- Begin

    def search_existing_char(self):
        # Search for an existing char with compatible information

        # First, fetch a list of existing character without associated live or work building
        connector = db_connector.Character_Connector()
        if self.building_live:
            candidates = connector.load_from_db('live_id', None)
            if self.building_work:
                removed_work = []
                for char in candidates:
                    if char.building_work:
                        removed_work.append(char)
                for char in removed_work:
                    candidates.remove(char)
        elif self.building_work:
            candidates = connector.load_from_db('work_id', None)
        else:
            raise Exception

        # Then, remove character with info incompatible with preset information
        default_char = Character()
        removed = []
        for char in candidates:
            if self.name != default_char.name:  # If new char attribute value is default, any character can do so skip verification
                if self.name != char.name:  # If new char attribute isn't the same as candidate ...
                    removed.append(char)  # ... remove candidate from list.
                    continue
            if self.family.id != default_char.family.id:
                if self.family.id != char.family.id:
                    removed.append(char)
                    continue
            if self.culture != default_char.culture:
                if self.culture != char.culture:
                    removed.append(char)
                    continue
            if self.race != default_char.race:
                if self.race != char.race:
                    removed.append(char)
                    continue
            if self.gender != default_char.gender:
                if self.gender != char.gender:
                    removed.append(char)
                    continue
            if self.age != default_char.age:
                if self.age < (char.age-catalog.Age_search_range) or self.age > (char.age+catalog.Age_search_range):  # Age search range can be modified in settings.csv
                    removed.append(char)
                    continue
            if self.wealth != default_char.wealth:
                if self.wealth < (char.wealth-catalog.Wealth_search_range) or self.wealth > (char.wealth+catalog.Wealth_search_range):
                    removed.append(char)
                    continue
            if self.social_group != default_char.social_group:
                if self.social_group != char.social_group:
                    removed.append(char)  # Replace with test for compatibilities
                    continue
            if self.profession != default_char.profession or char.profession != default_char.profession:  # Candidate profession can be unallocated, so check for that
                if self.profession != char.profession:
                    removed.append(char)
                    continue
        for char in removed:
            candidates.remove(char)

        if candidates:  # if compatible candidates remains ...
            selected = random.choice(candidates)
            f_role = self.family_role
            self.__dict__ = copy.copy(selected.__dict__)  # ... copy all info from selected existing character.
            self.family_role = f_role  # But make sure to keep new_family_role

    # ------------------ Search existing character for compatible ones --------------------- End

    # ------------------ Complete missing info after other steps --------------------------- Begin

    def complete_info(self):
        # Add missing information to the character
        default_char = Character()
        self.set_culture(default_char.culture)
        self.set_race(default_char.race)
        self.set_gender(default_char.gender)
        self.set_name(default_char.name)
        self.set_family(default_char.family.id)
        self.set_age(default_char.age)
        self.set_attributes(default_char.attributes)
        self.set_moralities(default_char.moralities)
        # Note to self: Be weary of spouse_family interaction!
        pass

    def set_culture(self, default):
        if self.culture == default:  # Assign culture if it is still default
            if self.family_role == family_role.spouse or self.family_role == family_role.child:  # If child or spouse, set culture to master's
                self.culture = self.master_char.culture
            else:  # Otherwise, check city dominant culture
                openness = 100 + self.in_city.culture.cultural_openness
                result = random.randint(1, openness)
                if result <= 100:
                    self.culture = self.in_city.culture
                else:
                    self.assign_minority_culture()

    def assign_minority_culture(self):
        culture_selector = selector.Selector(catalog.cultures)
        self.culture = culture_selector.minority_culture(self.in_city.culture)

    def set_race(self, default):
        if self.race == default:  # If race is default, set it culture race
            self.race = self.culture.race

    def set_gender(self, default):
        if self.gender == default:
            if self.family_role == family_role.spouse:  # Assign opposite gender if spouse
                if self.master_char.gender == 'Male':
                    self.gender = 'Female'
                elif self.master_char.gender == 'Female':
                    self.gender = 'Male'
            else:
                self.gender = random.choice(['Male', 'Female'])

    def set_name(self, default):
        if self.name == default:
            if self.gender == 'Male':
                self.name = random.choice(self.culture.male_names)
            elif self.gender == 'Female':
                self.name = random.choice(self.culture.female_names)

    def set_family(self, default):
        if self.family.id == default:  # If no family has been associated, create a new one in database, with preset or random name
            if self.family.name == default.family.name:
                self.family.name = random.choice(self.culture.family_names)
            connector = db_connector.Family_Connector()
            self.family.id = connector.write_to_db(self.family)

    def set_age(self, default):
        if self.age == default:
            if self.family_role.role == family_role.spouse.role:
                self.age = max(self.race.adult_age, self.master_char.age + round(random.gauss(0, 5)))
            elif self.family_role.role == family_role.child.role:
                self.age = max(0, self.master_char.age - max(self.race.adult_age, round(random.gauss(self.race.adult_age+5, 5))))
            else:
                self.age = max(self.race.adult_age + random.randint(0,4), random.triangular(self.race.adult_age/2, self.race.old_age*1.1, self.race.old_age/2.2))

    def set_attributes(self, default):
        if self.attributes == default:
            modifiers = self.build_race_modifiers()
            for index, value in enumerate(catalog.attributes):
                self.attributes[index] = random.gauss(value.mean, value.variance)
                if value.rounding:
                    self.attributes[index] = round(self.attributes[index])
                if self.attributes[index] < value.range[0]:
                    self.attributes[index] = value.range[0]
                elif self.attributes[index] > value.range[1]:
                    self.attributes[index] = value.range[1]
                for modifier in modifiers:
                    if modifier[0].rstrip() == value.name:
                        if modifier[1] == '+':
                            self.attributes[index] += int(modifier[2])
                        elif modifier[1] == '-':
                            self.attributes[index] -= int(modifier[2])

    def build_race_modifiers(self):
        race_modifiers = []
        for modifier_string in self.race.attr_mod:
            modifier_tuple = ('', '', '')
            if '+' in modifier_string:
                modifier_tuple = modifier_string.partition('+')
            elif '-' in modifier_string:
                modifier_tuple = modifier_string.partition('-')
            race_modifiers.append(modifier_tuple)
            try:
                int(modifier_tuple[2])
            except:
                print('Error in race attributes modifier')
        return race_modifiers

    def set_moralities(self, default):
        if self.moralities == default:
            modifiers = self.build_culture_modifiers()
            for index, value in enumerate(catalog.moralities):
                self.moralities[index] = random.gauss(value.mean, value.variance)
                if value.rounding:
                    self.moralities[index] = round(self.moralities[index])
                if self.moralities[index] < value.range[0]:
                    self.moralities[index] = value.range[0]
                elif self.moralities[index] > value.range[1]:
                    self.moralities[index] = value.range[1]
                for modifier in modifiers:
                    if modifier[0].rstrip() == value.name:
                        if modifier[1] == '+':
                            self.moralities[index] += int(modifier[2])
                        elif modifier[1] == '-':
                            self.moralities[index] -= int(modifier[2])

    def build_culture_modifiers(self):
        culture_modifiers = []
        for modifier_string in self.culture.morality_modifiers:
            modifier_tuple = ('', '', '')
            if '+' in modifier_string:
                modifier_tuple = modifier_string.partition('+')
            elif '-' in modifier_string:
                modifier_tuple = modifier_string.partition('-')
            culture_modifiers.append(modifier_tuple)
            try:
                int(modifier_tuple[2])
            except:
                print('Error in culture morality modifier')
        return culture_modifiers

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
                wealth_odds = [x for x in catalog_profession.professions if x.name == self.profession]
                wealth_odds = wealth_odds[0].wealth
                if (wealth_odds % 1) >= random.random():
                    wealth_odds = math.ceil(wealth_odds)
                else:
                    wealth_odds = math.floor(wealth_odds)
                self.wealth = catalog_character.wealth[int(wealth_odds)]
        except:
            self.wealth = 'Error'

    # ------------------ Complete missing info after other steps --------------------------- End

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

    def construct_profession(self, in_building, in_city, role):
        good_preset = None
        preset_list = [x.groups for x in catalog_building if x.name == in_building.subkind]
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
                required_feature = [x for x in catalog_profession.professions if x == possible_job[x]]
                required_feature = required_feature[0].geo_restric
                for y in range(odds[x]):
                    if self.test_geography(required_feature, in_city):
                        profession_list.append(possible_job[x].name)
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



from constructor import Constructor
import random
import json
import copy
import base
import catalog
import db_connector
import group
import family
import family_role
import associator
import selector
import verifier


class Character(Constructor):
    """ Class used to create and handle characters. Characters are part of one or multiple Groups. """

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

        # Temporary values not saved in database directly
        self.current_group_edit = group.Group()
        self.master_char = None
        self.auto_populate = False
        self.will_leave = False

    def build_character(self, param_dict, auto_populate=False):
        # auto_populate is set to True if method call is made as part of a building/group preset
        if auto_populate:
            self.auto_populate = True
        self.set_base(param_dict)
        if self.family_role.role != family_role.child.role:
            print('Search start')
            self.search_existing_char()
            print('Search end')
        self.complete_info()


    # -------------------------- Association methods -------------------------------- Begin

    def associate_group(self, group_id):
        # Add group_id to groups list if it's not already there and set current_group_edit to that Group object
        new_associator = associator.Associator(self)
        new_associator.group(group_id)

    def set_master(self):
        new_associator = associator.Associator(self)
        new_associator.master()

    # -------------------------- Association methods -------------------------------- End

    # ------------------ Preset base information from parameter dictionary  ---------------- Begin

    def set_base(self, param):
        # Take a param dict to set predefined information before searching for compatible characters
        print('set_base start')
        self.set_base_family_role(param['family role'])
        print(self.family_role.role)
        self.set_base_culture(param['culture'])
        print(self.culture.name)
        self.set_base_race(param['race'])
        print(self.race.name)
        self.set_base_gender(param['gender'])
        print(self.gender)
        self.set_base_name(param['name'])
        print(self.name)
        self.set_base_family(param['fname'])
        print(self.family.name)
        self.set_spouse_family()
        print(self.spouse_family.name)
        self.set_base_age(param['age'])
        print(self.age)
        self.set_base_social_group(param['social group'])
        print(self.social_group.name)
        self.set_base_profession(param['profession'])
        print(self.profession.name)
        self.set_base_wealth(param['wealth'])
        print(self.wealth)
        print('set_base end')

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
        if name != 'Random':
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
                self.wealth = float(wealth)
            except:
                self.wealth = -2

    # ------------------ Preset base information from parameter dictionary  ---------------- End

    # ------------------ Search existing character for compatible ones --------------------- Begin

    def search_existing_char(self):
        # Search for an existing char with compatible information

        # First, fetch a random list of potentiel characters
        connector = db_connector.Db_Connector(base.Character)
        bases = connector.load_all()
        random.shuffle(bases)
        candidates = []
        search_range = min(100, len(bases))
        for x in range(search_range):  # Limit loaded character to 100 to prevent having too many operations and randomizing the selection process
            char = Character()
            char.set_from_db(bases[x])
            candidates.append(char)

        # Then, remove character with info incompatible with preset information
        default_char = Character()
        removed = []
        for char in candidates:
            if self.current_group_edit.is_live:  # Remove character who already live somewhere
                found = False
                for g in char.groups:
                    if g.is_live:
                        removed.append(char)
                        found = True
                        continue
                if found:
                    continue
            if self.current_group_edit.is_work:  # Remove character who already work somewhere
                found = False
                for g in char.groups:
                    if g.is_work:
                        removed.append(char)
                        found = True
                        continue
                if found:
                    continue

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
            self.family_role = f_role  # But make sure to keep new_group_role

    # ------------------ Search existing character for compatible ones --------------------- End

    # ------------------ Complete missing info after other steps --------------------------- Begin

    def complete_info(self):
        # Add missing information to the character
        default_char = Character()
        self.set_family_role(default_char.family_role.role)
        print(self.family_role.role)
        self.set_culture(default_char.culture)
        print(self.culture.name)
        self.set_race(default_char.race)
        print(self.race.name)
        self.set_gender(default_char.gender)
        print(self.gender)
        self.set_name(default_char.name)
        print(self.name)
        self.set_family(default_char.family)
        print(self.family.name)
        self.set_age(default_char.age)
        print(self.age)
        self.set_will_leave()
        print(self.will_leave)
        self.set_attributes(default_char.attributes)
        print(self.attributes)
        self.set_moralities(default_char.moralities)
        print(self.moralities)
        self.set_wealth(default_char.wealth)
        print(self.wealth)
        self.set_social_group(default_char.social_group)
        print(self.social_group.name)
        self.set_profession(default_char.profession)
        print(self.profession.name)

    def set_family_role(self, default):
        if self.family_role.role == default:  # Assign family role if still default according to group attribute
            if self.current_group_edit.is_family:  # If group is a family, additional character are children of master (master and spouse must be preset in other way)
                self.family_role.role = family_role.child.role

    def set_culture(self, default):
        if self.culture == default:  # Assign culture if it is still default
            if self.family_role.role == family_role.spouse.role or self.family_role.role == family_role.child.role:  # If child or spouse, set culture to master's
                self.culture = self.master_char.culture
            else:  # Otherwise, check city dominant culture
                openness = 100 + self.current_group_edit.in_building.in_city.culture.cultural_openness
                result = random.randint(1, openness)
                if result <= 100:
                    self.culture = self.current_group_edit.in_building.in_city.culture
                else:
                    self.assign_minority_culture()

    def assign_minority_culture(self):
        culture_selector = selector.Selector(catalog.cultures)
        self.culture = culture_selector.minority_culture(self.current_group_edit.in_building.in_city.culture)

    def set_race(self, default):
        if self.race == default:  # If race is default, set it culture race
            self.race = self.culture.race

    def set_gender(self, default):
        if self.gender == default:
            if self.family_role.role == family_role.spouse.role:  # Assign opposite gender if spouse
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
        if self.family.id == default.id:  # If no family has been associated, create a new one in database, with preset or random name
            if self.family.name == default.name:
                self.family.name = random.choice(self.culture.family_names)
            connector = db_connector.Db_Connector(base.Family)
            self.family.id = connector.write_to_db(self.family)

    def set_age(self, default):
        if self.age == default:
            if self.family_role.role == family_role.spouse.role:
                self.age = max(self.race.adult_age, self.master_char.age + round(random.gauss(0, 5)))
            elif self.family_role.role == family_role.child.role:
                self.age = max(0, self.master_char.age - max(self.race.adult_age, round(random.gauss(self.race.adult_age+5, 5))))
            else:
                self.age = max(self.race.adult_age + random.randint(0,4), random.triangular(self.race.adult_age/2, self.race.old_age*1.1, self.race.old_age/2.2))
            self.age = int(self.age)

    def set_will_leave(self):
        if self.auto_populate and self.family_role.role == family_role.child.role:  # Manually added character cannot leave
            first_child = True
            if verifier.if_role_in_group(self.current_group_edit.characters, family_role.child.role):
                first_child = False
            if first_child and self.current_group_edit.preset.inheritance:  # First child of inherited group cannot leave
                return
            if self.age >= self.race.working_age and random.randint(1, 100) <= 80:  # !!! Can be changed to a config option
                self.will_leave = True

    def set_attributes(self, default):
        if self.attributes == default:
            modifiers = self.build_race_modifiers()
            for index, value in enumerate(catalog.attributes):
                self.attributes[index] = random.gauss(value.mean, value.variance)  # Assign random base value
                for modifier in modifiers:  # Check for racial modifiers
                    if modifier[0].strip() == value.name:
                        if modifier[1] == '+':
                            self.attributes[index] += float(modifier[2])
                        elif modifier[1] == '-':
                            self.attributes[index] -= float(modifier[2])
                if value.rounding:  # Round value if necessary
                    self.attributes[index] = round(self.attributes[index])
                if self.attributes[index] < value.range[0]:  # Make sure value is inside limits
                    self.attributes[index] = value.range[0]
                elif self.attributes[index] > value.range[1]:
                    self.attributes[index] = value.range[1]

    def set_moralities(self, default):
        if self.moralities == default:
            modifiers = self.build_culture_modifiers()
            for index, value in enumerate(catalog.moralities):
                self.moralities[index] = random.gauss(value.mean, value.variance)  # Assign random base value
                for modifier in modifiers:  # Check for cultural modifiers
                    if modifier[0].strip() == value.name:
                        if modifier[1] == '+':
                            self.moralities[index] += float(modifier[2])
                        elif modifier[1] == '-':
                            self.moralities[index] -= float(modifier[2])
                if value.rounding:  # Round value if necessary
                    self.moralities[index] = round(self.moralities[index])
                if self.moralities[index] < value.range[0]:  # Make sure value is inside limits
                    self.moralities[index] = value.range[0]
                elif self.moralities[index] > value.range[1]:
                    self.moralities[index] = value.range[1]

    def set_wealth(self, default):
        if self.wealth == default:
            if self.family_role.role == family_role.child.role or self.family_role.role == family_role.spouse.role:
                self.wealth = max(0, round(self.master_char.wealth + self.master_char.wealth*random.uniform(-0.3, 0.3), 2))
            else:
                self.wealth = random.betavariate(2, 5)

    def set_social_group(self, default):
        if self.social_group == default and not self.will_leave:
            if self.current_group_edit.preset.name != 'Default':
                self.social_group = self.current_group_edit.preset.social_group
            else:
                social_selector = selector.Selector(catalog.social_groups)
                self.social_group = social_selector.social_group(self)

    def set_profession(self, default):
        if self.profession == default and not self.will_leave:
            if self.age < self.race.working_age:
                self.profession = catalog.professions['Child']
            else:
                if self.current_group_edit.preset.name != 'Default':
                    if self.family_role.role == family_role.master.role:
                        prof_list = self.current_group_edit.preset.professions_main
                        odds = self.current_group_edit.preset.odds_main
                    else:
                        prof_list = self.current_group_edit.preset.professions
                        odds = self.current_group_edit.preset.professions_odds
                else:
                    prof_list = self.social_group.professions
                    odds = self.social_group.professions_odds

                prof_selector = selector.Selector(prof_list)
                self.profession = prof_selector.profession(odds, self.current_group_edit.in_building.in_city)

        if self.profession.unique:
            self.update_taken_job()

    def update_taken_job(self):
        in_city = self.current_group_edit.in_building.in_city
        in_city.taken_jobs.append(self.profession)
        city_connector = db_connector.Db_Connector(base.City)
        city_connector.update_entry(in_city.id, 'taken_jobs', json.dumps(in_city.taken_jobs))
        city_connector.close_session()

    # ------------------ Complete missing info after other steps --------------------------- End

    # --------------------- Misc. list construction methods -------------------------------- Begin

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
                float(modifier_tuple[2])
            except:
                print('Error in race "{0}" attributes modifier'.format(self.race.name))
        return race_modifiers

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
                float(modifier_tuple[2])
            except:
                print('Error in culture "{0}" morality modifier'.format(self.culture.name))
        return culture_modifiers

    # --------------------- Misc. list construction methods -------------------------------- End

    # ----------------------- Load from database methods ----------------------------------- Begin

    def set_from_db(self, base_character):
        self.id = base_character.id
        self.name = base_character.name
        self.culture = catalog.cultures[base_character.culture]
        self.race = catalog.races[base_character.race]
        self.gender = base_character.gender
        self.age = base_character.age
        self.social_group = catalog.social_groups[base_character.social_group]
        self.profession = catalog.professions[base_character.profession]
        self.wealth = base_character.wealth
        self.attributes = json.loads(base_character.attributes)
        self.moralities = json.loads(base_character.moralities)
        self.family_role.role = base_character.family_role
        self.load_groups(json.loads(base_character.groups))
        self.load_family(base_character.family_id)
        self.load_spouse_family(base_character.spouse_family_id)

    def load_groups(self, id_list):
        group_connector = db_connector.Db_Connector(base.Group)
        for item in id_list:
            g = group_connector.load_from_db('id', item)
            self.groups.append(g[0])
        group_connector.close_session()

    def load_family(self, family_id):
        if family_id:
            family_connector = db_connector.Db_Connector(base.Family)
            f = family_connector.load_from_db('id', family_id)
            self.family = f[0]
            family_connector.close_session()

    def load_spouse_family(self, spouse_family_id):
        if spouse_family_id:
            family_connector = db_connector.Db_Connector(base.Family)
            f = family_connector.load_from_db('id', spouse_family_id)
            self.spouse_family = f[0]
            family_connector.close_session()

    # ----------------------- Load from database methods ----------------------------------- End

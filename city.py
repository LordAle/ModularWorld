import random
import catalogs_city
import catalogs_character

class City():

    names_list = ['Id', 'Name', 'Kind', 'Population', 'Main race', 'Forests', 'Plains', 'Rivers', 'Sea',
                  'Mountains', 'Mines']

    def __init__(self):
        self.id = None
        self.name = 'Default name'
        self.kind = 'Default kind'
        self.population = 0
        self.main_race = 'Default race'
        self.forests = False
        self.plains = False
        self.river = False
        self.sea = False
        self.mountains = False
        self.mines = False
        self.update_values_list()

    def set_from_dialog(self, param):
        # Expect dictionary with keys: name, kind, population, main_race, geography

        self.name = param['name']
        if self.name == 'Random':
            self.name = random.choice(catalogs_city.names)

        self.kind = param['kind']
        if self.kind == 'Random':
            self.kind = random.choice(catalogs_city.kinds)

        self.population = param['population']
        if self.population == 'Random':
            for x in range(len(catalogs_city.kinds)):
                    if self.kind == catalogs_city.kinds[x]:
                        self.population = random.randint(catalogs_city.population_ranges[x][0],
                                                         catalogs_city.population_ranges[x][1])
                        break

        self.main_race = param['main_race']
        if self.main_race == 'Random':
            self.main_race = random.choice(catalogs_character.races)

        if param['geography'] == 'Random':
            self.forests = random.choice([True, False])
            self.plains = random.choice([True, False])
            self.river = random.choice([True, False])
            self.sea = random.choice([True, False])
            self.mountains = random.choice([True, False])
            self.mines = random.choice([True, False])
        else:
            try:
                if param['geography']['forests']:
                    self.forests = True
                if param['geography']['plains']:
                    self.plains = True
                if param['geography']['river']:
                    self.river = True
                if param['geography']['sea']:
                    self.sea = True
                if param['geography']['mountains']:
                    self.mountains = True
                if param['geography']['mines']:
                    self.mines = True
            except:
                pass

    def set_from_db(self, base_city):
        self.id = base_city.id
        self.name = base_city.name
        self.kind = base_city.kind
        self.population = base_city.population
        self.main_race = base_city.main_race
        self.forests = base_city.forests
        self.plains = base_city.plains
        self.river = base_city.river
        self.sea = base_city.sea
        self.mountains = base_city.mountains
        self.mines = base_city.mines
        self.update_values_list()

    def special_traveller(self):
        self.id = None
        self.name = 'Traveller'
        self.kind = 'Traveller'
        self.population = 0
        self.main_race = 'None'
        self.forests = False
        self.plains = False
        self.river = False
        self.sea = False
        self.mountains = False
        self.mines = False
        self.update_values_list()

    def update_values_list(self):
        self.values_list = [self.id, self.name, self.kind, self.population, self.main_race, self.forests, self.plains,
                            self.river, self.sea, self.mountains, self.mines]

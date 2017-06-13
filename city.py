import random
import catalog
import selector


class City:
    """ Class used to generate and handle cities. A 'city' is any large association of people clustered in 'buildings'. """

    def __init__(self):
        self.id = None
        self.name = 'Default name'
        self.culture = catalog.cultures['Default']
        self.size = catalog.city_sizes['Default']
        self.population = 0
        self.forest = False
        self.plain = False
        self.river = False
        self.sea = False
        self.mountain = False
        self.mine = False

    def set_from_dialog(self, param):
        # Expect dictionary with keys: name, culture, size, population, geography

        self.set_culture(param['culture'])
        self.set_name(param['name'])
        self.set_size(param['size'])
        self.set_population(param['population'])
        self.set_geography(param['geography'])

        print(self.name, self.culture.name, self.size.name, self.population)
        print(self.forest, self.plain, self.river, self.sea, self.mountain, self.mine)

    def set_culture(self, culture):
        try:
            if culture == 'Random' or culture == 'random':
                new_selector = selector.Selector(catalog.cultures)
                self.culture = new_selector.simple()
            else:
                self.culture = catalog.cultures[culture]
        except:
            self.culture = catalog.cultures['Error']

    def set_name(self, name):
        try:
            if name == 'Random' or name == 'random':
                self.name = random.choice(self.culture.city_names)
            else:
                self.name = name
        except:
            self.name = 'Error'

    def set_size(self, size):
        try:
            if size == 'Random' or size == 'random':
                new_selector = selector.Selector(catalog.city_sizes)
                self.culture = new_selector.simple()
            else:
                self.size = catalog.city_sizes[size]
        except:
            self.size = catalog.city_sizes['Error']

    def set_population(self, pop):
        try:
            if pop == 'Random' or pop == 'random':
                self.population = random.randint(self.size.pop_range[0], self.size.pop_range[1])
            else:
                self.population = int(pop)
        except:
            self.population = 0

    def set_geography(self, geo):
        try:
            if geo == 'Random' or geo == 'random':
                self.forest = random.choice([True, False])
                self.plain = random.choice([True, False])
                self.river = random.choice([True, False])
                self.sea = random.choice([True, False])
                self.mountain = random.choice([True, False])
                self.mine = random.choice([True, False])
            else:
                if geo['forest']:
                    self.forest = True
                if geo['plain']:
                    self.plain = True
                if geo['river']:
                    self.river = True
                if geo['sea']:
                    self.sea = True
                if geo['mountain']:
                    self.mountain = True
                if geo['mine']:
                    self.mine = True
        except:
            pass

    def set_from_db(self, base_city):
        self.id = base_city.id
        self.name = base_city.name
        self.culture = catalog.cultures[base_city.culture]
        self.size = catalog.city_sizes[base_city.size]
        self.population = base_city.population
        self.forest = base_city.forest
        self.plain = base_city.plain
        self.river = base_city.river
        self.sea = base_city.sea
        self.mountain = base_city.mountain
        self.mine = base_city.mine


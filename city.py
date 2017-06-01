import random
#from catalogs import catalog_city
#from catalogs import catalog_character
import catalog


class City():
    """ Class used to gererate and handle cities. A 'city' is any large association of people clustered in 'buildings'. """

    def __init__(self):
        self.id = None
        self.name = 'Default name'
        self.culture = catalog.cultures['Error']
        self.kind = catalog.city_kinds['Error']
        self.size = catalog.city_sizes['Error']
        self.population = 0
        self.forest = False
        self.plain = False
        self.river = False
        self.sea = False
        self.mountain = False
        self.mine = False

    def set_from_dialog(self, param):
        # Expect dictionary with keys: name, culture, kind, size, population, geography

        self.set_culture(param['culture'])
        self.set_name(param['name'])
        self.set_kind(param['kind'])
        self.set_size(param['size'])
        self.set_population(param['population'])
        self.set_geography(param['geography'])

        print(self.name, self.culture.name, self.kind.name, self.size.name, self.population)
        print(self.forest, self.plain, self.river, self.sea, self.mountain, self.mine)

    def set_culture(self, culture):
        try:
            if culture == 'Random' or culture == 'random':
                culture_list = list(catalog.cultures.values())
                culture_list.remove(catalog.cultures['Error'])
                self.culture = random.choice(culture_list)
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

    def set_kind(self, kind):
        try:
            if kind == 'Random' or kind == 'random':
                kind_list = list(catalog.city_kinds.values())
                kind_list.remove(catalog.city_kinds['Error'])
                self.kind = random.choice(kind_list)
            else:
                self.kind = catalog.city_kinds[kind]
        except:
            self.kind = catalog.city_kinds['Error']

    def set_size(self, size):
        try:
            if size == 'Random' or size == 'random':
                size_list = list(catalog.city_sizes.values())
                size_list.remove(catalog.city_sizes['Error'])
                self.size = random.choice(size_list)
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
        self.kind = catalog.city_kinds[base_city.kind]
        self.size = catalog.city_sizes[base_city.size]
        self.population = base_city.population
        self.forest = base_city.forest
        self.plain = base_city.plain
        self.river = base_city.river
        self.sea = base_city.sea
        self.mountain = base_city.mountain
        self.mine = base_city.mine

    def special_traveller(self):
        self.id = None
        self.name = 'Travellers'
        self.culture = catalog.cultures['Human']
        self.kind = catalog.city_kinds['Traveller']
        self.size = catalog.city_sizes['Error']
        self.population = 0
        self.forest = False
        self.plain = False
        self.river = False
        self.sea = False
        self.mountain = False
        self.mine = False


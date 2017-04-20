import random
import catalogs_building
import catalogs_city

class Building():

    names_list = ['Id', 'Name', 'Kind', 'Subkind', 'City']

    def __init__(self):
        self.id = None
        self.name = 'Default name'
        self.kind = 'Default kind'
        self.subkind = 'Default subkind'
        self.city_id = None
        self.values_list = [self.id, self.name, self.kind, self.subkind, self.city_id]

    def set_from_dialog(self, param, in_city):
        # Expect dictionary with keys: name, kind

        self.name = param['name']
        if self.name == 'Random':
            self.name = 'Random (placeholder)'

        self.kind = param['kind']
        if self.kind == 'Random':
            self.kind = random.choice(catalogs_building.kinds)

        self.subkind = param['subkind']
        if self.subkind == 'Random' or False:
            subkind_list = []
            for subkind_info in catalogs_building.subkinds[self.kind]:
                if subkind_info[1] <= catalogs_city.kinds.index(in_city.kind):
                    for x in range(subkind_info[2]):
                        subkind_list.append(subkind_info[0])
            try:
                self.subkind = random.choice(subkind_list)
            except:
                raise Exception

        self.update_values_list()

    def special_floating(self, city_id):
        self.name = 'Floating'
        self.kind = 'Floating'
        self.subkind = 'Floating'
        self.set_city_id(city_id)

    def set_city_id(self, city_id):
        self.city_id = city_id

    def set_from_db(self, base_building):
        self.id = base_building.id
        self.name = base_building.name
        self.kind = base_building.kind
        self.subkind = base_building.subkind
        self.city_id = base_building.city_id
        self.update_values_list()


    def update_values_list(self):
        self.values_list = [self.id, self.name, self.kind, self.subkind, self.city_id]

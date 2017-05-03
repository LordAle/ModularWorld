import random
import catalogs_building
import catalogs_city

class Building():

    names_list = ['Id', 'Name', 'Kind', 'Subkind', 'City']

    def __init__(self, in_city = None):
        self.id = None
        self.name = 'Default name'
        self.kind = 'Default kind'
        self.subkind = 'Default subkind'
        self.in_city = in_city
        self.city_id = None
        self.values_list = [self.id, self.name, self.kind, self.subkind, self.city_id]

    def set_from_dialog(self, param):
        # Expect dictionary with keys: name, kind
        self.set_name(param['name'])

        self.set_kind(param['kind'])

        self.set_subkind(param['subkind'])

        self.update_values_list()

    def set_name(self, name):
        self.name = name
        if self.name == 'Random':
            self.name = 'Random (placeholder)'

    def set_kind(self, kind):
        self.kind = kind
        if self.kind == 'Random':
            info_list = [(x.name, x.odds) for x in catalogs_building.kinds]
            choice_list = self.build_weighted_list(info_list)
            self.kind = random.choice(choice_list)

    def set_subkind(self, subkind):
        self.subkind = subkind
        if self.subkind == 'Random':
            info_list = [(x.name, x.odds) for x in catalogs_building.subkinds if (x.kind.name == self.kind and
                                                    x.min_city_size <= catalogs_city.kinds.index(self.in_city.kind))]
            choice_list = self.build_weighted_list(info_list)
            if choice_list:
                self.subkind = random.choice(choice_list)
            else:
                self.subkind = 'No valid subkind'

    def set_city_id(self, city_id):
        self.city_id = city_id

    def special_floating(self, city_id):
        self.name = 'Floating'
        self.kind = 'Floating'
        self.subkind = 'Floating'
        self.set_city_id(city_id)

    def set_from_db(self, base_building):
        self.id = base_building.id
        self.name = base_building.name
        self.kind = base_building.kind
        self.subkind = base_building.subkind
        self.city_id = base_building.city_id
        self.update_values_list()

    def update_values_list(self):
        self.values_list = [self.id, self.name, self.kind, self.subkind, self.city_id]

    def build_weighted_list(self, info_list):
        # require a list of tuples in the form [{item, weight}, (item, weight)...]
        new_list = []
        for item in info_list:
            for time in range(item[1]):
                new_list.append(item[0])
        return new_list

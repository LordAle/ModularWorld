from constructor import Constructor
import catalog
import selector
import associator
import city


class Building(Constructor):
    """ Class used to generate and handle buildings. A 'building' is a location used to group people together by their occupations """

    def __init__(self):
        self.id = None
        self.name = 'Default'
        self.kind = catalog.building_kinds['Default']
        self.in_city = city.City()

    def set_from_dialog(self, param, city_id):
        # Expect dictionary with keys: name, kind
        self.associate(city_id)
        self.set_name(param['name'])
        self.set_kind(param['kind'])

    def set_name(self, name):
        self.name = name
        if self.name == 'Random' or self.name == 'random':
            self.name = 'Random'

    def set_kind(self, kind):
        try:
            if kind == 'Random':
                new_selector = selector.Selector(catalog.building_kinds)
                self.kind = new_selector.building_kind(self.in_city.population)
            else:
                self.kind = catalog.building_kinds[kind]
        except:
            self.kind = catalog.building_kinds['Error']

    def set_from_db(self, base_building):
        self.associate(base_building.city_id)
        self.id = base_building.id
        self.name = base_building.name
        self.kind = catalog.building_kinds[base_building.kind]
        self.associate(base_building.city_id)

    def associate(self, city_id):
        asso = associator.Associator(self)
        asso.city(city_id)

    def set_from_edit_box(self, param):
        self.name = param['name']
        self.kind = catalog.building_kinds[param['kind']]
        if self.in_city.id != param['in_city_id']:
            self.associate(param['in_city_id'])

from constructor import Constructor
import json
import base
import db_connector
import associator
import building
import catalog


class Group(Constructor):
    """ Class used to generate and handle groups. A 'group' is used to group people together by their occupations inside buildings"""

    def __init__(self):
        self.id = None
        self.preset = catalog.professions_groups['Default']
        self.name = 'Default'
        self.is_family = False
        self.is_live = False
        self.is_work = False
        self.is_visit = False
        self.in_building = building.Building()
        self.characters = []

    def set_from_dialog(self, param, building_id):
        self.associate(building_id)
        self.name = param['name']
        if param['family']:
            self.is_family = True
        if param['live']:
            self.is_live = True
        if param['work']:
            self.is_work = True
        if param['visit']:
            self.is_visit = True

    def set_from_catalog(self, preset_name, building_id):
        self.associate(building_id)
        self.preset = catalog.professions_groups[preset_name]
        self.name = preset_name
        self.is_family = self.preset.children
        self.is_live = self.preset.live
        self.is_work = self.preset.work

    def associate(self, building_id):
        asso = associator.Associator(self)
        asso.building(building_id)

    def add_character(self, added_character_id):
        if added_character_id not in [self.characters]:
            self.characters.append(added_character_id)

    def assign_characters(self, chars_id):
        for x in chars_id:
            if x not in [y for y in self.characters]:
                self.characters.append(x)

    def set_from_db(self, base_group):
        self.associate(base_group.building_id)
        self.id = base_group.id
        self.preset = catalog.professions_groups[base_group.preset]
        self.name = base_group.name
        self.is_family = base_group.family
        self.is_live = base_group.live
        self.is_work = base_group.work
        self.is_visit = base_group.visit
        if base_group.characters:
            self.assign_characters(json.loads(base_group.characters))
        else:
            self.assign_characters([])

    def set_from_edit_box(self, param):
        self.name = param['name']
        if param['family']:
            self.is_family = True
        else:
            self.is_family = False
        if param['live']:
            self.is_live = True
        else:
            self.is_live = False
        if param['work']:
            self.is_work = True
        else:
            self.is_work = False
        if param['visit']:
            self.is_visit = True
        else:
            self.is_visit = False
        if self.in_building.id != param['in_building_id']:
            self.associate(param['in_building_id'])


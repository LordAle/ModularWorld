import db_connector
import base
import family_role

class Associator:

    def __init__(self, item):
        self.item = item

    def city(self, city_id):
        if hasattr(self.item, 'in_city'):
            connector = db_connector.Db_Connector(base.City)
            in_city = connector.load_from_db('id', city_id)
            self.item.in_city = in_city[0]

    def building(self, building_id):
        if hasattr(self.item, 'in_building'):
            connector = db_connector.Db_Connector(base.Building)
            in_building = connector.load_from_db('id', building_id)
            self.item.in_building = in_building[0]

    def group(self, group_id):
        if hasattr(self.item, 'groups'):
            connector = db_connector.Db_Connector(base.Group)
            in_group = connector.load_from_db('id', group_id)
            self.item.current_group_edit = in_group[0]
            if group_id not in [x.id for x in self.item.groups]:
                self.item.groups.append(in_group[0])

    def remove_group(self, group_id):
        if hasattr(self.item, 'groups') and group_id in [x.id for x in self.item.groups]:
            removed_group = [x for x in self.item.groups if x.id == group_id]
            for removed in removed_group:
                self.item.groups.remove(removed)

    def family(self, family_id):
        if hasattr(self.item, 'family'):
            connector = db_connector.Db_Connector(base.Family)
            in_family = connector.load_from_db('id', family_id)
            self.item.family = in_family[0]

    def spouse_family(self, family_id):
        if hasattr(self.item, 'spouse_family'):
            connector = db_connector.Db_Connector(base.Family)
            in_family = connector.load_from_db('id', family_id)
            self.item.spouse_family = in_family[0]

    def master(self):
        if not self.item.current_group_edit.id:
            print('No current group associated with character!')
            return

        for char in self.item.current_group_edit.characters:
            if char.family_role.role == family_role.master.role:
                master_char = char
                break
        try:
            self.item.master_char = master_char
        except:
            print('No master in selected group {0}'.format(self.item.current_group_edit.id))


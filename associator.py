import db_connector
import family_role

class Associator:

    def __init__(self, item):
        self.item = item

    def associate(self, city_id=None, live_id=None, work_id=None, visit_id=None):
        if hasattr(self.item, 'in_city') and city_id:
            connector = db_connector.City_Connector()
            in_city = connector.load_from_db('id', city_id)
            self.item.in_city = in_city[0]

        if hasattr(self.item, 'building_live') and live_id:
            connector = db_connector.Building_Connector()
            in_building = connector.load_from_db('id', live_id)
            self.item.building_live = in_building[0]

        if hasattr(self.item, 'building_work') and work_id:
            connector = db_connector.Building_Connector()
            in_building = connector.load_from_db('id', work_id)
            self.item.building_work = in_building[0]

        if hasattr(self.item, 'building_visit') and visit_id:
            connector = db_connector.Building_Connector()
            in_building = connector.load_from_db('id', visit_id)
            self.item.building_visit = in_building[0]

    def city(self, city_id=None):
        if hasattr(self.item, 'in_city') and city_id:
            connector = db_connector.City_Connector()
            in_city = connector.load_from_db('id', city_id)
            self.item.in_city = in_city[0]

    def building(self, building_id=None):
        if hasattr(self.item, 'in_building') and building_id:
            connector = db_connector.Building_Connector()
            in_building = connector.load_from_db('id', building_id)
            self.item.in_building = in_building[0]

    def group(self, group_id=None):
        if hasattr(self.item, 'groups') and group_id:
            connector = db_connector.


    def family(self, family_id):
        connector = db_connector.Family_Connector()
        in_family = connector.load_from_db('id', family_id)
        self.item.family = in_family[0]

    def spouse_family(self, family_id):
        connector = db_connector.Family_Connector()
        in_family = connector.load_from_db('id', family_id)
        self.item.spouse_family = in_family[0]

    def master(self):
        connector = db_connector.Character_Connector()
        live_chars = connector.load_from_db('live_id', self.item.building_live.id)
        master = [char for char in live_chars if char.family_role.role == family_role.master.role]
        try:
            self.item.master_char = master[0]
        except:
            print('No master in selected building {0}'.format(self.item.building_live.id))


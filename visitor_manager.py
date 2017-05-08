import db_connector
import random


class Visitor_manager:

    def __init__(self, building_id, city_id, wealth, groups, loader):
        self.loader = loader
        self.building_id = building_id
        self.city_id = city_id
        self.traveller_city_id = self.get_traveller_id()
        self.wealth = wealth
        try:
            self.groups = int(groups)
        except:
            self.groups = 0

    def add_visitor(self):
        self.purge_old_visitor()
        self.add_groups()


    def purge_old_visitor(self):
        connector = db_connector.Character_Connector(self.loader)
        old_visitor = connector.load_from_db('visiting_id', self.building_id)
        for visitor in old_visitor:
            connector.update_entry(visitor.id, 'visiting_id', 0)
        connector.close_session()

    def add_groups(self):
        connector = db_connector.Character_Connector(self.loader)
        characters = connector.load_from_db('city_id', self.city_id)
        characters = [x for x in characters if x.wealth == self.wealth]
        outside_characters = connector.load_from_db('city_id', self.traveller_city_id)
        outside_characters = [x for x in outside_characters if x.wealth == self.wealth]

        for group in range(self.groups):
            visitors = []
            if random.randrange(4) != 3:
                group_core = random.choice(characters)
                visitors.append(group_core)
                friends = [x for x in characters if x.building_id == group_core.building_id]
                for x in range(random.randrange(6)):
                    friend = random.choice(friends)
                    friends.remove(friend)
                    characters.remove(friend)
                    visitors.append(friend)
                for visitor in visitors:
                    connector.update_entry(visitor.id, 'visiting_id', self.building_id)
            else:
                group_core = random.choice(outside_characters)
                visitors.append(group_core)
                friends = [x for x in characters if x.building_id == group_core.building_id]
                for visitor in friends:
                    connector.update_entry(visitor.id, 'visiting_id', self.building_id)

    def get_traveller_id(self):
        connector = db_connector.City_Connector(self.loader)
        traveller_city = connector.load_from_db('kind', 'Traveller')
        connector.close_session()
        traveller_city_id = traveller_city[0].id

        return traveller_city_id


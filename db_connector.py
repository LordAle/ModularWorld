import json
import base
import city
import building
import group
import character
import family
from db_loader import loader


class Db_Connector():

    def __init__(self, base_object):
        self.session = loader.Session()
        self.base = base_object
        self.constructor = None
        self.set_constructor()

    def set_constructor(self):
        if self.base == base.City:
            self.constructor = city.City
        elif self.base == base.Building:
            self.constructor = building.Building
        elif self.base == base.Group:
            self.constructor = group.Group
        elif self.base == base.Character:
            self.constructor = character.Character
        elif self.base == base.Family:
            self.constructor = family.Family

    def open_session(self):
        self.session = loader.Session()

    def close_session(self):
        self.session.close()

    def write_to_db(self, item):
        if self.base == base.City:
            new_base_item = self.base(name=item.name, culture=item.culture.name, size=item.size.name, population=item.population,
                                      forest=item.forest, plain=item.plain, river=item.river, sea=item.sea, mountain=item.mountain, mine=item.mine)
        elif self.base == base.Building:
            new_base_item = self.base(name=item.name, kind=item.kind.name, city_id=item.in_city.id)
        elif self.base == base.Group:
            new_base_item = self.base(name=item.name, family=item.is_family, live=item.is_live, work=item.is_work, visit=item.is_visit, building_id=item.in_building.id)
        elif self.base == base.Character:
            new_base_item = self.base(name=item.name, culture=item.culture.name, race=item.race.name, gender=item.gender, age=item.age,
                                      social_group=item.social_group.name, profession=item.profession.name, wealth=item.wealth,
                                      attributes=json.dumps(item.attributes), moralities=json.dumps(item.moralities), family_role=item.family_role.name,
                                      groups=json.dumps([x.id for x in item.groups]), family_id=item.family.id, spouse_family_id=item.spouse_family.id)
        elif self.base == base.Family:
            new_base_item = self.base(name=item.name)

        try:
            self.session.add(new_base_item)
            self.session.commit()
            return new_base_item.id
        except NameError:
            print('Base item type in Db_Connector is not defined')

    def load_from_db(self, filter_by, filter_value):
        item_list = []
        loaded_items = self.session.query(self.base).filter(getattr(self.base, filter_by) == filter_value).all()
        for item in loaded_items:
            new_item = self.constructor()
            new_item.set_from_db(item)
            item_list.append(new_item)
        return item_list

    def update_entry(self, row_id, column_name, new_value):
        self.session.query(self.base).filter(self.base.id == row_id).update({column_name: new_value})
        self.session.commit()

    def delete_entry(self, row_id):
        self.session.query(self.base).filter(self.base.id == row_id).delete()
        self.session.commit()


class City_Connector(Db_Connector):

    def write_to_db(self, info_city):
        # Expect a City instance, return new city id
        new_city = base.City(name=info_city.name, culture=info_city.culture.name, size=info_city.size.name, population=info_city.population,
                             forest=info_city.forest, plain=info_city.plain, river=info_city.river, sea=info_city.sea,
                             mountain=info_city.mountain, mine=info_city.mine)
        self.session.add(new_city)
        self.session.commit()
        return new_city.id

    def load_from_db(self, filter_by, filter_value):
        # return a list of City objects
        cities_list = []
        loaded_cities = self.session.query(base.City).filter(getattr(base.City, filter_by) == filter_value).all()
        for select in loaded_cities:
            new_city = city.City()
            new_city.set_from_db(select)
            cities_list.append(new_city)
        return cities_list

    def update_entry(self, row_id, column_name, new_value):
        self.session.query(base.City).filter(base.City.id == row_id).update({column_name: new_value})
        self.session.commit()

    def delete_entry(self, row_id):
        self.session.query(base.City).filter(base.City.id == row_id).delete()
        self.session.commit()


class Building_Connector(Db_Connector):

    def write_to_db(self, info_building):
        # Expect Building instance, return new building id

        self.assign_id(info_building)
        new_building = base.Building(name=info_building.name, kind=info_building.kind, city_id=self.city_id)
        self.session.add(new_building)
        self.session.commit()
        return new_building.id

    def load_from_db(self, filter_by, filter_value):
        # return a list of Building objects
        building_list = []
        loaded_buildings = self.session.query(base.Building).filter(getattr(base.Building, filter_by) ==
                                                                    filter_value).all()
        for select in loaded_buildings:
            new_building = building.Building()
            new_building.set_from_db(select)
            building_list.append(new_building)
        return building_list

    def update_entry(self, row_id, column_name, new_value):
        self.session.query(base.Building).filter(base.Building.id == row_id).update({column_name: new_value})
        self.session.commit()

    def delete_entry(self, row_id):
        self.session.query(base.Building).filter(base.Building.id == row_id).delete()
        self.session.commit()

    def assign_id(self, info_building):
        try:
            self.city_id = info_building.in_city.id
        except:
            self.city_id = None


class Character_Connector(Db_Connector):

    def write_to_db(self, info_character):
        # Expect Character instance, return new character id

        self.assign_id(info_character)
        if info_character.id:
            self.full_update
        else:
            new_character = base.Character(name=info_character.name, culture=info_character.culture.name, race=info_character.race.name,
                                           gender=info_character.gender, age=info_character.age, social_group=info_character.social_group.name,
                                           profession=info_character.profession.name, wealth=info_character.wealth,
                                           attributes=info_character.attributes, moralities=info_character.moralities,
                                           family_role=info_character.family_role,
                                           family_id=info_character.family.id, spouse_family_id=info_character.spouse_family.id,
                                           city_id=self.city_id, live_id=self.live_id, work_id=self.work_id, visiting_id=self.visit_id)
            self.session.add(new_character)
            self.session.commit()
            return new_character.id

    def load_from_db(self, filter_by, filter_value):
        # return a list of Character objects
        character_list = []
        loaded_characters = self.session.query(base.Character).filter(getattr(base.Character, filter_by) == filter_value).all()
        for select in loaded_characters:
            new_character = character.Character()
            new_character.set_from_db(select)
            character_list.append(new_character)
        return character_list

    def update_entry(self, row_id, column_name, new_value):
        self.session.query(base.Character).filter(base.Character.id == row_id).update({column_name: new_value})
        self.session.commit()

    def delete_entry(self, row_id):
        self.session.query(base.Character).filter(base.Character.id == row_id).delete()
        self.session.commit()

    def assign_id(self, info_character):
        try:
            self.city_id = info_character.in_city.id
        except:
            self.city_id = None
        try:
            self.live_id = info_character.building_live.id
        except:
            self.live_id = None
        try:
            self.work_id = info_character.building_work.id
        except:
            self.work_id = None
        try:
            self.visit_id = info_character.building_visit.id
        except:
            self.visit_id = None


class Family_Connector(Db_Connector):

    def write_to_db(self, info_family):
        # Expect Family instance, return new family id
        new_family = base.Family(name=info_family.name)

        self.session.add(new_family)
        self.session.commit()
        return new_family.id

    def load_from_db(self, filter_by, filter_value):
        # return a list of Family objects
        family_list = []
        loaded_families = self.session.query(base.Building).filter(getattr(base.Family, filter_by) == filter_value).all()
        for select in loaded_families:
            new_family = family.Family()
            new_family.set_from_db(select)
            family_list.append(new_family)
        return family_list



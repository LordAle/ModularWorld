import base
import city
import building
import character
import family


class Db_Connector():

    def __init__(self, loader):
        self.session = loader.Session()

    def open_session(self, loader):
        self.session = loader.Session()

    def close_session(self):
        self.session.close()


class City_Connector(Db_Connector):

    def write_to_db(self, info_city):
        # Expect a City instance, return new city id
        new_city = base.City(name=info_city.name, kind=info_city.kind, population=info_city.population, main_race=info_city.main_race,
                             forests=info_city.forests, plains=info_city.plains, river=info_city.river, sea=info_city.sea,
                             mountains=info_city.mountains, mines=info_city.mines)
        self.session.add(new_city)
        self.session.commit()
        return new_city.id

    def load_from_db(self, filter_by, filter_value):
        # return complete City objects
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
        new_building = base.Building(name=info_building.name, kind=info_building.kind, subkind=info_building.subkind,
                                    city_id=info_building.city_id)
        self.session.add(new_building)
        self.session.commit()
        return new_building.id

    def load_from_db(self, filter_by, filter_value):
        # return complete Building objects
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

class Character_Connector(Db_Connector):

    def write_to_db(self, info_character):
        # Expect Character instance, return new character id
        new_character = base.Character(name=info_character.name, fname=info_character.fname, race=info_character.race,
                                       gender=info_character.gender, age=info_character.age, role=info_character.role,
                                       profession=info_character.profession, wealth=info_character.wealth,
                                       classe=info_character.classe, level=info_character.level,
                                       family_id=info_character.family_id, building_id=info_character.building_id,
                                       city_id=info_character.city_id, visiting_id=info_character.visiting_id)
        self.session.add(new_character)
        self.session.commit()
        return new_character.id

    def load_from_db(self, filter_by, filter_value):
        # return complete Character objects
        character_list = []
        loaded_characters = self.session.query(base.Character).filter(getattr(base.Character, filter_by) ==
                                                                     filter_value).all()
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


class Family_Connector(Db_Connector):

    def write_to_db(self, info_family):
        # Expect Family instance, return new family id
        new_family = base.Family(name=info_family.name)

        self.session.add(new_family)
        self.session.commit()
        return new_family.id



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
        self.assign_constructor()

    def assign_constructor(self):
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
        if item.id:  # if the item has an associated id, it must be updated and not duplicated
            self.full_update(item, item.id)
            return item.id

        else:
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

    def full_update(self, item, p_key):
        if self.base == base.City:
            self.session.query(self.base).filter(self.base.id == p_key).update({'name': item.name, 'culture': item.culture.name, 'size': item.size.name, 'population': item.population,
                                                                                'forest': item.forest, 'plain': item.plain, 'river': item.river,
                                                                                'sea': item.sea, 'mountain': item.mountain, 'mine': item.mine})
        elif self.base == base.Building:
            self.session.query(self.base).filter(self.base.id == p_key).update({'name': item.name, 'kind':item.kind.name, 'city_id': item.in_city.id})
        elif self.base == base.Group:
            self.session.query(self.base).filter(self.base.id == p_key).update({'name': item.name, 'family': item.is_family, 'live': item.is_live, 'work': item.is_work,
                                                                                'visit': item.is_visit, 'building_id': item.in_building.id})
        elif self.base == base.Character:
            self.session.query(self.base).filter(self.base.id == p_key).update({'name': item.name, 'culture': item.culture.name, 'race': item.race.name, 'gender': item.gender, 'age': item.age,
                                                                                'social_group': item.social_group.name, 'profession': item.profession.name, 'wealth': item.wealth,
                                                                                'attributes': json.dumps(item.attributes), 'moralities': json.dumps(item.moralities), 'family_role': item.family_role.name,
                                                                                'groups': json.dumps([x.id for x in item.groups]), 'family_id': item.family.id, 'spouse_family_id': item.spouse_family.id})
        elif self.base == base.Family:
            self.session.query(self.base).filter(self.base.id == p_key).update({'name': item.name})

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


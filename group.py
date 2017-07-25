from constructor import Constructor
import building


class Group(Constructor):
    """ Class used to generate and handle groups. A 'group' is location used to group people together by their occupations """

    def __init__(self):
        self.id = None
        self.name = 'Default'
        self.is_family = False
        self.is_live = False
        self.is_work = False
        self.is_visit = False
        self.in_building = building.Building()

    def set_from_db(self, base_group):
        self.id = base_group.id
        self.name = base_group.name
        self.is_family = base_group.family
        self.is_live = base_group.live
        self.is_work = base_group.work
        self.is_visit = base_group.visit

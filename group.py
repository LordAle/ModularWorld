from constructor import Constructor
import building


class Group(Constructor):

    def __init__(self):
        self.id = None
        self.name = 'Default'
        self.is_family = False
        self.is_live = False
        self.is_work = False
        self.is_visit = False
        self.in_building = building.Building()

    def set_from_db(self, base_item):
        pass

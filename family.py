from constructor import Constructor


class Family(Constructor):

    def __init__(self):
        self.id = None
        self.name = 'Default'

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_from_db(self, base_family):
        self.id = base_family.id
        self.name = base_family.name

from constructor import Constructor
import db_connector
import base


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

    def update_name_to_db(self, new_name):
        self.set_name(new_name)
        connector = db_connector.Db_Connector(base.Family)
        connector.full_update(self, self.id)
        connector.close_session()

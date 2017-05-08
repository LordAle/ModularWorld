from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os.path
import base


class Db_Loader():
    def __init__(self):
        return

    def create_new(self, path):
        if os.path.isfile(path):
            is_new_db = False
        else:
            is_new_db = True

        self.bind_engine(path)

        if is_new_db == True:
            base.Base.metadata.create_all(self.engine)

    def close(self):
        try:
            self.session.close()
        except:
            pass

    def bind_engine(self, path):
        self.engine = create_engine('sqlite:///{0}'.format(path), echo=False)
        base.Base.metadata.bind = self.engine

        self.Session = sessionmaker(bind=self.engine)


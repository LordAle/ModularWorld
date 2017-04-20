from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    kind = Column(String)
    population = Column(Integer)
    main_race = Column(String)

    forests = Column(Boolean)
    plains = Column(Boolean)
    river = Column(Boolean)
    sea = Column(Boolean)
    mountains = Column(Boolean)
    mines = Column(Boolean)


    buildings = relationship('Building', back_populates='city')
    characters = relationship('Character', back_populates='city')

    note = Column(String(10000))

class Building(Base):
    __tablename__ = 'buildings'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    kind = Column(String)
    subkind = Column(String)

    city_id = Column(Integer, ForeignKey('cities.id'))
    city = relationship(City, back_populates='buildings')

    characters = relationship('Character', back_populates='building')
    # workers = relationship('Character', back_populate='building')

    note = Column(String(10000))

class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fname = Column(String)
    race = Column(String)
    gender = Column(String)
    age = Column(Integer)
    role = Column(String)
    profession = Column(String)
    wealth = Column(String)
    classe = Column(String)
    level = Column(Integer)

    parent_id = Column(Integer)

    city_id = Column(Integer, ForeignKey('cities.id'))
    city = relationship(City, back_populates='characters')

    building_id = Column(Integer, ForeignKey('buildings.id'))
    building = relationship(Building, back_populates='characters')

    visiting_id = Column(Integer)

    note = Column(String(10000))

    # work_building_id = Column(Integer, ForeignKey('buildings.id'))
    # work_building = relationship(Building, back_populate='characters')

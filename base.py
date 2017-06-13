from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    culture = Column(String)
    size = Column(String)
    population = Column(Integer)

    forest = Column(Boolean)
    plain = Column(Boolean)
    river = Column(Boolean)
    sea = Column(Boolean)
    mountain = Column(Boolean)
    mine = Column(Boolean)

    #buildings = relationship('Building', back_populates='city')
    #characters = relationship('Character', back_populates='city')

    note = Column(String(10000))


class Building(Base):
    __tablename__ = 'buildings'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    kind = Column(String)

    city_id = Column(Integer, ForeignKey('cities.id'))
    #city = relationship(City, back_populates='buildings')

    #characters = relationship('Character', back_populates='building')

    note = Column(String(10000))


class Family(Base):
    __tablename__ = 'families'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # characters = relationship('Character', back_populates='families')


class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fname = Column(String)
    culture = Column(String)
    race = Column(String)
    gender = Column(String)
    age = Column(Integer)
    social_group = Column(String)
    profession = Column(String)
    wealth = Column(String)
    attributes = Column(String)
    moralities = Column(Integer)
    family_role = Column(Integer)

    family_id = Column(Integer, ForeignKey('families.id'))
    # family = relationship(Family, back_populates='characters') # Breaks base.City????

    city_id = Column(Integer, ForeignKey('cities.id'))
    #city = relationship(City, back_populates='characters')

    building_id = Column(Integer, ForeignKey('buildings.id'))
    #building = relationship(Building, back_populates='characters')

    work_building_id = Column(Integer, ForeignKey('buildings.id'))

    visiting_id = Column(Integer, ForeignKey('buildings.id'))

    note = Column(String(10000))


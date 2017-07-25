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

    # buildings = relationship('Building', back_populates='city')
    # characters = relationship('Character', back_populates='city')

    note = Column(String(10000))


class Building(Base):
    __tablename__ = 'buildings'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    kind = Column(String)

    city_id = Column(Integer, ForeignKey('cities.id'))

    note = Column(String(10000))

class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    family = Column(Boolean)
    live = Column(Boolean)
    work = Column(Boolean)
    visit = Column(Boolean)

    building_id = Column(Integer, ForeignKey('buildings.id'))


class Family(Base):
    __tablename__ = 'families'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # characters = relationship('Character', back_populates='families')


class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    culture = Column(String)
    race = Column(String)
    gender = Column(String)
    age = Column(Integer)
    social_group = Column(String)
    profession = Column(String)
    wealth = Column(String)
    attributes = Column(String)
    moralities = Column(String)
    family_role = Column(String)
    groups = Column(String)

    family_id = Column(Integer, ForeignKey('families.id'))
    spouse_family_id = Column(Integer, ForeignKey('families.id'))

    building_id = Column(Integer)  # To be removed after groups are added

    note = Column(String(10000))

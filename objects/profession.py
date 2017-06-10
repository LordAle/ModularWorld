

class Profession:

    def __init__(self, name=None, wealth=0, geo_restric=None, unique=0):
        self.name = name  # The name of the profession
        self.wealth = wealth  # Wealth of the profession, between 0 and 1, 1 being the richest person in the area
        self.geo_restric = geo_restric  # Needed geographic feature needed for the profession. Support strings 'Plain', 'Forest', 'Mountain', 'Mine', 'Sea', 'River' and 'Water'
        self.unique = unique  # Bool, determine if more than one person can have this job in the same city


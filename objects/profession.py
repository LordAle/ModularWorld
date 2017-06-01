

class Profession():

    def __init__(self, name=None, wealth=0, class_list=['Undefined'], class_odds=[1], geo_restric=None, unique=0):
        self.name = name  # The name of the profession
        self.wealth = wealth  # Wealth of the profession, between 0 and 1, 1 being the richest person in the area
        self.class_list = class_list  # Possible classes people of this profession can be
        self.class_odds = class_odds  # Odds associated with each class
        self.geo_restric = geo_restric  # Needed geographic feature needed for the profession. Support strings 'Plain', 'Forest', 'Mountain', 'Mine', 'Sea', 'River' and 'Water'
        self.unique = unique  # Determine if more than one person can have this job in the same city

        if len(class_list) != len(class_odds):
            print('Lists of different length in a Profession instance named {0}, error will occur!'.format(self.name))


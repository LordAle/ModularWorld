

class Profession():

    def __init__(self, name=None, wealth=0, class_list=['Undefined'], class_odds=[1], geo_restric=None):
        self.name = name
        self.wealth = wealth
        self.class_list = class_list
        self.class_odds = class_odds
        self.geo_restric = geo_restric


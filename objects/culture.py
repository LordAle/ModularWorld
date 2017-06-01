

class Culture:
    """ Class used to determine objects culture """

    def __init__(self, name, main_race, main_race_odds, other_races =[], other_races_odds=[], city_names=[]):
        self.name = name  # All name must be unique
        self.main_race = main_race  # A Race object
        self.main_race_odds = main_race_odds  # An integer used to weight the proportion of the population in a city that is main_race
        self.other_races = other_races  # A list of Race object, determines which races can appear in the city
        self.other_races_odds = other_races_odds  # A list of integer used to weight the proportion of each races in the city
        self.city_names = city_names  # A list of possible city names for that culture

        if len(self.other_races) != len(self.other_races_odds):  # Sends warning message if a error is found in the catalogs csv files
            print('Lists of different length in a Culture instance named {0}, error will occur!'.format(self.name))

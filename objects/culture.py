

class Culture:
    """ Class used to determine objects culture """

    def __init__(self, name, race, morality_modifiers, gender_equality, cultural_openness, other_cultures =[], other_cultures_odds=[]):
        self.name = name  # All name must be unique
        self.race = race  # A Race object, the one that is most present in the culture
        self.morality_modifiers = morality_modifiers  # A list of the modifiers to apply to mean_morality for members of this Culture, e.g. [Altruism+0.3, Order-0.5]
        self.gender_equality = gender_equality  # Determine who can be the head of a house and can inherit building, supports 'Patriarchal', 'Matriarchal' and 'Equal'
        self.cultural_openness = cultural_openness  # An integer x, for each 100 members of this culture, there will be x members of another culture in the city
        self.other_cultures = other_cultures  # A list of Race object, determines which races can appear in the city
        self.other_cultures_odds = other_cultures_odds  # A list of integer used to weight the proportion of each cultures other than the main one in the city
        self.male_names = []  # A list of possible male names for this culture
        self.female_names = []  # A list of possible female names for this culture
        self.family_names = []  # A list of possible family names for this culture
        self.city_names = []  # A list of possible city names for this culture

        if len(self.other_cultures) != len(self.other_cultures_odds):  # Sends warning message if a error is found in the catalogs csv files
            print('Lists of different length in a Culture instance named {0}, error will occur!'.format(self.name))

    def fill_names_lists(self, male, female, family, city):
        self.male_names = male
        self.female_names = female
        self.family_names = family
        self.city_names = city

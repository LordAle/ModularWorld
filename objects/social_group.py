

class Social_Group:

    def __init__(self, name, strict_inheritance, gender, wealth, attributes=[], moralities=[], cultures=[], professions=[], professions_odds=[]):
        self.name = name  # All name must be unique
        self.strict_inheritance = strict_inheritance  # Bool, if true, child will always have his parent's social group
        self.gender = gender  # Required gender to be in this social group, support 'Male' and 'Female'
        self.wealth = wealth  # Required wealth to be in this group, e.g. '>0.6', '<0.4'
        self.attributes = attributes  # A list of required attributes e.g. ['Dexterity>10', 'Wisdom>12']
        self.moralities = moralities  # A list of required moralities rating e.g. ['Altruism<0', 'Order<0.2']
        self.cultures = cultures  # A list of Culture objects that can be part of this social group, empty means anyone e.g. [Human, Elven, Dwarven]
        self.professions = professions  # A list of default Professions in case the characters is generated outside a preset group
        self.professions_odds = professions_odds  # The odds for each of these professions

        if len(professions) != len(professions_odds):  # Sends warning message if a error is found in the catalogs csv files
            print('Social group {0} has professions and professions_odds of different length! Error will occur!'.format(name))

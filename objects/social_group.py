

class Social_Group:

    def __init__(self, name, strict_inheritance, odds, parent_bias, gender, wealth, attributes = [], moralities=[], cultures=[]):
        self.name = name  # All name must be unique
        self.strict_inheritance = strict_inheritance  # Bool, if true, child will always have his parent's social group
        self.odds = odds  # Int, relative chance of children being in this social group if they can
        self.parent_bias = parent_bias  # Int, added to odds if parents are of this social group
        self.gender = gender  # Required gender to be in this social group, support 'Male' and 'Female'
        self.wealth = wealth  # Required wealth to be in this group, e.g. '>0.6', '<0.4'
        self.attributes = attributes  # A list of required attributes e.g. ['Dexterity>10', 'Wisdom>12']
        self.moralities = moralities  # A list of required moralities rating e.g. ['Altruism<0', 'Order<0.2']
        self.cultures = cultures  # A list of Culture objects that can be part of this social group, empty means anyone e.g. [Human, Elven, Dwarven]

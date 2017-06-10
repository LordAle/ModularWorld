

class Race:
    """ Class used to define races"""

    def __init__(self, name, working_age, adult_age, old_age, attr_mod):
        self.name = name  # All name must be unique
        self.working_age = working_age  # Age at which one can leave home and start working
        self.adult_age = adult_age  # Age at which one can have a spouse and children
        self.old_age = old_age  # Age around which average members of this race die
        self.attr_mod = attr_mod  # A list of modified attributes, handled by string manipulation, e.g. ['Dexterity+2', 'Constitution-1']

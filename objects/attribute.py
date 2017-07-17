

class Attribute:
    """ Class used to define character attributes, can be anything from stats, skills or others depending on game system"""

    def __init__(self, name, range, mean, variance, rounding):
        self.name = name  # The name of the attribute
        self.range = range  # Min and max value of attribute [min, max]
        self.mean = mean  # Mean value of attribute
        self.variance = variance  # Standard deviation of attribute
        self.rounding = rounding  # Should this attribute be rounded to the nearest integer

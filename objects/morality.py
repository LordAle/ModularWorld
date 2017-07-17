

class Morality:
    """ Class used to define morality meters, e.g. good/evil, law/chaos"""

    def __init__(self, name, range, mean, variance, rounding, inherited = False):
        self.name = name  # The name of the attribute
        self.range = range  # Min and max value of attribute [min, max]
        self.mean = mean  # Mean value of attribute
        self.variance = variance  # Standard deviation of attribute
        self.rounding = rounding  # Should this attribute be rounded to the nearest integer
        self.inherited = inherited  # Should parent attribute be used instead of cultural mean

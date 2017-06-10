

class Morality:
    """ Class used to define morality meters, e.g. good/evil, law/chaos"""

    def __init__(self, name, bounds, rounding=False, inherited=False, mean=0, variance=0):
        self.name = name  # The name of the morality meter
        self.bounds = bounds  # The possible range of value for the morality meter
        self.rounding = rounding  # Boolean, should the value be rounded down before being stored
        self.inherited = inherited  # Boolean, should the parents mean values be used instead of cultural mean
        self.mean = mean  # Mean value for an average character, can be modified by Culture
        self.variance = variance  # If inherited is true, determine standard deviation around inherited value

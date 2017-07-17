

class Building_Kind():

    def __init__(self, name, min_pop, odds, groups=[]):
        self.name = name  # All name must be unique
        self.min_pop = min_pop  # The minimum population a city must have to randomly generate this building
        self.odds = odds  # Relative weight of this building kind in random generation
        self.groups = groups  # The profession groups that live and work in this building


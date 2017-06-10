

class Building_Kind():

    def __init__(self, name, min_pop, odds, spouse, children, inheritance, groups=[], home_groups=[], work_groups=[]):
        self.name = name  # All name must be unique
        self.min_pop = min_pop  # The minimum population a city must have to randomly generate this building
        self.odds = odds  # Relative weight of this building kind in random generation
        self.spouse = spouse  # Float from 0 to 1, odds that a standard spouse will be added
        self.children = children  # Int, average number of children in building. 0 is always no child
        self.inheritance = inheritance  # Bool, will the oldest child stay at home to inherit the property
        self.groups = groups  # The profession groups that live and work in this building
        self.home_groups = home_groups  # The profession groups that live but do not work in this building
        self.work_groups = work_groups  # The profession groups that only work in this building


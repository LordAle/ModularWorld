

class City_Size:
    """ Class used to determine city size"""

    def __init__(self, name, pop_range=(0, 0)):
        self.name = name  # All name must be unique
        self.pop_range = pop_range  # Range of min and max population i.e. (min, max)

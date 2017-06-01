

class City_Kind:
    """ Class used to determine city kind """

    def __init__(self, name, houses=True):
        self.name = name  # All name must be unique
        self.houses = houses  # Determines if houses can appear in this city

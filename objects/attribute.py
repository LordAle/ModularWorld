

class Attribute:
    """ Class used to define character attributes, can be anything from stats, skills or others depending on game system"""

    def __init__(self, name, dist_type, dist_value):
        self.name = name  # The name of the attribute
        self.dist_type = dist_type  # The random distribution used to generate the attribute value
        self.dist_value = dist_value  # The parameters of the distribution, expects a list to accommodate for different number of parameters

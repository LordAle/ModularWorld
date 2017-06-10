

class Professions_Group:
    """ Class used to create grouping of possible professions to populate buildings """

    def __init__(self, name, main_figure, social_group, dist_type, dist_value, professions, professions_odds):
        self.name = name  # All name must be unique
        self.main_figure = main_figure  # Bool, is this group used as a main figure (determine possible spouse and children)
        self.social_group = social_group  # What Social_Group are these people part of
        self.dist_type = dist_type  # The random distribution type e.g. 'One', 'Flat', 'Triangular', 'Normal'
        self.dist_value = dist_value  # The parameter of the random distribution
        self.professions = professions  # A list of possible Profession objects
        self.professions_odds = professions_odds  # A list of int the same length as professions

        if professions != professions_odds:  # Sends warning message if a error is found in the catalogs csv files
            print('Profession group {0} has professions and professions_odds of different length! Error will occur!'.format(name))

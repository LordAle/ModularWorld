

class Professions_Group:
    """ Class used to create grouping of possible professions to populate buildings """

    def __init__(self, name, social_group, main_figure, spouse, children, inheritance, mean, variance, live, work, professions_main, odds_main, professions, professions_odds):
        self.name = name  # All name must be unique
        self.social_group = social_group  # What Social_Group are these people part of
        self.main_figure = main_figure  # Bool, is there a main figure in this group, using special profession attribution and used in family creation
        self.spouse = spouse  # Float from 0 to 1, odds to have a spouse. Default to 0 if main_figure is false
        self.children = children  # Bool, are the other members of this group (after possible spouse) children of the main figure?
        self.inheritance = inheritance  # Bool, bypass normal rule of children leaving home for oldest children
        self.mean = mean  # Average number of people in this group
        self.variance = variance  # Standard deviation around mean
        self.live = live  # Bool, do the people from this group live in that building?
        self.work = work  # Bool, do the people from this group work in that building?
        self.professions_main = professions_main  # A list of possible Profession Object for this group main_figure
        self.odds_main = odds_main  # A list of int the same length as professions_main
        self.professions = professions  # A list of possible Profession objects
        self.professions_odds = professions_odds  # A list of int the same length as professions

        self.auto_correction()

        if len(professions) != len(professions_odds):  # Sends warning message if a error is found in the catalogs csv files
            print('Profession group {0} has professions and professions_odds of different length! Error will occur!'.format(name))
        if len(professions_main) != len(odds_main):  # Sends warning message if a error is found in the catalogs csv files
            print('Profession group {0} has professions_main and odds_main of different length! Error will occur!'.format(name))

    def auto_correction(self):
        if not self.main_figure:
            self.spouse = 0
            self.children = 0
            self.inheritance = 0
            self.professions_main = []
            self.odds_main = []

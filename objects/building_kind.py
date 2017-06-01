

class Building_Kind():

    def __init__(self, name, odds):
        self.name = name
        self.odds = odds


class Building_Subkind():

    def __init__(self, kind, name, min_pop, odds, groups=[]):
        self.kind = kind
        self.name = name
        self.min_pop = min_pop
        self.odds = odds
        self.groups = groups


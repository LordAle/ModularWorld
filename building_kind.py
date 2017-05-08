

class Building_Kind():

    def __init__(self, name, odds):
        self.name = name
        self.odds = odds


class Building_Subkind():

    def __init__(self, kind, name, min_city_size, odds, groups=[]):
        self.kind = kind
        self.name = name
        self.min_city_size = min_city_size
        self.odds = odds
        self.groups = groups


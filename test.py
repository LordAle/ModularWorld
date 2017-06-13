import random
import catalog


class Selector:

    def __init__(self, selection):
        self.selection = selection

    def simple(self):
        self.remove_error()
        catalog_list = list(self.selection.values())
        print(random.choice(catalog_list))

    def remove_error(self):
        if 'Error' in self.selection:
            del self.selection['Error']

print(catalog.races)
selector = Selector(catalog.races)
selector.simple()
print(catalog.races)

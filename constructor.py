from abc import ABCMeta, abstractmethod


class Constructor:
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_from_db(self, base_item):
        print('Specific set_from_db method must be implemented for each constructor')

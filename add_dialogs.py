from PyQt5 import QtWidgets
from ModularWorldUi.add_building_dialog import Ui_Dialog as add_building_ui
from ModularWorldUi.add_char_dialog import Ui_Dialog as add_char_ui
from ModularWorldUi.add_city_dialog import Ui_Dialog as add_city_ui
import models
import catalog


class add_city_dialog(QtWidgets.QDialog, add_city_ui):

    def __init__(self, main_window):
        super(self.__class__, self).__init__()
        add_city_ui.__init__(self)
        self.setupUi(self)
        self.main_window = main_window

        # Set models to all combobox
        self.cultureModel = models.StringListModel()
        self.cultureModel.setStringList(['Random'] + [x.name for x in catalog.cultures.values() if (x.name != 'Error' and x.name != 'Default)')])
        self.cultureComboBox.setModel(self.cultureModel)

        self.sizeModel = models.StringListModel()
        self.sizeModel.setStringList(['Random'] + [x.name for x in catalog.city_sizes.values() if (x.name != 'Error' and x.name != 'Default)')])
        self.sizeComboBox.setModel(self.sizeModel)

    def set_geography(self):
        if self.geographyButton.isChecked():
            self.geography = 'Random'
        else:
            self.geography = {'forest': self.forestsCheckBox.checkState(), 'plain': self.plainsCheckBox.checkState(), 'river': self.riverCheckBox.checkState(),
                              'sea': self.seaCheckBox.checkState(), 'mountain': self.mountainsCheckBox.checkState(), 'mine': self.minesCheckBox.checkState()}

    def accept(self):
        # Pass all parameters to the add_city method in controller

        self.set_geography()

        param = {'name': self.nameLineEdit.text(),
                 'population': self.populationLineEdit.text(),
                 'culture': self.cultureComboBox.currentText(),
                 'size': self.sizeComboBox.currentText(),
                 'geography': self.geography}

        self.main_window.add_city(param)
        self.close()

class add_building_dialog(QtWidgets.QDialog, add_building_ui):

    def __init__(self, main_window):
        super(self.__class__, self).__init__()
        add_building_ui.__init__(self)
        self.setupUi(self)
        self.main_window = main_window

        # Set models to all combobox
        self.kindModel = models.StringListModel()
        self.kindModel.setStringList(['Random'] + [x.name for x in catalog.building_kinds if (x.name != 'Error' and x.name != 'Default)')])
        self.kindComboBox.setModel(self.kindModel)

    def accept(self):
        param = {'kind': self.kindComboBox.currentText(),
                 'name': self.nameLineEdit.text()
                 }

        auto_populate = self.autoPopulateCheckBox.checkState()

        self.main_window.add_building(param, auto_populate, core_character=core_character)
        self.close()


class add_character_dialog(QtWidgets.QDialog, add_char_ui):

    def __init__(self, main_window):
        super(self.__class__, self).__init__()
        add_char_ui.__init__(self)
        self.setupUi(self)
        self.main_window = main_window

        # Set models to all combobox
        self.cultureModel = models.StringListModel()
        self.cultureModel.setStringList(['Random'] + [x.name for x in catalog.cultures if (x.name != 'Error' and x.name != 'Default)')])
        self.cultureComboBox.setModel(self.cultureModel)

        self.raceModel = models.StringListModel()
        self.raceModel.setStringList([x.name for x in catalog.races if (x.name != 'Error' and x.name != 'Default)')])
        self.raceComboBox.setModel(self.raceModel)

        self.genderModel = models.StringListModel()
        self.genderModel.setStringList(['Random', 'Male', 'Female'])
        self.genderComboBox.setModel(self.genderModel)

        self.socialGroupModel = models.StringListModel()
        self.socialGroupModel.setStringList([x.name for x in catalog.social_groups if (x.name != 'Error' and x.name != 'Default)')])
        self.socialGroupComboBox.setModel(self.socialGroupModel)

        self.professionModel = models.StringListModel()
        self.professionModel.setStringList([x.name for x in catalog.professions if (x.name != 'Error' and x.name != 'Default)')])
        self.professionComboBox.setModel(self.professionModel)

        self.familyRoleModel = models.StringListModel()
        self.familyRoleModel.setStringList(['None', 'Master', 'Spouse', 'Child'])
        self.familyRoleComboBox.setModel(self.familyRoleModel)

    def accept(self):
        param = {'name': self.coreNameLineEdit.text(),
                 'fname': self.familyNameLineEdit.text(),
                 'culture': self.cultureComboBox.currentText(),
                 'race': self.raceComboBox.currentText(),
                 'gender': self.genderComboBox.currentText(),
                 'age': self.ageLineEdit.text(),
                 'social group': self.socialGroupComboBox.currentText(),
                 'profession': self.professionComboBox.currentText(),
                 'wealth': self.wealthLineEdit.text(),
                 'family role': self.familyRoleComboBox.currentText(),
                 'live': self.liveCheckBox.checkState(),
                 'work': self.workCheckBox.checkState()
                 }

        self.main_window.add_character(param)
        self.close()

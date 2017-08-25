from PyQt5 import QtWidgets, QtGui
from ModularWorldUi.add_city_dialog import Ui_Dialog as add_city_ui
from ModularWorldUi.add_building_dialog import Ui_Dialog as add_building_ui
from ModularWorldUi.add_group_dialog import Ui_Dialog as add_group_ui
from ModularWorldUi.add_char_dialog import Ui_Dialog as add_char_ui
import models
import catalog


class add_city_dialog(QtWidgets.QDialog, add_city_ui):

    def __init__(self, main_window):
        super(self.__class__, self).__init__()
        add_city_ui.__init__(self)
        self.setupUi(self)
        self.main_window = main_window

        # Signal connect
        self.geographyButton.toggled.connect(self.geo_state)

        # self.forestCheckBox.setIcon(QtGui.QIcon('ModularWorldUi/Icons/Tree.jpg'))

        # Set models to all combobox
        culture_list = [x.name for x in catalog.cultures.values() if not (x.name == 'Error' or x.name == 'Default')]
        culture_list.sort()
        self.cultureModel = models.StringListModel()
        self.cultureModel.setStringList(['Random'] + culture_list)
        self.cultureComboBox.setModel(self.cultureModel)

        size_list = [x.name for x in catalog.city_sizes.values() if (x.name != 'Error' and x.name != 'Default')]
        size_list.sort()
        self.sizeModel = models.StringListModel()
        self.sizeModel.setStringList(['Random'] + size_list)
        self.sizeComboBox.setModel(self.sizeModel)

    def geo_state(self):
        if self.geographyButton.isChecked():
            self.forestCheckBox.setEnabled(False)
            self.plainCheckBox.setEnabled(False)
            self.riverCheckBox.setEnabled(False)
            self.seaCheckBox.setEnabled(False)
            self.mountainCheckBox.setEnabled(False)
            self.mineCheckBox.setEnabled(False)
        elif not self.geographyButton.isChecked():
            self.forestCheckBox.setEnabled(True)
            self.plainCheckBox.setEnabled(True)
            self.riverCheckBox.setEnabled(True)
            self.seaCheckBox.setEnabled(True)
            self.mountainCheckBox.setEnabled(True)
            self.mineCheckBox.setEnabled(True)

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
        kind_list = [x.name for x in catalog.building_kinds.values() if (x.name != 'Error' and x.name != 'Default')]
        kind_list.sort()
        self.kindModel = models.StringListModel()
        self.kindModel.setStringList(['Random'] + kind_list)
        self.kindComboBox.setModel(self.kindModel)

    def accept(self):
        param = {'kind': self.kindComboBox.currentText(),
                 'name': self.nameLineEdit.text()
                 }

        auto_populate = self.autoPopulateCheckBox.checkState()

        self.main_window.add_building(param, auto_populate)
        self.close()


class add_group_dialog(QtWidgets.QDialog, add_group_ui):

    def __init__(self, main_window):
        super(self.__class__, self).__init__()
        add_char_ui.__init__(self)
        self.setupUi(self)
        self.main_window = main_window

        # Signal connect
        self.presetRadioButton.toggled.connect(self.preset_state)

        # Set models to combobox
        preset_list = [x.name for x in catalog.professions_groups.values()]
        preset_list.sort()
        self.presetModel = models.StringListModel()
        self.presetModel.setStringList(preset_list)
        self.presetComboBox.setModel(self.presetModel)

    def preset_state(self):
        if self.presetRadioButton.isChecked():
            self.presetComboBox.setEnabled(True)
            self.nameLineEdit.setEnabled(False)
            self.familyCheckBox.setEnabled(False)
            self.liveCheckBox.setEnabled(False)
            self.workCheckBox.setEnabled(False)
            self.visitCheckBox.setEnabled(False)
        elif not self.presetRadioButton.isChecked():
            self.presetComboBox.setEnabled(False)
            self.nameLineEdit.setEnabled(True)
            self.familyCheckBox.setEnabled(True)
            self.liveCheckBox.setEnabled(True)
            self.workCheckBox.setEnabled(True)
            self.visitCheckBox.setEnabled(True)

    def accept(self):
        param = {'name': self.nameLineEdit.text(),
                 'family': self.familyCheckBox.checkState(),
                 'live': self.liveCheckBox.checkState(),
                 'work': self.workCheckBox.checkState(),
                 'visit': self.visitCheckBox.checkState()}

        preset = self.presetRadioButton.isChecked()
        preset_name = self.presetComboBox.currentText()

        self.main_window.add_group(param, preset, preset_name)
        self.close()

class add_character_dialog(QtWidgets.QDialog, add_char_ui):

    def __init__(self, main_window, in_group):
        super(self.__class__, self).__init__()
        add_char_ui.__init__(self)
        self.setupUi(self)
        self.main_window = main_window

        # Set models to all combobox
        self.cultureModel = models.StringListModel()
        self.cultureModel.setStringList(['Random'] + [x.name for x in catalog.cultures.values() if (x.name != 'Error' and x.name != 'Default')])
        self.cultureComboBox.setModel(self.cultureModel)

        self.raceModel = models.StringListModel()
        self.raceModel.setStringList(['Random'] + [x.name for x in catalog.races.values() if (x.name != 'Error' and x.name != 'Default')])
        self.raceComboBox.setModel(self.raceModel)

        self.genderModel = models.StringListModel()
        self.genderModel.setStringList(['Random', 'Male', 'Female'])
        self.genderComboBox.setModel(self.genderModel)

        self.socialGroupModel = models.StringListModel()
        self.socialGroupModel.setStringList(['Random'] + [x.name for x in catalog.social_groups.values() if (x.name != 'Error' and x.name != 'Default')])
        self.socialGroupComboBox.setModel(self.socialGroupModel)

        self.professionModel = models.StringListModel()
        self.professionModel.setStringList(['Random'] + [x.name for x in catalog.professions.values() if (x.name != 'Error' and x.name != 'Default')])
        self.professionComboBox.setModel(self.professionModel)

        self.familyRoleModel = models.StringListModel()
        if in_group.is_family:
            if 'Master' in [x.family_role.role for x in in_group.characters]:
                self.familyRoleModel.setStringList(['Child', 'Spouse'])
            else:
                self.familyRoleModel.setStringList(['Master'])
        else:
            self.familyRoleModel.setStringList(['None'])
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
                 }

        self.main_window.add_character(param)
        self.close()

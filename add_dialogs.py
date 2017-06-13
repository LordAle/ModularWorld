from catalogs import catalog_character
# from catalogs import catalog_city
from catalogs import catalog_profession
from catalogs import catalog_building
import catalog
from PyQt5 import QtWidgets
import models
from ModularWorldUi.add_building_dialog import Ui_Dialog as add_building_ui
from ModularWorldUi.add_char_dialog import Ui_Dialog as add_char_ui
from ModularWorldUi.add_city_dialog import Ui_Dialog as add_city_ui


class add_city_dialog(QtWidgets.QDialog, add_city_ui):

    def __init__(self, main_window):
        super(self.__class__, self).__init__()
        add_city_ui.__init__(self)
        self.setupUi(self)
        self.main_window = main_window

        # Set models to all combobox
        self.cultureModel = models.StringListModel()
        self.cultureModel.setStringList(['Random'] + [x.name for x in catalog.cultures.values() if x.name != 'Error'])
        self.cultureComboBox.setModel(self.cultureModel)

        self.sizeModel = models.StringListModel()
        self.sizeModel.setStringList(['Random'] + [x.name for x in catalog.city_sizes.values() if x.name != 'Error'])
        self.sizeComboBox.setModel(self.sizeModel)

    def accept(self):
        # Pass all parameters to the add_city method in controller
        if self.geographyButton.isChecked():
            geography = 'Random'
        else:
            geography = {'forest': self.forestsCheckBox.checkState(), 'plain': self.plainsCheckBox.checkState(), 'river': self.riverCheckBox.checkState(),
                        'sea': self.seaCheckBox.checkState(), 'mountain': self.mountainsCheckBox.checkState(), 'mine': self.minesCheckBox.checkState()}

        param = {'name': self.nameLineEdit.text(),
                 'population': self.populationLineEdit.text(),
                 'culture': self.cultureComboBox.currentText(),
                 'size': self.sizeComboBox.currentText(),
                 'geography':geography}

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
        self.kindModel.setStringList(['Random'] + [x.name for x in catalog_building.kinds])
        self.kindComboBox.setModel(self.kindModel)

        self.subkindModel = models.StringListModel()
        self.subkindModel.setStringList(['Random'])
        self.subkindComboBox.setModel(self.subkindModel)

        self.raceModel = models.StringListModel()
        self.raceModel.setStringList(['Random'] + catalog_character.races)
        self.raceComboBox.setModel(self.raceModel)

        self.genderModel = models.StringListModel()
        self.genderModel.setStringList(['Random'] + catalog_character.genders)
        self.genderComboBox.setModel(self.genderModel)

        self.professionModel = models.StringListModel()
        self.professionModel.setStringList(['Random'] + [x.name for x in catalog_profession.professions])
        self.professionComboBox.setModel(self.professionModel)

        self.wealthModel = models.StringListModel()
        self.wealthModel.setStringList(['Random'] + catalog_character.wealth)
        self.wealthComboBox.setModel(self.wealthModel)

        self.classModel = models.StringListModel()
        self.classModel.setStringList(['Random'] + catalog_character.classes)
        self.classComboBox.setModel(self.classModel)

        #Signals emission
        self.kindComboBox.currentIndexChanged.connect(self.update_subkind)

    def update_subkind(self):
        subkind_list = [x.name for x in catalog_building.subkinds if x.kind.name == self.kindComboBox.currentText()]
        self.subkindModel.setStringList(['Random'] + subkind_list)

    def accept(self):
        param = {'kind':self.kindComboBox.currentText(),
                 'subkind':self.subkindComboBox.currentText(),
                'name':self.nameLineEdit.text()}

        core_character = {'name':self.coreNameLineEdit.text(),
                        'fname':self.familyNameLineEdit.text(),
                        'race':self.raceComboBox.currentText(),
                        'gender':self.genderComboBox.currentText(),
                        'age':self.ageLineEdit.text(),
                        'role':self.roleLineEdit.text(),
                        'profession':self.professionComboBox.currentText(),
                        'wealth':self.wealthComboBox.currentText(),
                        'class':self.classComboBox.currentText(),
                        'level':self.levelLineEdit.text()}

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
        self.raceModel = models.StringListModel()
        self.raceModel.setStringList(['Random'] + catalog_character.races)
        self.raceComboBox.setModel(self.raceModel)

        self.genderModel = models.StringListModel()
        self.genderModel.setStringList(['Random'] + catalog_character.genders)
        self.genderComboBox.setModel(self.genderModel)

        self.roleModel = models.StringListModel()
        self.roleModel.setStringList(catalog_character.roles)
        self.roleComboBox.setModel(self.roleModel)

        self.professionModel = models.StringListModel()
        self.professionModel.setStringList(['Random'] + [x.name for x in catalog_profession.professions])
        self.professionComboBox.setModel(self.professionModel)

        self.wealthModel = models.StringListModel()
        self.wealthModel.setStringList(['Random'] + catalog_character.wealth)
        self.wealthComboBox.setModel(self.wealthModel)

        self.classModel = models.StringListModel()
        self.classModel.setStringList(['Random'] + catalog_character.classes)
        self.classComboBox.setModel(self.classModel)

    def accept(self):
        param ={'name':self.coreNameLineEdit.text(),
                'fname':self.familyNameLineEdit.text(),
                'race':self.raceComboBox.currentText(),
                'gender':self.genderComboBox.currentText(),
                'age':self.ageLineEdit.text(),
                'role':self.roleComboBox.currentText(),
                'profession':self.professionComboBox.currentText(),
                'wealth':self.wealthComboBox.currentText(),
                'class':self.classComboBox.currentText(),
                'level':self.levelLineEdit.text()}

        self.main_window.add_character(param)
        self.close()

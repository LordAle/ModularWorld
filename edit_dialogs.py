from PyQt5 import QtWidgets, QtSql
from ModularWorldUi.edit_city_dialog import Ui_Dialog as edit_city_ui
from ModularWorldUi.edit_building_dialog import Ui_Dialog as edit_building_ui
from ModularWorldUi.edit_group_dialog import Ui_Dialog as edit_group_ui
from ModularWorldUi.edit_char_dialog import Ui_Dialog as edit_char_ui
import models
import catalog
import base
import db_connector


class edit_city_dialog(QtWidgets.QDialog, edit_city_ui):

    def __init__(self, main_window, edited_city):
        super(self.__class__, self).__init__()
        edit_city_ui.__init__(self)
        self.setupUi(self)
        self.main_window = main_window
        self.edited_city = edited_city

        # Set models to all combobox
        culture_list = [x.name for x in catalog.cultures.values() if not (x.name == 'Error' or x.name == 'Default')]
        culture_list.sort()
        self.cultureModel = models.StringListModel()
        self.cultureModel.setStringList(culture_list)
        self.cultureComboBox.setModel(self.cultureModel)

        size_list = [x.name for x in catalog.city_sizes.values() if (x.name != 'Error' and x.name != 'Default')]
        size_list.sort()
        self.sizeModel = models.StringListModel()
        self.sizeModel.setStringList(size_list)
        self.sizeComboBox.setModel(self.sizeModel)

        # Set default value to edited item value
        self.nameLineEdit.setText(edited_city.name)
        self.cultureComboBox.setCurrentText(edited_city.culture.name)
        self.sizeComboBox.setCurrentText(edited_city.size.name)
        self.populationLineEdit.setText(str(edited_city.population))
        if edited_city.forest:
            self.forestCheckBox.setChecked(True)
        if edited_city.plain:
            self.plainCheckBox.setChecked(True)
        if edited_city.river:
            self.riverCheckBox.setChecked(True)
        if edited_city.sea:
            self.seaCheckBox.setChecked(True)
        if edited_city.mountain:
            self.mountainCheckBox.setChecked(True)
        if edited_city.mine:
            self.mineCheckBox.setChecked(True)

    def accept(self):
        geography = {'forest': self.forestCheckBox.checkState(), 'plain': self.plainCheckBox.checkState(), 'river': self.riverCheckBox.checkState(),
                     'sea': self.seaCheckBox.checkState(), 'mountain': self.mountainCheckBox.checkState(), 'mine': self.mineCheckBox.checkState()}
        param = {'name': self.nameLineEdit.text(),
                 'population': self.populationLineEdit.text(),
                 'culture': self.cultureComboBox.currentText(),
                 'size': self.sizeComboBox.currentText(),
                 'geography': geography}

        self.edited_city.set_from_edit_box(param)
        city_connector = db_connector.Db_Connector(base.City)
        city_connector.full_update(self.edited_city, self.edited_city.id)
        city_connector.close_session()
        self.main_window.build_tree_model()
        self.close()


class edit_builduing_dialog(QtWidgets.QDialog, edit_building_ui):

    def __init__(self, main_window, edited_building):
        super(self.__class__, self).__init__()
        edit_building_ui.__init__(self)
        self.setupUi(self)
        self.main_window = main_window
        self.edited_building = edited_building

        # Set models to all combobox
        kind_list = [x.name for x in catalog.building_kinds.values() if not (x.name == 'Error' or x.name == 'Default')]
        kind_list.sort()
        self.kindModel = models.StringListModel()
        self.kindModel.setStringList(kind_list)
        self.kindComboBox.setModel(self.kindModel)

        query = QtSql.QSqlQuery("SELECT name, id FROM cities")
        while query.next():
            self.inCityComboBox.addItem(query.value(0), query.value(1))

        # Set default value to edited item value
        self.kindComboBox.setCurrentText(edited_building.kind.name)
        self.nameLineEdit.setText(edited_building.name)
        city_box_index = self.inCityComboBox.findData(edited_building.in_city.id, role=256)
        self.inCityComboBox.setCurrentIndex(city_box_index)

    def accept(self):
        param = {'name': self.nameLineEdit.text(),
                 'kind': self.kindComboBox.currentText(),
                 'in_city_id': self.inCityComboBox.currentData(256)}

        self.edited_building.set_from_edit_box(param)
        building_connector = db_connector.Db_Connector(base.Building)
        building_connector.full_update(self.edited_building, self.edited_building.id)
        building_connector.close_session()
        self.main_window.build_tree_model()
        self.close()


class edit_group_dialog(QtWidgets.QDialog, edit_group_ui):

    def __init__(self, main_window, edited_group):
        super(self.__class__, self).__init__()
        edit_group_ui.__init__(self)
        self.setupUi(self)
        self.main_window = main_window
        self.edited_group = edited_group

        # Set models to all combobox
        query = QtSql.QSqlQuery("SELECT name, id FROM buildings")
        while query.next():
            self.inBuildingComboBox.addItem(query.value(0), query.value(1))

        # Set default value to edited item value
        self.nameLineEdit.setText(self.edited_group.name)
        if self.edited_group.is_family:
            self.familyCheckBox.setChecked(True)
        if self.edited_group.is_live:
            self.liveCheckBox.setChecked(True)
        if self.edited_group.is_work:
            self.workCheckBox.setChecked(True)
        if self.edited_group.is_visit:
            self.visitCheckBox.setChecked(True)
        building_box_index = self.inBuildingComboBox.findData(edited_group.in_building.id, role=256)
        self.inBuildingComboBox.setCurrentIndex(building_box_index)

    def accept(self):
        param = {'name': self.nameLineEdit.text(),
                 'family': self.familyCheckBox.checkState(),
                 'live': self.liveCheckBox.checkState(),
                 'work': self.workCheckBox.checkState(),
                 'visit': self.visitCheckBox.checkState(),
                 'in_building_id': self.inBuildingComboBox.currentData(256)}

        self.edited_group.set_from_edit_box(param)
        group_connector = db_connector.Db_Connector(base.Group)
        group_connector.full_update(self.edited_group, self.edited_group.id)
        group_connector.close_session()
        self.main_window.build_tree_model()
        self.close()


class edit_character_dialog(QtWidgets.QDialog, edit_char_ui):

    def __init__(self, main_window, edited_char):
        super(self.__class__, self).__init__()
        edit_char_ui.__init__(self)
        self.setupUi(self)
        self.main_window = main_window
        self.edited_char = edited_char

        # Set models to all combobox
        self.cultureModel = models.StringListModel()
        self.cultureModel.setStringList([x.name for x in catalog.cultures.values() if (x.name != 'Error' and x.name != 'Default')])
        self.cultureComboBox.setModel(self.cultureModel)

        self.raceModel = models.StringListModel()
        self.raceModel.setStringList([x.name for x in catalog.races.values() if (x.name != 'Error' and x.name != 'Default')])
        self.raceComboBox.setModel(self.raceModel)

        self.genderModel = models.StringListModel()
        self.genderModel.setStringList(['Male', 'Female'])
        self.genderComboBox.setModel(self.genderModel)

        self.socialGroupModel = models.StringListModel()
        self.socialGroupModel.setStringList([x.name for x in catalog.social_groups.values() if (x.name != 'Error' and x.name != 'Default')])
        self.socialGroupComboBox.setModel(self.socialGroupModel)

        self.professionModel = models.StringListModel()
        self.professionModel.setStringList([x.name for x in catalog.professions.values() if (x.name != 'Error' and x.name != 'Default')])
        self.professionComboBox.setModel(self.professionModel)

        self.familyRoleModel = models.StringListModel()
        self.familyRoleModel.setStringList(['None', 'Master', 'Child', 'Spouse'])
        self.familyRoleComboBox.setModel(self.familyRoleModel)

        # Set default value to edited item value
        self.coreNameLineEdit.setText(self.edited_char.name)
        self.familyNameLineEdit.setText(self.edited_char.family.name)
        self.cultureComboBox.setCurrentText(self.edited_char.culture.name)
        self.raceComboBox.setCurrentText(self.edited_char.race.name)
        self.genderComboBox.setCurrentText(self.edited_char.gender)
        self.ageLineEdit.setText(str(self.edited_char.age))
        self.socialGroupComboBox.setCurrentText(self.edited_char.social_group.name)
        self.professionComboBox.setCurrentText(self.edited_char.profession.name)
        self.wealthLineEdit.setText(str(self.edited_char.wealth))
        try:
            self.familyRoleComboBox.setCurrentText(self.edited_char.family_role.role)
        except:
            self.familyRoleComboBox.setCurrentText('None')

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

        self.edited_char.set_from_edit_box(param)
        char_connector = db_connector.Db_Connector(base.Character)
        char_connector.full_update(self.edited_char, self.edited_char.id)
        char_connector.close_session()
        self.main_window.build_tree_model()
        self.close()


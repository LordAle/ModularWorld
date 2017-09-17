from PyQt5 import QtWidgets, QtSql
from ModularWorldUi.edit_city_dialog import Ui_Dialog as edit_city_ui
from ModularWorldUi.edit_building_dialog import Ui_Dialog as edit_building_ui
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
        box_index = self.inCityComboBox.findData(edited_building.in_city.id, role=256)
        self.inCityComboBox.setCurrentIndex(box_index)

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




from PyQt5 import QtWidgets
from ModularWorldUi.edit_city_dialog import Ui_Dialog as edit_city_ui
import models
import catalog


class edit_city_dialog(QtWidgets.QDialog, edit_city_ui):

    def __init__(self, main_window, edited_city):
        super(self.__class__, self).__init__()
        edit_city_ui.__init__(self)
        self.setupUi(self)
        self.main_window = main_window

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
        self.populationLineEdit.setText(edited_city.population)


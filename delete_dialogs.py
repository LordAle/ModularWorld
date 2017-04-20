from PyQt5 import QtCore, QtWidgets, QtSql
from ModularWorldUi.delete_dialog import Ui_Dialog as delete_ui
import models


class delete_dialog(QtWidgets.QDialog, delete_ui):

    def __init__(self, main_window, table, text):
        super(self.__class__, self).__init__()
        delete_ui.__init__(self)
        self.setupUi(self)
        self.main_window = main_window
        self.table = table
        self.label_2.setText(text)

    def accept(self):
        if self.table == 'characters':
            self.main_window.delete_character()
        elif self.table == 'buildings':
            self.main_window.delete_building()
        elif self.table == 'cities':
            self.main_window.delete_city()

        self.close()
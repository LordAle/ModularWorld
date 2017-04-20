import sys
from PyQt5 import Qt, QtCore, QtWidgets, QtGui, QtSql


class StringListModel(QtCore.QStringListModel):

    def __init__(self):
        super().__init__()


class ItemModel (QtGui.QStandardItemModel):

    def __init__(self):
        super().__init__()


class ValueListModel(QtCore.QAbstractListModel):

    def __init__(self):
        super().__init__()
        self.values = []

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self.values)

    def data(self, index, role=None):
        print('Inside data function')
        if role == QtCore.Qt.DisplayRole:
            print(self.values[index.row()])
            return self.values[index.row()]
        return QtCore.QVariant()

    def set_values(self, values):
        self.values = values
        print(self.dataChanged.emit(0,0))
        print('Bloup)')


class SqlQueryModel(QtSql.QSqlQueryModel):

    def __init__(self):
        super().__init__()


class SqlTableModel(QtSql.QSqlTableModel):

    def __init__(self, db=None):
        super().__init__()


class SqlRelationalModel(QtSql.QSqlRelationalTableModel):

    def __init__(self, db=None):
        super().__init__()
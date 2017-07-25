from PyQt5 import Qt, QtCore, QtWidgets, QtGui, QtSql


class StringListModel(QtCore.QStringListModel):

    def __init__(self):
        super().__init__()


class TreeModel (QtGui.QStandardItemModel):

    def __init__(self):
        super().__init__()


class SqlQueryModel(QtSql.QSqlQueryModel):

    def __init__(self):
        super().__init__()


class SqlTableModel(QtSql.QSqlTableModel):

    def __init__(self, db=None):
        super().__init__()


class SqlRelationalModel(QtSql.QSqlRelationalTableModel):

    def __init__(self, db=None):
        super().__init__()
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_dev.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1064, 837)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.treeView = QtWidgets.QTreeView(self.centralWidget)
        self.treeView.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.treeView.setObjectName("treeView")
        self.verticalLayout_5.addWidget(self.treeView)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.listViewSelectedValue = QtWidgets.QListView(self.centralWidget)
        self.listViewSelectedValue.setMaximumSize(QtCore.QSize(300, 16777215))
        self.listViewSelectedValue.setObjectName("listViewSelectedValue")
        self.verticalLayout_6.addWidget(self.listViewSelectedValue)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tableViewContent = QtWidgets.QTableView(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableViewContent.sizePolicy().hasHeightForWidth())
        self.tableViewContent.setSizePolicy(sizePolicy)
        self.tableViewContent.setMinimumSize(QtCore.QSize(512, 0))
        self.tableViewContent.setSortingEnabled(True)
        self.tableViewContent.setObjectName("tableViewContent")
        self.verticalLayout_4.addWidget(self.tableViewContent)
        self.tableViewSpecial = QtWidgets.QTableView(self.centralWidget)
        self.tableViewSpecial.setMinimumSize(QtCore.QSize(512, 0))
        self.tableViewSpecial.setObjectName("tableViewSpecial")
        self.verticalLayout_4.addWidget(self.tableViewSpecial)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.showFamilyLabel = QtWidgets.QLabel(self.centralWidget)
        self.showFamilyLabel.setMaximumSize(QtCore.QSize(150, 16777215))
        self.showFamilyLabel.setObjectName("showFamilyLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.showFamilyLabel)
        self.pushButtonShowFamily = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonShowFamily.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButtonShowFamily.setObjectName("pushButtonShowFamily")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pushButtonShowFamily)
        self.visitorLabel = QtWidgets.QLabel(self.centralWidget)
        self.visitorLabel.setMaximumSize(QtCore.QSize(150, 16777215))
        self.visitorLabel.setObjectName("visitorLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.visitorLabel)
        self.comboBoxVisitor = QtWidgets.QComboBox(self.centralWidget)
        self.comboBoxVisitor.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBoxVisitor.setObjectName("comboBoxVisitor")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBoxVisitor)
        self.numberLabel = QtWidgets.QLabel(self.centralWidget)
        self.numberLabel.setObjectName("numberLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.numberLabel)
        self.lineEditVisitor = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEditVisitor.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditVisitor.setObjectName("lineEditVisitor")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditVisitor)
        self.visitorLabel_2 = QtWidgets.QLabel(self.centralWidget)
        self.visitorLabel_2.setObjectName("visitorLabel_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.visitorLabel_2)
        self.pushButtonVisitor = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonVisitor.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButtonVisitor.setObjectName("pushButtonVisitor")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pushButtonVisitor)
        self.verticalLayout.addLayout(self.formLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1064, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuShow = QtWidgets.QMenu(self.menuBar)
        self.menuShow.setObjectName("menuShow")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionNewDatabase = QtWidgets.QAction(MainWindow)
        self.actionNewDatabase.setObjectName("actionNewDatabase")
        self.actionLoadDatabase = QtWidgets.QAction(MainWindow)
        self.actionLoadDatabase.setObjectName("actionLoadDatabase")
        self.actionCity_table = QtWidgets.QAction(MainWindow)
        self.actionCity_table.setObjectName("actionCity_table")
        self.actionBuilding_table = QtWidgets.QAction(MainWindow)
        self.actionBuilding_table.setObjectName("actionBuilding_table")
        self.actionCharacter_table = QtWidgets.QAction(MainWindow)
        self.actionCharacter_table.setObjectName("actionCharacter_table")
        self.actionAddCity = QtWidgets.QAction(MainWindow)
        self.actionAddCity.setObjectName("actionAddCity")
        self.actionAddBuilding = QtWidgets.QAction(MainWindow)
        self.actionAddBuilding.setObjectName("actionAddBuilding")
        self.actionAddGroup = QtWidgets.QAction(MainWindow)
        self.actionAddGroup.setObjectName("actionAddGroup")
        self.actionAddCharacter = QtWidgets.QAction(MainWindow)
        self.actionAddCharacter.setObjectName("actionAddCharacter")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionEdit = QtWidgets.QAction(MainWindow)
        self.actionEdit.setObjectName("actionEdit")
        self.menuFile.addAction(self.actionNewDatabase)
        self.menuFile.addAction(self.actionLoadDatabase)
        self.menuShow.addAction(self.actionCity_table)
        self.menuShow.addAction(self.actionBuilding_table)
        self.menuShow.addAction(self.actionCharacter_table)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuShow.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.showFamilyLabel.setText(_translate("MainWindow", "Show family"))
        self.pushButtonShowFamily.setText(_translate("MainWindow", "Show Family"))
        self.visitorLabel.setText(_translate("MainWindow", "Visitor"))
        self.numberLabel.setText(_translate("MainWindow", "Number"))
        self.visitorLabel_2.setText(_translate("MainWindow", "Visitor"))
        self.pushButtonVisitor.setText(_translate("MainWindow", "Visitor"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuShow.setTitle(_translate("MainWindow", "Show"))
        self.actionNewDatabase.setText(_translate("MainWindow", "New Database"))
        self.actionLoadDatabase.setText(_translate("MainWindow", "Load Database"))
        self.actionLoadDatabase.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionCity_table.setText(_translate("MainWindow", "City table"))
        self.actionBuilding_table.setText(_translate("MainWindow", "Building table"))
        self.actionCharacter_table.setText(_translate("MainWindow", "Character table"))
        self.actionAddCity.setText(_translate("MainWindow", "Add City"))
        self.actionAddBuilding.setText(_translate("MainWindow", "Add Building"))
        self.actionAddGroup.setText(_translate("MainWindow", "Add Group"))
        self.actionAddCharacter.setText(_translate("MainWindow", "Add Character"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionEdit.setText(_translate("MainWindow", "Edit"))


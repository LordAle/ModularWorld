# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1413, 840)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 1391, 761))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listViewCities = QtWidgets.QListView(self.horizontalLayoutWidget_3)
        self.listViewCities.setObjectName("listViewCities")
        self.verticalLayout.addWidget(self.listViewCities)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonAddCity = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButtonAddCity.setObjectName("pushButtonAddCity")
        self.horizontalLayout.addWidget(self.pushButtonAddCity)
        self.pushButtonDeleteCity = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButtonDeleteCity.setObjectName("pushButtonDeleteCity")
        self.horizontalLayout.addWidget(self.pushButtonDeleteCity)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.listViewBuildings = QtWidgets.QListView(self.horizontalLayoutWidget_3)
        self.listViewBuildings.setObjectName("listViewBuildings")
        self.verticalLayout_2.addWidget(self.listViewBuildings)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonAddBuilding = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButtonAddBuilding.setObjectName("pushButtonAddBuilding")
        self.horizontalLayout_2.addWidget(self.pushButtonAddBuilding)
        self.pushButtonDeleteBuilding = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButtonDeleteBuilding.setObjectName("pushButtonDeleteBuilding")
        self.horizontalLayout_2.addWidget(self.pushButtonDeleteBuilding)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.listViewCharacters = QtWidgets.QListView(self.horizontalLayoutWidget_3)
        self.listViewCharacters.setObjectName("listViewCharacters")
        self.verticalLayout_3.addWidget(self.listViewCharacters)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButtonAddCharacter = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButtonAddCharacter.setObjectName("pushButtonAddCharacter")
        self.horizontalLayout_3.addWidget(self.pushButtonAddCharacter)
        self.pushButtonDeleteCharacter = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButtonDeleteCharacter.setObjectName("pushButtonDeleteCharacter")
        self.horizontalLayout_3.addWidget(self.pushButtonDeleteCharacter)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_4.addItem(spacerItem2)
        self.tableViewContent = QtWidgets.QTableView(self.horizontalLayoutWidget_3)
        self.tableViewContent.setSortingEnabled(True)
        self.tableViewContent.setObjectName("tableViewContent")
        self.verticalLayout_4.addWidget(self.tableViewContent)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.listViewSelectedName = QtWidgets.QListView(self.horizontalLayoutWidget_3)
        self.listViewSelectedName.setObjectName("listViewSelectedName")
        self.horizontalLayout_5.addWidget(self.listViewSelectedName)
        self.listViewSelectedValue = QtWidgets.QListView(self.horizontalLayoutWidget_3)
        self.listViewSelectedValue.setObjectName("listViewSelectedValue")
        self.horizontalLayout_5.addWidget(self.listViewSelectedValue)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.pushButtonCommit = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButtonCommit.setObjectName("pushButtonCommit")
        self.verticalLayout_5.addWidget(self.pushButtonCommit)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1413, 21))
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
        self.label.setText(_translate("MainWindow", "Cities"))
        self.pushButtonAddCity.setText(_translate("MainWindow", "Add"))
        self.pushButtonDeleteCity.setText(_translate("MainWindow", "Delete"))
        self.label_2.setText(_translate("MainWindow", "Buildings"))
        self.pushButtonAddBuilding.setText(_translate("MainWindow", "Add"))
        self.pushButtonDeleteBuilding.setText(_translate("MainWindow", "Delete"))
        self.label_3.setText(_translate("MainWindow", "Characters"))
        self.pushButtonAddCharacter.setText(_translate("MainWindow", "Add"))
        self.pushButtonDeleteCharacter.setText(_translate("MainWindow", "Delete"))
        self.pushButtonCommit.setText(_translate("MainWindow", "Commit"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuShow.setTitle(_translate("MainWindow", "Show"))
        self.actionNewDatabase.setText(_translate("MainWindow", "New Database"))
        self.actionLoadDatabase.setText(_translate("MainWindow", "Load Database"))
        self.actionCity_table.setText(_translate("MainWindow", "City table"))
        self.actionBuilding_table.setText(_translate("MainWindow", "Building table"))
        self.actionCharacter_table.setText(_translate("MainWindow", "Character table"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_city_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(418, 453)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 410, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.cultureLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cultureLabel.setFont(font)
        self.cultureLabel.setObjectName("cultureLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.cultureLabel)
        self.cultureComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.cultureComboBox.setObjectName("cultureComboBox")
        self.cultureComboBox.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cultureComboBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.sizeLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sizeLabel.setFont(font)
        self.sizeLabel.setObjectName("sizeLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.sizeLabel)
        self.sizeComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.sizeComboBox.setEditable(False)
        self.sizeComboBox.setObjectName("sizeComboBox")
        self.sizeComboBox.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.sizeComboBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        self.populationLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.populationLabel.setFont(font)
        self.populationLabel.setObjectName("populationLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.populationLabel)
        self.populationLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.populationLineEdit.setObjectName("populationLineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.populationLineEdit)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.geographyButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.geographyButton.setObjectName("geographyButton")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.geographyButton)
        self.verticalLayout.addLayout(self.formLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.forestsCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.forestsCheckBox.setObjectName("forestsCheckBox")
        self.gridLayout.addWidget(self.forestsCheckBox, 0, 0, 1, 1)
        self.riverCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.riverCheckBox.setObjectName("riverCheckBox")
        self.gridLayout.addWidget(self.riverCheckBox, 1, 0, 1, 1)
        self.mountainsCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.mountainsCheckBox.setObjectName("mountainsCheckBox")
        self.gridLayout.addWidget(self.mountainsCheckBox, 2, 0, 1, 1)
        self.seaCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.seaCheckBox.setObjectName("seaCheckBox")
        self.gridLayout.addWidget(self.seaCheckBox, 1, 1, 1, 1)
        self.minesCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.minesCheckBox.setObjectName("minesCheckBox")
        self.gridLayout.addWidget(self.minesCheckBox, 2, 1, 1, 1)
        self.plainsCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.plainsCheckBox.setObjectName("plainsCheckBox")
        self.gridLayout.addWidget(self.plainsCheckBox, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "City"))
        self.nameLabel.setText(_translate("Dialog", "Name :"))
        self.nameLineEdit.setText(_translate("Dialog", "Random"))
        self.cultureLabel.setText(_translate("Dialog", "Culture :"))
        self.cultureComboBox.setItemText(0, _translate("Dialog", "Random"))
        self.sizeLabel.setText(_translate("Dialog", "Size :"))
        self.sizeComboBox.setItemText(0, _translate("Dialog", "Random"))
        self.populationLabel.setText(_translate("Dialog", "Population :"))
        self.populationLineEdit.setText(_translate("Dialog", "Random"))
        self.label_2.setText(_translate("Dialog", "Geography :"))
        self.geographyButton.setText(_translate("Dialog", "Random"))
        self.forestsCheckBox.setText(_translate("Dialog", "Forests"))
        self.riverCheckBox.setText(_translate("Dialog", "River"))
        self.mountainsCheckBox.setText(_translate("Dialog", "Mountains"))
        self.seaCheckBox.setText(_translate("Dialog", "Sea"))
        self.minesCheckBox.setText(_translate("Dialog", "Mines"))
        self.plainsCheckBox.setText(_translate("Dialog", "Plains"))


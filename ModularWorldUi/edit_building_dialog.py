# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_building_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(410, 194)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 361, 151))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.kindLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.kindLabel.setObjectName("kindLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.kindLabel)
        self.kindComboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.kindComboBox.setObjectName("kindComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.kindComboBox)
        self.nameLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.nameLineEdit.setText("")
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.inCityLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.inCityLabel.setObjectName("inCityLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.inCityLabel)
        self.inCityComboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.inCityComboBox.setObjectName("inCityComboBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.inCityComboBox)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.horizontalLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Building (Edit)"))
        self.kindLabel.setText(_translate("Dialog", "Kind :"))
        self.nameLabel.setText(_translate("Dialog", "Name :"))
        self.inCityLabel.setText(_translate("Dialog", "In city :"))


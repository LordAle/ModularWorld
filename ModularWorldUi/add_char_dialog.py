# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_char_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 388)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 451, 359))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.nameLabel_2 = QtWidgets.QLabel(self.layoutWidget)
        self.nameLabel_2.setObjectName("nameLabel_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel_2)
        self.coreNameLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.coreNameLineEdit.setObjectName("coreNameLineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.coreNameLineEdit)
        self.familyNameLabel = QtWidgets.QLabel(self.layoutWidget)
        self.familyNameLabel.setObjectName("familyNameLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.familyNameLabel)
        self.familyNameLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.familyNameLineEdit.setObjectName("familyNameLineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.familyNameLineEdit)
        self.cultureLabel = QtWidgets.QLabel(self.layoutWidget)
        self.cultureLabel.setObjectName("cultureLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.cultureLabel)
        self.cultureComboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.cultureComboBox.setObjectName("cultureComboBox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cultureComboBox)
        self.raceLabel = QtWidgets.QLabel(self.layoutWidget)
        self.raceLabel.setObjectName("raceLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.raceLabel)
        self.raceComboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.raceComboBox.setObjectName("raceComboBox")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.raceComboBox)
        self.genderLabel = QtWidgets.QLabel(self.layoutWidget)
        self.genderLabel.setObjectName("genderLabel")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.genderLabel)
        self.genderComboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.genderComboBox.setObjectName("genderComboBox")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.genderComboBox)
        self.ageLabel = QtWidgets.QLabel(self.layoutWidget)
        self.ageLabel.setObjectName("ageLabel")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.ageLabel)
        self.ageLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.ageLineEdit.setObjectName("ageLineEdit")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.ageLineEdit)
        self.socialGroupLabel = QtWidgets.QLabel(self.layoutWidget)
        self.socialGroupLabel.setObjectName("socialGroupLabel")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.socialGroupLabel)
        self.socialGroupComboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.socialGroupComboBox.setObjectName("socialGroupComboBox")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.socialGroupComboBox)
        self.professionLabel = QtWidgets.QLabel(self.layoutWidget)
        self.professionLabel.setObjectName("professionLabel")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.professionLabel)
        self.professionComboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.professionComboBox.setObjectName("professionComboBox")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.professionComboBox)
        self.familyRoleLabel = QtWidgets.QLabel(self.layoutWidget)
        self.familyRoleLabel.setObjectName("familyRoleLabel")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.familyRoleLabel)
        self.familyRoleComboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.familyRoleComboBox.setObjectName("familyRoleComboBox")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.familyRoleComboBox)
        self.wealthLabel = QtWidgets.QLabel(self.layoutWidget)
        self.wealthLabel.setObjectName("wealthLabel")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.wealthLabel)
        self.wealthLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.wealthLineEdit.setObjectName("wealthLineEdit")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.wealthLineEdit)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Character"))
        self.nameLabel_2.setText(_translate("Dialog", "Name :"))
        self.coreNameLineEdit.setText(_translate("Dialog", "Random"))
        self.familyNameLabel.setText(_translate("Dialog", "Family Name :"))
        self.familyNameLineEdit.setText(_translate("Dialog", "Random"))
        self.cultureLabel.setText(_translate("Dialog", "Culture : "))
        self.raceLabel.setText(_translate("Dialog", "Race :"))
        self.genderLabel.setText(_translate("Dialog", "Gender :"))
        self.ageLabel.setText(_translate("Dialog", "Age :"))
        self.ageLineEdit.setText(_translate("Dialog", "Random"))
        self.socialGroupLabel.setText(_translate("Dialog", "Social Group"))
        self.professionLabel.setText(_translate("Dialog", "Profession :"))
        self.familyRoleLabel.setText(_translate("Dialog", "Family Role"))
        self.wealthLabel.setText(_translate("Dialog", "Wealth : "))
        self.wealthLineEdit.setText(_translate("Dialog", "Random"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_building_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1113, 718)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 40, 861, 414))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
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
        self.kindComboBox.addItem("")
        self.kindComboBox.addItem("")
        self.kindComboBox.addItem("")
        self.kindComboBox.addItem("")
        self.kindComboBox.addItem("")
        self.kindComboBox.addItem("")
        self.kindComboBox.addItem("")
        self.kindComboBox.addItem("")
        self.kindComboBox.addItem("")
        self.kindComboBox.addItem("")
        self.kindComboBox.addItem("")
        self.kindComboBox.addItem("")
        self.kindComboBox.addItem("")
        self.kindComboBox.addItem("")
        self.kindComboBox.addItem("")
        self.kindComboBox.addItem("")
        self.kindComboBox.addItem("")
        self.kindComboBox.addItem("")
        self.kindComboBox.addItem("")
        self.kindComboBox.addItem("")
        self.kindComboBox.addItem("")
        self.kindComboBox.addItem("")
        self.kindComboBox.addItem("")
        self.kindComboBox.addItem("")
        self.kindComboBox.addItem("")
        self.kindComboBox.addItem("")
        self.kindComboBox.addItem("")
        self.kindComboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.kindComboBox)
        self.nameLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.autoPopulateLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.autoPopulateLabel.setObjectName("autoPopulateLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.autoPopulateLabel)
        self.autoPopulateCheckBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.autoPopulateCheckBox.setChecked(True)
        self.autoPopulateCheckBox.setObjectName("autoPopulateCheckBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.autoPopulateCheckBox)
        self.subkindLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.subkindLabel.setObjectName("subkindLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.subkindLabel)
        self.subkindComboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.subkindComboBox.setObjectName("subkindComboBox")
        self.subkindComboBox.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.subkindComboBox)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.horizontalLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.nameLabel_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.nameLabel_2.setObjectName("nameLabel_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel_2)
        self.coreNameLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.coreNameLineEdit.setObjectName("coreNameLineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.coreNameLineEdit)
        self.familyNameLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.familyNameLabel.setObjectName("familyNameLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.familyNameLabel)
        self.familyNameLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.familyNameLineEdit.setObjectName("familyNameLineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.familyNameLineEdit)
        self.raceLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.raceLabel.setObjectName("raceLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.raceLabel)
        self.raceComboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.raceComboBox.setObjectName("raceComboBox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.raceComboBox)
        self.genderLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.genderLabel.setObjectName("genderLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.genderLabel)
        self.genderComboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.genderComboBox.setObjectName("genderComboBox")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.genderComboBox)
        self.ageLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.ageLabel.setObjectName("ageLabel")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.ageLabel)
        self.roleLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.roleLabel.setObjectName("roleLabel")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.roleLabel)
        self.professionLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.professionLabel.setObjectName("professionLabel")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.professionLabel)
        self.professionComboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.professionComboBox.setObjectName("professionComboBox")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.professionComboBox)
        self.classLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.classLabel.setObjectName("classLabel")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.classLabel)
        self.classComboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.classComboBox.setObjectName("classComboBox")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.classComboBox)
        self.levelLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.levelLabel.setObjectName("levelLabel")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.levelLabel)
        self.levelLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.levelLineEdit.setObjectName("levelLineEdit")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.levelLineEdit)
        self.ageLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.ageLineEdit.setObjectName("ageLineEdit")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.ageLineEdit)
        self.wealthLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.wealthLabel.setObjectName("wealthLabel")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.wealthLabel)
        self.wealthComboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.wealthComboBox.setObjectName("wealthComboBox")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.wealthComboBox)
        self.roleLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.roleLineEdit.setReadOnly(True)
        self.roleLineEdit.setObjectName("roleLineEdit")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.roleLineEdit)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Building"))
        self.kindLabel.setText(_translate("Dialog", "Kind :"))
        self.kindComboBox.setItemText(0, _translate("Dialog", "Random"))
        self.kindComboBox.setItemText(1, _translate("Dialog", "House (Noble)"))
        self.kindComboBox.setItemText(2, _translate("Dialog", "House (Bourgeois)"))
        self.kindComboBox.setItemText(3, _translate("Dialog", "House (Commoner)"))
        self.kindComboBox.setItemText(4, _translate("Dialog", "House (Farmer)"))
        self.kindComboBox.setItemText(5, _translate("Dialog", "Shop (General)"))
        self.kindComboBox.setItemText(6, _translate("Dialog", "Shop (Food)"))
        self.kindComboBox.setItemText(7, _translate("Dialog", "Shop (Health)"))
        self.kindComboBox.setItemText(8, _translate("Dialog", "Shop (Book)"))
        self.kindComboBox.setItemText(9, _translate("Dialog", "Shop (Magic)"))
        self.kindComboBox.setItemText(10, _translate("Dialog", "Shop (Luxery)"))
        self.kindComboBox.setItemText(11, _translate("Dialog", "Shop (Ressource)"))
        self.kindComboBox.setItemText(12, _translate("Dialog", "Workshop (Blacksmith)"))
        self.kindComboBox.setItemText(13, _translate("Dialog", "Workshop (Tailor)"))
        self.kindComboBox.setItemText(14, _translate("Dialog", "Workshop (Leatherwork)"))
        self.kindComboBox.setItemText(15, _translate("Dialog", "Workshop (Woodwork)"))
        self.kindComboBox.setItemText(16, _translate("Dialog", "Workshop (Other)"))
        self.kindComboBox.setItemText(17, _translate("Dialog", "Castle (Keep)"))
        self.kindComboBox.setItemText(18, _translate("Dialog", "Castle (Castle)"))
        self.kindComboBox.setItemText(19, _translate("Dialog", "Religious (Shrine)"))
        self.kindComboBox.setItemText(20, _translate("Dialog", "Religious (Monastery)"))
        self.kindComboBox.setItemText(21, _translate("Dialog", "Religious (Church)"))
        self.kindComboBox.setItemText(22, _translate("Dialog", "Religious (Cathedral)"))
        self.kindComboBox.setItemText(23, _translate("Dialog", "Education (School)"))
        self.kindComboBox.setItemText(24, _translate("Dialog", "Education (University)"))
        self.kindComboBox.setItemText(25, _translate("Dialog", "Military (Barrack)"))
        self.kindComboBox.setItemText(26, _translate("Dialog", "Military (Prison)"))
        self.kindComboBox.setItemText(27, _translate("Dialog", "Military (Fortress)"))
        self.nameLabel.setText(_translate("Dialog", "Name :"))
        self.nameLineEdit.setText(_translate("Dialog", "Random"))
        self.autoPopulateLabel.setText(_translate("Dialog", "Auto populate"))
        self.subkindLabel.setText(_translate("Dialog", "Subkind"))
        self.subkindComboBox.setItemText(0, _translate("Dialog", "Random"))
        self.label_2.setText(_translate("Dialog", "Core member"))
        self.nameLabel_2.setText(_translate("Dialog", "Name :"))
        self.coreNameLineEdit.setText(_translate("Dialog", "Random"))
        self.familyNameLabel.setText(_translate("Dialog", "Family Name :"))
        self.familyNameLineEdit.setText(_translate("Dialog", "Random"))
        self.raceLabel.setText(_translate("Dialog", "Race :"))
        self.genderLabel.setText(_translate("Dialog", "Gender :"))
        self.ageLabel.setText(_translate("Dialog", "Age :"))
        self.roleLabel.setText(_translate("Dialog", "Role :"))
        self.professionLabel.setText(_translate("Dialog", "Profession :"))
        self.classLabel.setText(_translate("Dialog", "Class :"))
        self.levelLabel.setText(_translate("Dialog", "Level :"))
        self.levelLineEdit.setText(_translate("Dialog", "Random"))
        self.ageLineEdit.setText(_translate("Dialog", "Random"))
        self.wealthLabel.setText(_translate("Dialog", "Wealth :"))
        self.roleLineEdit.setText(_translate("Dialog", "Master"))


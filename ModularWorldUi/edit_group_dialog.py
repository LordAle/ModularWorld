# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_group_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(463, 259)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(110, 220, 311, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 421, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.familyLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.familyLabel.setObjectName("familyLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.familyLabel)
        self.familyCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.familyCheckBox.setObjectName("familyCheckBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.familyCheckBox)
        self.liveLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.liveLabel.setObjectName("liveLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.liveLabel)
        self.liveCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.liveCheckBox.setObjectName("liveCheckBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.liveCheckBox)
        self.workLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.workLabel.setObjectName("workLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.workLabel)
        self.workCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.workCheckBox.setObjectName("workCheckBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.workCheckBox)
        self.visitLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.visitLabel.setObjectName("visitLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.visitLabel)
        self.visitCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.visitCheckBox.setObjectName("visitCheckBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.visitCheckBox)
        self.inBuildingLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.inBuildingLabel.setObjectName("inBuildingLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.inBuildingLabel)
        self.inBuildingComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.inBuildingComboBox.setObjectName("inBuildingComboBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.inBuildingComboBox)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Group (Edit)"))
        self.nameLabel.setText(_translate("Dialog", "Name :"))
        self.familyLabel.setText(_translate("Dialog", "Family :"))
        self.liveLabel.setText(_translate("Dialog", "Live :"))
        self.workLabel.setText(_translate("Dialog", "Work :"))
        self.visitLabel.setText(_translate("Dialog", "Visit"))
        self.inBuildingLabel.setText(_translate("Dialog", "In building :"))


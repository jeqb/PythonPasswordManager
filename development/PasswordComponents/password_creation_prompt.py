# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'password_creation_prompt.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_password_creation(object):
    def setupUi(self, password_creation):
        password_creation.setObjectName("password_creation")
        password_creation.resize(282, 255)
        self.label_one = QtWidgets.QLabel(password_creation)
        self.label_one.setGeometry(QtCore.QRect(20, 10, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_one.setFont(font)
        self.label_one.setAlignment(QtCore.Qt.AlignCenter)
        self.label_one.setObjectName("label_one")
        self.password_field = QtWidgets.QLineEdit(password_creation)
        self.password_field.setGeometry(QtCore.QRect(30, 70, 221, 20))
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_field.setObjectName("password_field")
        self.submit_button = QtWidgets.QPushButton(password_creation)
        self.submit_button.setGeometry(QtCore.QRect(150, 190, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.submit_button.setFont(font)
        self.submit_button.setObjectName("submit_button")
        self.cancel_button = QtWidgets.QPushButton(password_creation)
        self.cancel_button.setGeometry(QtCore.QRect(30, 190, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_button.setFont(font)
        self.cancel_button.setObjectName("cancel_button")
        self.label_two = QtWidgets.QLabel(password_creation)
        self.label_two.setGeometry(QtCore.QRect(20, 90, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_two.setFont(font)
        self.label_two.setAlignment(QtCore.Qt.AlignCenter)
        self.label_two.setObjectName("label_two")
        self.password_field_2 = QtWidgets.QLineEdit(password_creation)
        self.password_field_2.setGeometry(QtCore.QRect(30, 150, 221, 20))
        self.password_field_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_field_2.setObjectName("password_field_2")

        self.retranslateUi(password_creation)
        QtCore.QMetaObject.connectSlotsByName(password_creation)

    def retranslateUi(self, password_creation):
        _translate = QtCore.QCoreApplication.translate
        password_creation.setWindowTitle(_translate("password_creation", "Form"))
        self.label_one.setText(_translate("password_creation", "Type Master Password"))
        self.submit_button.setText(_translate("password_creation", "Submit"))
        self.cancel_button.setText(_translate("password_creation", "Cancel"))
        self.label_two.setText(_translate("password_creation", "Retype Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    password_creation = QtWidgets.QWidget()
    ui = Ui_password_creation()
    ui.setupUi(password_creation)
    password_creation.show()
    sys.exit(app.exec_())

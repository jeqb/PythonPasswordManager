import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class ManagerWindow(QtWidgets.QMainWindow):


    def __init__(self):
        super().__init__()

        # Load settings and initialize API
        

        # window settings
        self.title = "Python Password Manager"
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 800
        self.icon_name = "PythonIcon.png"

        # set characteristics about the window
        self.setWindowIcon(QtGui.QIcon(self.icon_name))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # create ui components
        self.call_ui_components()

        # maximals maximize!
        self.show()


    def call_ui_components(self):
        self.create_password_prompt_container()


    def create_password_prompt_container(self):
        # make the QGroupBox
        PasswordPromptContainer = QtWidgets.QGroupBox(self)
        PasswordPromptContainer.setGeometry(QtCore.QRect(270, 110, 251, 191))
        PasswordPromptContainer.setTitle("")
        PasswordPromptContainer.setObjectName("PasswordPromptContainer")

        # make the QPushButton
        SubmitPassword = QtWidgets.QPushButton(PasswordPromptContainer)
        SubmitPassword.setGeometry(QtCore.QRect(60, 120, 131, 51))
        SubmitPassword.setObjectName("SubmitPassword")
        SubmitPassword.setText("Submit")
        SubmitPassword.clicked.connect(self.submit_password)

        #  make the password entry field
        PasswordField = QtWidgets.QTextEdit(PasswordPromptContainer)
        PasswordField.setGeometry(QtCore.QRect(10, 60, 231, 31))
        PasswordField.setObjectName("PasswordField")

        # make the password label
        PasswordMessage = QtWidgets.QLabel(PasswordPromptContainer)
        PasswordMessage.setGeometry(QtCore.QRect(60, 20, 111, 21))
        PasswordMessage.setObjectName("PasswordMessage")
        PasswordMessage.setText(" Entry your password")

        # give the main window access to all the items
        self.PasswordPromptContainer = PasswordPromptContainer
        self.SubmitPassword = SubmitPassword
        self.PasswordField = PasswordField
        self.PasswordMessage = PasswordMessage


    def submit_password(self):
        value = self.PasswordField.toPlainText()

        print(value)

        self.delete_password_prompt_container()


    def delete_password_prompt_container(self):
        self.PasswordPromptContainer.deleteLater()
import sys
import os
from pathlib import Path
from PyQt5 import QtWidgets, QtGui, QtCore


class ManagerWindow(QtWidgets.QMainWindow):


    def __init__(self, settings, Api):
        super().__init__()

        self.settings = settings
        self.ApiClass = Api


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
        # self.create_database_prompt_container()


    def create_database_routine(self):
        """
        1. Check if there is a database directory
            if no directory in settings:
                1. tell user to select directory
                2. create database with tables
        2. connect to database and create tables
        3. add database directory to settings
        4. export settings to json file
        """

        # 1.
        yield self.get_database_path_prompt_container()

        # 2.

        # 3.

        # 4.
        cwd = os.getcwd()
        cwd = Path(cwd)
        settings_file = cwd / 'password_manager_settings.json'
        self.settings.export_settings_to_json(settings_file)
        print('exported settings.json')


    def get_database_path_prompt_container(self):
        # make the QGroupBox
        DatabasePromptContainer = QtWidgets.QGroupBox(self)
        DatabasePromptContainer.setGeometry(QtCore.QRect(270, 110, 251, 191))
        DatabasePromptContainer.setTitle("")
        DatabasePromptContainer.setObjectName("Select Database Folder")

        # make the password label
        DatabaseMessage = QtWidgets.QLabel(DatabasePromptContainer)
        DatabaseMessage.setGeometry(QtCore.QRect(60, 53, 111, 53))
        DatabaseMessage.setObjectName("DatabaseMessage")
        DatabaseMessage.setText(" No Database exists.")
        DatabaseMessage2 = QtWidgets.QLabel(DatabasePromptContainer)
        DatabaseMessage2.setGeometry(QtCore.QRect(60, 70, 111, 53))
        DatabaseMessage2.setObjectName("DatabaseMessage")
        DatabaseMessage2.setText("Choose a directory")

        # make the QPushButton
        OpenBrowser = QtWidgets.QPushButton(DatabasePromptContainer)
        OpenBrowser.setGeometry(QtCore.QRect(60, 120, 131, 51))
        OpenBrowser.setObjectName("OpenFileBrowser")
        OpenBrowser.setText("Open File Browser")
        OpenBrowser.clicked.connect(self.set_database_directory)

        # give the main window access to all the items
        self.DatabasePromptContainer = DatabasePromptContainer


    def set_database_directory(self):
        """
        Call this to create a Folder browser, get the directory from the browser
        and then set the self.settings.database_file_path to that directory
        """

        database_directory = self.create_folder_browser()
        database_directory = database_directory + '/password_database.db'
        database_directory = Path(database_directory)

        self.settings.database_file_path = str(database_directory)


    def delete_database_prompt_container(self):
        self.DatabasePromptContainer.deleteLater()


    def create_password_prompt_container(self):
        """ This is the prompt used to create the database password """

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
        """
        used in conjunction with create_password_prompt_container() to register
        the password entered by user.
        """
        value = self.PasswordField.toPlainText()

        print(value)

        self.delete_password_prompt_container()


    def delete_password_prompt_container(self):
        """ Makes the password prompt go away """
        self.PasswordPromptContainer.deleteLater()


    def create_file_browser(self):
        """
        Creates the file browser to do stuff with.
        """
        FileBrowser = QtWidgets.QFileDialog()
        file_path = FileBrowser.getOpenFileName(self, 'Select File')
        return file_path


    def create_folder_browser(self):
        """ Create the browser to select a file directory """
        FolderBrowser = QtWidgets.QFileDialog()
        directory = FolderBrowser.getExistingDirectory(self, 'Select a folder')
        return directory
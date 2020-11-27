from PyQt5 import QtWidgets, QtCore

from .password_prompt import Ui_password_prompt

# class PasswordPrompt(QtWidgets.QWidget):
class PasswordPrompt(QtWidgets.QFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_password_prompt()
        self.ui.setupUi(self)

        # connections
        self.ui.submit_button.clicked.connect(self.authenticate)
        self.ui.cancel_button.clicked.connect(self.quit)

    def authenticate(self):
        password = self.ui.password_field.text()

        if password == 'password':
            QtWidgets.QMessageBox.information(self, 'Success', 'You have logged in')
        else:
            QtWidgets.QMessageBox.critical(self, 'Fail', 'You have failed to log in')

    def quit(self):
        exit()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    widget = PasswordPrompt()
    widget.show()

    app.exec_()
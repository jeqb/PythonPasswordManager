from PyQt5 import QtWidgets, QtCore

from .password_creation_prompt import Ui_password_creation

class PasswordCreationPrompt(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_password_creation()
        self.ui.setupUi(self)

        # connections
        self.ui.submit_button.clicked.connect(self.validate)
        self.ui.cancel_button.clicked.connect(self.close)

    def validate(self):
        password_one = self.ui.password_field.text()
        password_two = self.ui.password_field_2.text()

        if password_one != password_two:
            QtWidgets.QMessageBox.critical(self, 'Fail', 'Your passwords do not match.')
        else:
            QtWidgets.QMessageBox.information(self, 'Success', 'Master Password Created')
            self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    widget = PasswordCreationPrompt()
    widget.show()

    app.exec_()
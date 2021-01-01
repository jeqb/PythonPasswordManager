from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

from .Actions import submit, cancel

class PasswordPromptWindow(QDialog):
    def __init__(self, parent_widget):
        super().__init__()

        self.parent_widget = parent_widget

        self.setWindowTitle("Enter Password")
        self.setWindowIcon(QIcon('PythonPasswordManager/icons/PythonIcon.png'))
        self.setGeometry(450,150,450,200)
        self.setFixedSize(self.size())

        self.create_ui()
        
        self.show()

    def create_ui(self):
        # make the form layout
        form_layout = QFormLayout()
        form_layout.setFormAlignment(Qt.AlignHCenter| Qt.AlignCenter)
        # make horizontal layout
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addStretch()

        # Enter Password Label
        password_label = QLabel("Enter Password")

        # Password Field
        self.password_field = QLineEdit()
        self.password_field.setEchoMode(QLineEdit.Password)

        # submit button
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(lambda: submit(self))

        # cancel button
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(lambda: cancel(self))

        # align the buttons horizontally
        horizontal_layout.addStretch()
        horizontal_layout.addWidget(submit_button)
        horizontal_layout.addWidget(cancel_button)

        # add everything to the main form
        form_layout.addRow(password_label)
        form_layout.addRow(self.password_field)
        form_layout.addRow(horizontal_layout)

        self.setLayout(form_layout)
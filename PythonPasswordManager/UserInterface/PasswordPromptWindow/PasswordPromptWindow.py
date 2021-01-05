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
        self.setGeometry(450,100,300,100)
        self.setFixedSize(self.size())
        self.move(900, 350)

        self.create_ui()
        
        self.show()

    def create_ui(self):
        # make the form layout
        form_layout = QFormLayout()
        form_layout.setFormAlignment(Qt.AlignHCenter| Qt.AlignCenter)
        # make horizontal layout
        horizontal_layout_one = QHBoxLayout()
        horizontal_layout_one.addStretch()
        horizontal_layout_two = QHBoxLayout()
        horizontal_layout_two.addStretch()

        # Enter Password Label
        password_label = QLabel("Enter Password")
        horizontal_layout_one.addWidget(password_label)
        horizontal_layout_one.addStretch()

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
        horizontal_layout_two.addWidget(submit_button)
        horizontal_layout_two.addWidget(cancel_button)
        horizontal_layout_two.addStretch()

        # add everything to the main form
        form_layout.addRow(horizontal_layout_one)
        form_layout.addRow(self.password_field)
        form_layout.addRow(horizontal_layout_two)

        self.setLayout(form_layout)
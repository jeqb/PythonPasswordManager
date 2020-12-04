from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

from .Actions import submit, cancel

class CreatePasswordWindow(QDialog):
    """
    Prompt to create a password. This will also verify that it
    is somewhat secure
    """
    def __init__(self, parent_widget):
        # "None, Qt.WindowCloseButtonHint" removes question mark
        super().__init__(None, Qt.WindowCloseButtonHint)
        # removes close button
        # self.setWindowFlag(Qt.WindowCloseButtonHint, False)

        self.setWindowTitle("Create Password")
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

        # Create Password Label
        password_label = QLabel("Create Password")

        # Password Field
        password_field = QLineEdit()

        # strength indicator label
        strength_indicator = QLabel("Strength")
        strength_label = QLabel("")

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
        form_layout.addRow(password_field)
        form_layout.addRow(strength_indicator)
        form_layout.addRow(strength_label)
        form_layout.addRow(horizontal_layout)

        self.setLayout(form_layout)
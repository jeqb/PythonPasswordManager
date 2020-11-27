import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PIL import Image

from .Actions import cancel, add_note

class AddNoteWindow(QWidget):
    def __init__(self, api):
        super().__init__()

        # database connection
        self.api = api

        self.setWindowTitle("Add Note")
        self.setWindowIcon(QIcon('PythonPasswordManager/icons/PythonIcon.png'))
        self.setGeometry(450,150,350,550)
        self.setFixedSize(self.size())

        self.create_ui()
        self.show()

    def create_ui(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        # Top Layout Widgets
        self.add_note_img=QLabel()
        self.img=QPixmap('PythonPasswordManager/icons/addproduct.png')
        self.add_note_img.setPixmap(self.img)
        self.add_note_img.setAlignment(Qt.AlignCenter)
        self.titleText=QLabel("Add Product")
        self.titleText.setAlignment(Qt.AlignCenter)

        # Bottom Layout Widgets
        self.note_entry=QLineEdit()
        self.note_entry.setPlaceholderText("Enter Note Content")
        self.cancel_button=QPushButton("Cancel")
        self.cancel_button.clicked.connect(lambda: cancel(self))
        self.submit_button=QPushButton("Submit")
        self.submit_button.clicked.connect(lambda: add_note(self))

    def layouts(self):
        # create layouts
        self.main_layout=QVBoxLayout()
        self.top_layout=QVBoxLayout()
        self.bottom_layout=QFormLayout()
        self.top_frame=QFrame()
        self.bottom_frame=QFrame()
        
        # add top_layout widgets
        self.top_layout.addWidget(self.titleText)
        self.top_layout.addWidget(self.add_note_img)
        self.top_frame.setLayout(self.top_layout)
        
        # add bottom_layout widgets
        self.bottom_layout.addRow(QLabel("Content: "), self.note_entry)
        self.bottom_layout.addRow(QLabel(""), self.submit_button)
        self.bottom_frame.setLayout(self.bottom_layout)

        # attach everyone
        self.main_layout.addWidget(self.top_frame)
        self.main_layout.addWidget(self.bottom_frame)
        self.setLayout(self.main_layout)
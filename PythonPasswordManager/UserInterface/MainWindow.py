import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

from .actions import get_notes, create_password, create_note, select_password


class MainWindow(QMainWindow):
    def __init__(self, api, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # database connection
        self.api = api

        self.setWindowTitle("Python Password Manager")
        self.setWindowIcon(QIcon('PythonPasswordManager/icons/PythonIcon.png'))
        self.setGeometry(450,150,1350,750)
        self.setFixedSize(self.size())
        
        self.create_ui()

        self.show()

    def create_ui(self):
        """
        This method calls all other methods used to add things to the UI.
        """
        self.tool_bar()
        self.tab_widget()
        self.widgets()
        self.layouts()
        get_notes(self)

    def tab_changed(self):
        get_notes(self)

    def tool_bar(self):
        """
        Creates the Tool Bar at the top of the screen
        """
        # create ToolBar
        self.tool_bar=self.addToolBar("Tool Bar")
        self.tool_bar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        # Add Password Button
        self.add_password_button=QAction(QIcon('PythonPasswordManager/icons/add.png'),"Add Password",self)
        self.tool_bar.addAction(self.add_password_button)
        self.add_password_button.triggered.connect(lambda: create_password(self))
        self.tool_bar.addSeparator()

        # Add Note Button
        self.add_note_button=QAction(QIcon('PythonPasswordManager/icons/users.png'),"Add Note",self)
        self.tool_bar.addAction(self.add_note_button)
        self.add_note_button.triggered.connect(lambda: create_note(self))
        self.tool_bar.addSeparator()

    def tab_widget(self):
        """
        Creates a blank canvas with 2 tabs.
        """
        # create main tab
        self.tabs=QTabWidget()
        self.tabs.blockSignals(True)
        # TODO: flesh out method
        self.tabs.currentChanged.connect(self.tab_changed)
        self.setCentralWidget(self.tabs)

        # create individual tabs
        self.password_tab=QWidget()
        self.note_tab=QWidget()
        self.tabs.addTab(self.password_tab,"Password")
        self.tabs.addTab(self.note_tab,"Notes")

    def widgets(self):
        # tab_one widget
        # main left layout widget
        self.password_table = QTableWidget()
        self.password_table.setColumnCount(7)
        self.password_table.setColumnHidden(0,True)
        self.password_table.setHorizontalHeaderItem(0,QTableWidgetItem("Password Id"))
        self.password_table.setHorizontalHeaderItem(1,QTableWidgetItem("Website"))
        self.password_table.setHorizontalHeaderItem(2,QTableWidgetItem("Username"))
        self.password_table.setHorizontalHeaderItem(3,QTableWidgetItem("Email"))
        self.password_table.setHorizontalHeaderItem(4,QTableWidgetItem("Password"))
        self.password_table.setHorizontalHeaderItem(5,QTableWidgetItem("Category"))
        self.password_table.setHorizontalHeaderItem(6,QTableWidgetItem("Note"))
        self.password_table.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        self.password_table.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)
        # add behavior
        self.password_table.doubleClicked.connect(lambda: select_password(self))


        # Right top layout widget
        self.search_text=QLabel("Search")
        self.search_entry=QLineEdit()
        self.search_entry.setPlaceholderText("Search by Website")
        self.search_button=QPushButton("Search")
        # TODO: flesh out method
        # self.searchButton.clicked.connect(self.searchProducts)
        # TODO: flesh out style sheet
        # self.searchButton.setStyleSheet(style.searchButtonStyle())

        # right middle layout widgets
        # TODO: Repurpose this to filter by categor.
        # TODO: It can search the database for distict categories and dynamically render here?
        self.allProducts=QRadioButton("All Products")
        self.avaialableProducts=QRadioButton("Available")
        self.notAvaialableProducts=QRadioButton("Not Available")
        self.listButton=QPushButton("List")
        # TODO: flesh out method
        # self.listButton.clicked.connect(self.listProducts)
        # TODO: flesh out style sheet
        # self.listButton.setStyleSheet(style.listButtonStyle())


        # tab_two widgets
        self.note_table=QTableWidget()
        self.note_table.setColumnCount(2)
        self.note_table.setHorizontalHeaderItem(0,QTableWidgetItem("Id"))
        self.note_table.setHorizontalHeaderItem(1,QTableWidgetItem("Content"))
        self.note_table.horizontalHeader().setSectionResizeMode(0,QHeaderView.Stretch)
        self.note_table.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        # TODO: flesh out method
        # self.membersTable.doubleClicked.connect(self.selectedMember)
        self.note_search_text=QLabel("Search")
        self.note_search_entry=QLineEdit()
        self.note_search_entry.setPlaceholderText("Search by Content")
        self.note_search_button=QPushButton("Search")
        # TODO: flesh out method
        # self.memberSearchButton.clicked.connect(self.searchMembers)

    def layouts(self):
        # tab 1 layous
        self.main_layout=QHBoxLayout()
        self.main_left_layout=QVBoxLayout()
        self.main_right_layout=QVBoxLayout()
        self.right_top_layout=QHBoxLayout()
        self.right_middle_layout=QHBoxLayout()
        self.top_group_box=QGroupBox("Search Box")
        # TODO: flesh out style sheet
        # self.topGroupBox.setStyleSheet(style.searchBoxStyle())
        self.middle_group_box=QGroupBox("List Box")
        # TODO: flesh out style sheet
        # self.middleGroupBox.setStyleSheet(style.listBoxStyle())
        self.bottom_group_box=QGroupBox()

        # Add widgets
        # main left layout widget
        self.main_left_layout.addWidget(self.password_table)

        # right top layout widget
        self.right_top_layout.addWidget(self.search_text)
        self.right_top_layout.addWidget(self.search_entry)
        self.right_top_layout.addWidget(self.search_button)
        self.top_group_box.setLayout(self.right_top_layout)

        # right middle layout widget
        self.right_middle_layout.addWidget(self.allProducts)
        self.right_middle_layout.addWidget(self.avaialableProducts)
        self.right_middle_layout.addWidget(self.notAvaialableProducts)
        self.right_middle_layout.addWidget(self.listButton)
        self.middle_group_box.setLayout(self.right_middle_layout)

        self.main_right_layout.addWidget(self.top_group_box,20)
        self.main_right_layout.addWidget(self.middle_group_box,20)
        self.main_right_layout.addWidget(self.bottom_group_box,60)
        self.main_layout.addLayout(self.main_left_layout,70)
        self.main_layout.addLayout(self.main_right_layout,30)
        self.password_tab.setLayout(self.main_layout)
        
        # tab 2 layouts
        self.note_main_layout=QHBoxLayout()
        self.note_left_layout=QHBoxLayout()
        self.note_right_layout=QHBoxLayout()
        self.note_right_groupbox=QGroupBox("Search For Notes")
        self.note_right_groupbox.setContentsMargins(10,10,10,600)
        self.note_right_layout.addWidget(self.note_search_text)
        self.note_right_layout.addWidget(self.note_search_entry)
        self.note_right_layout.addWidget(self.note_search_button)
        self.note_right_groupbox.setLayout(self.note_right_layout)

        self.note_left_layout.addWidget(self.note_table)
        self.note_main_layout.addLayout(self.note_left_layout,70)
        self.note_main_layout.addWidget(self.note_right_groupbox,30)
        self.note_tab.setLayout(self.note_main_layout)
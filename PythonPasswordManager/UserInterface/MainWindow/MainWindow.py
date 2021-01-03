import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

from Api import Api
from Storage import Base, create_tables, create_database_engine
from Security import PasswordTools
from Common.Constants import SETTINGS_FILE_NAME, DECRYPTED_DATABASE_NAME, ENCRYPTED_DATABASE_NAME
from Common.Exceptions import InvalidPasswordException
from Common.Enums import Category

from .Actions import (
    get_notes, create_password, create_note, select_password,
    select_note, delete_password, delete_note,
    search_note_by_content, check_if_blank, get_passwords, update_password,
    clear_radio_buttons
)

from ..CreatePasswordWindow import CreatePasswordWindow
from ..PasswordPromptWindow import PasswordPromptWindow

class MainWindow(QMainWindow):
    """
    Main UI for the application.

    NEW startup routine:
        1. Does it have both a database path and a salt?
            if either is missing, need to create
                brand new for both and save to settings.
                For database, make prompt pop up.
                Then ask user for new password.
                Lastly, instantiate Api class and
                    encrypt database.
        
        2. If both exist:
            2.1 prompt for password
            2.2. attempt decryption
                    if decryption fails:
                        tell them & reprompt

        3. start main ui (I think that's about it)
    """
    def __init__(self, settings, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # applicaiton settings
        self.settings = settings

        # deliberate. for the startup routine
        self.api = None

        # used by the AddNoteWindow and AddPasswordWindow
        self.edit_note_mode = False
        self.edit_password_mode = False

        # window properties and dimensions
        self.setWindowTitle("Python Password Manager")
        self.setWindowIcon(QIcon('PythonPasswordManager/icons/PythonIcon.png'))
        self.setGeometry(450,150,1350,750)
        self.setFixedSize(self.size())
        # show a blank window to signify the application has started.
        self.show()



        # startup routine
        # 1.
        # check that settings has the required properties and not empty or invalid path
        # if the settings are not valid, create a new database.
        if not hasattr(self.settings, 'database_folder_path') or \
            self.settings.database_folder_path is None or \
            self.settings.database_folder_path == '' or \
            not os.path.exists(self.settings.database_folder_path) or \
            not os.path.exists(self.settings.database_folder_path + '/' + ENCRYPTED_DATABASE_NAME):

            # prompt for database path
            valid_dir = False
            while not valid_dir:
                db_dir = QFileDialog.getExistingDirectory(self,
                    "Choose Database Directory")
                
                valid_dir = os.path.exists(db_dir)

                if not valid_dir:
                    continue
                else:
                    self.settings.database_folder_path = db_dir

                    self.settings.export_settings_to_json(SETTINGS_FILE_NAME)

            # create the missing database after a valid_dir is chosen and saved
            engine = create_database_engine(
                db_directory=self.settings.database_folder_path + '/' + DECRYPTED_DATABASE_NAME
                )
            create_tables(Base, engine)


            # prompt password
            self.password_prompt = PasswordPromptWindow(self)
            self.password_prompt.exec_()
            # password = self.password_submission
            # TODO: validate password strength

            # encrypt new database
            self.api = Api(
                database_folder_path=self.settings.database_folder_path,
                password_string=self.password_submission
                )

            self.api.encrypt_database()


        successful_decryption=False
        while not successful_decryption:
            # 2.
            # prompt password if have not already
            self.password_prompt = PasswordPromptWindow(self)
            self.password_prompt.exec_()
            # password = self.password_submission
            # TODO: validate password strength

            # 3.
            # create database connection if it's not there already
            self.api = Api(
                database_folder_path=self.settings.database_folder_path,
                password_string=self.password_submission
                )

            try:
                # check the password validity
                self.api.test_database_connection()
                successful_decryption=True
            except InvalidPasswordException:
                continue
            else:
                successful_decryption=True


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
        get_passwords(self)

    def tab_changed(self):
        get_notes(self)
        get_passwords(self)

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

        # Delete Password Button
        self.delete_password_button = QAction(QIcon('PythonPasswordManager/icons/add.png'),"Delete Password",self)
        self.tool_bar.addAction(self.delete_password_button)
        self.delete_password_button.triggered.connect(lambda: delete_password(self))
        self.tool_bar.addSeparator()

        # Add Note Button
        self.add_note_button=QAction(QIcon('PythonPasswordManager/icons/users.png'),"Add Note",self)
        self.tool_bar.addAction(self.add_note_button)
        self.add_note_button.triggered.connect(lambda: create_note(self))
        self.tool_bar.addSeparator()

        # Delete Note Button
        self.delete_note_button = QAction(QIcon('PythonPasswordManager/icons/users.png'),"Delete Note",self)
        self.tool_bar.addAction(self.delete_note_button)
        self.delete_note_button.triggered.connect(lambda: delete_note(self))
        self.tool_bar.addSeparator()

    def tab_widget(self):
        """
        Creates a blank canvas with 2 tabs.
        """
        # create main tab
        self.tabs=QTabWidget()
        self.tabs.blockSignals(True)
        self.tabs.currentChanged.connect(self.tab_changed)
        self.setCentralWidget(self.tabs)

        # create individual tabs
        self.password_tab=QWidget()
        self.note_tab=QWidget()
        self.tabs.addTab(self.password_tab,"Password")
        self.tabs.addTab(self.note_tab,"Notes")

    def widgets(self):
        # Create Password Table Widget
        self.password_table = QTableWidget()
        # makes clicks select the whole row
        self.password_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # disallows the editing of tables
        self.password_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.password_table.setColumnCount(7)
        self.password_table.setColumnHidden(0,True) # hides the Password Id column
        self.password_table.setHorizontalHeaderItem(0,QTableWidgetItem("Password Id"))
        self.password_table.setHorizontalHeaderItem(1,QTableWidgetItem("Website"))
        self.password_table.setHorizontalHeaderItem(2,QTableWidgetItem("Username"))
        self.password_table.setHorizontalHeaderItem(3,QTableWidgetItem("Email"))
        self.password_table.setHorizontalHeaderItem(4,QTableWidgetItem("Password"))
        self.password_table.setHorizontalHeaderItem(5,QTableWidgetItem("Category"))
        self.password_table.setHorizontalHeaderItem(6,QTableWidgetItem("Note"))
        self.password_table.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        self.password_table.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)
        self.password_table.doubleClicked.connect(lambda: select_password(self))


        # Create widgets to go in the Password Search QGroupBox
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
        self.email_radiobutton = QRadioButton("Email")
        self.financial_radiobutton = QRadioButton("Financial")
        self.shopping_radiobutton = QRadioButton("Shopping")
        self.social_radiobutton = QRadioButton("Social")
        self.clear_button=QPushButton("Clear")
        # TODO: flesh out method
        self.clear_button.clicked.connect(lambda: clear_radio_buttons(self))
        # TODO: flesh out style sheet
        # self.listButton.setStyleSheet(style.listButtonStyle())


        # tab_two widgets
        self.note_table=QTableWidget()
        # makes clicks select the whole row
        self.note_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # disallows the editing of tables
        self.note_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.note_table.setColumnCount(2)
        self.note_table.setHorizontalHeaderItem(0,QTableWidgetItem("Id"))
        self.note_table.setHorizontalHeaderItem(1,QTableWidgetItem("Content"))
        self.note_table.horizontalHeader().setSectionResizeMode(0,QHeaderView.Stretch)
        self.note_table.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        self.note_table.doubleClicked.connect(lambda: select_note(self))
        self.note_search_text=QLabel("Search")
        self.note_search_entry=QLineEdit()
        self.note_search_entry.setPlaceholderText("Search by Content")
        self.note_search_entry.textChanged.connect(lambda: check_if_blank(self))
        self.note_search_button=QPushButton("Search")
        self.note_search_button.clicked.connect(lambda: search_note_by_content(self))

    def layouts(self):
        # tab 1 layous
        self.main_layout=QHBoxLayout()
        self.main_left_layout=QVBoxLayout()
        self.main_right_layout=QVBoxLayout()
        self.right_top_layout=QHBoxLayout()
        self.right_middle_layout=QHBoxLayout()
        self.top_group_box=QGroupBox("Password Search")
        # TODO: flesh out style sheet
        # self.topGroupBox.setStyleSheet(style.searchBoxStyle())
        self.middle_group_box=QGroupBox("Filter By Category")
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
        self.right_middle_layout.addWidget(self.email_radiobutton)
        self.right_middle_layout.addWidget(self.financial_radiobutton)
        self.right_middle_layout.addWidget(self.shopping_radiobutton)
        self.right_middle_layout.addWidget(self.social_radiobutton)
        self.right_middle_layout.addWidget(self.clear_button)
        self.middle_group_box.setLayout(self.right_middle_layout)

        self.main_right_layout.addWidget(self.top_group_box,20)
        self.main_right_layout.addWidget(self.middle_group_box,20)
        self.main_right_layout.addWidget(self.bottom_group_box,60)
        self.main_layout.addLayout(self.main_left_layout,70)
        self.main_layout.addLayout(self.main_right_layout,30)
        self.password_tab.setLayout(self.main_layout)
        # makes the bottom_group_box sort of invisible
        # https://stackoverflow.com/a/42485560
        self.bottom_group_box.setFlat(True)
        self.bottom_group_box.setStyleSheet("border:0;")
        
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
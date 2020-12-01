import sys
import os
from pathlib import Path
from PyQt5 import QtWidgets

from UserInterface import MainWindow
from Settings import Settings
from Api import Api


if __name__ == '__main__':
    # load settings
    settings = Settings()
    
    # TODO: make this go bye bye. handle instantiation within MainWindow
    api = Api(database_path='./database.db')

    # run the UI
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(settings, api)
    sys.exit(app.exec())
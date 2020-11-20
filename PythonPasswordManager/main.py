import sys
import os
from pathlib import Path
from PyQt5 import QtWidgets

from UserInterface import ManagerWindow
from Settings import Settings
from Api import Api


if __name__ == '__main__':
    # load settings
    cwd = os.getcwd()
    cwd = Path(cwd)
    settings_file = cwd / 'password_manager_settings.json'
    settings = Settings()

    try:
        settings.load_json_settings(settings_file)
    except FileNotFoundError:
        # could not fine the settings file
        pass


    # run the UI
    app = QtWidgets.QApplication(sys.argv)
    window = ManagerWindow(settings, Api)
    sys.exit(app.exec())
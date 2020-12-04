import sys
import os
from pathlib import Path
from PyQt5 import QtWidgets

from UserInterface import MainWindow
from Settings import Settings


if __name__ == '__main__':
    # load settings
    settings = Settings()

    # run the UI
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(settings)
    sys.exit(app.exec())
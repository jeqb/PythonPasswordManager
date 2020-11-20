# run the UI
import sys
from PyQt5 import QtWidgets

from UserInterface import ManagerWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ManagerWindow()
    sys.exit(app.exec())
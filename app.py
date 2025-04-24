# app file -- bring everyhting together
# @author : Ethan Eshbaugh
# 4/24/2025

import sys
from PySide6 import QtWidgets
import sys
import os

from gui.main_window import MainWindow

def main():
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.setWindowTitle("Scrabble Solver")
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
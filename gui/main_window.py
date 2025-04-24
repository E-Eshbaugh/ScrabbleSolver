# PySide6 GUI implementation for app main window
# @author : Ethan Eshbaugh
# 4/24/2025

from datetime import datetime
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import QStringListModel
from gui.ui_main_window import Ui_MainWindow
from algorithms.anagrams import find_anagrams
from algorithms.hooks import find_hooks
from data import log_search


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Two separate models for Anagram and Hook results
        self.anagram_model = QStringListModel(self)
        self.hook_model = QStringListModel(self)

        # Bind each model to its respective QListView
        # Make sure in Qt Designer you named the Anagram tab's QListView: resultsView_2
        # and the Hook tab's QListView: resultsView
        self.ui.resultView2.setModel(self.anagram_model)
        self.ui.resultView.setModel(self.hook_model)

        # Connect buttons
        self.ui.runButton_2.clicked.connect(self.on_anagram)  # Anagram tab button
        self.ui.runButton.clicked.connect(self.on_hook)       # Hook tab button

    def on_anagram(self):
        rack = self.ui.inputLine_2.text().strip().lower()
        if len(rack) != 7:
            QMessageBox.warning(
                self,
                "Input Error",
                "Anagram mode requires exactly 7 letters."
            )
            return

        results = find_anagrams(rack)
        timestamp = datetime.now().isoformat()
        try:
            log_search(rack, "anagram", timestamp)
        except Exception as e:
            QMessageBox.critical(
                self,
                "Logging Failed",
                f"Could not log search: {e}"
            )

        self.anagram_model.setStringList(results)

    def on_hook(self):
        word = self.ui.inputLine.text().strip().lower()
        if not word:
            QMessageBox.warning(
                self,
                "Input Error",
                "Hook mode requires a non-empty word."
            )
            return

        results = find_hooks(word)
        timestamp = datetime.now().isoformat()
        try:
            log_search(word, "hook", timestamp)
        except Exception as e:
            QMessageBox.critical(
                self,
                "Logging Failed",
                f"Could not log search: {e}"
            )

        self.hook_model.setStringList(results)
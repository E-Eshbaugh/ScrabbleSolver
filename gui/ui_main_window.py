# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLineEdit, QListView, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(520, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 781, 541))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.inputLine_2 = QLineEdit(self.tab)
        self.inputLine_2.setObjectName(u"inputLine_2")
        self.inputLine_2.setGeometry(QRect(20, 30, 151, 22))
        self.inputLine_2.setClearButtonEnabled(False)
        self.runButton_2 = QPushButton(self.tab)
        self.runButton_2.setObjectName(u"runButton_2")
        self.runButton_2.setGeometry(QRect(90, 60, 75, 24))
        self.resultView2 = QListView(self.tab)
        self.resultView2.setObjectName(u"resultView2")
        self.resultView2.setGeometry(QRect(190, 30, 311, 471))
        self.textEdit = QTextEdit(self.tab)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(190, 0, 251, 31))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.inputLine = QLineEdit(self.tab_2)
        self.inputLine.setObjectName(u"inputLine")
        self.inputLine.setGeometry(QRect(20, 30, 151, 22))
        self.inputLine.setEchoMode(QLineEdit.EchoMode.Normal)
        self.runButton = QPushButton(self.tab_2)
        self.runButton.setObjectName(u"runButton")
        self.runButton.setGeometry(QRect(90, 60, 75, 24))
        self.resultView = QListView(self.tab_2)
        self.resultView.setObjectName(u"resultView")
        self.resultView.setGeometry(QRect(190, 30, 311, 471))
        self.textEdit_2 = QTextEdit(self.tab_2)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(190, 0, 251, 31))
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 520, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.inputLine_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.inputLine_2.setInputMask("")
        self.inputLine_2.setText("")
        self.inputLine_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Your 7 Letters Here", None))
        self.runButton_2.setText(QCoreApplication.translate("MainWindow", u"- Submit -", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Results (sorted by score - highest to lowest) :</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Word Finder", None))
#if QT_CONFIG(tooltip)
        self.inputLine.setToolTip(QCoreApplication.translate("MainWindow", u"Enter Text", None))
#endif // QT_CONFIG(tooltip)
        self.inputLine.setText("")
        self.inputLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Word to Extend", None))
        self.runButton.setText(QCoreApplication.translate("MainWindow", u"- Submit -", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Results (sorted by score - highest to lowest) :</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Extension Finder", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'coder.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(364, 497)
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow \n"
"{	\n"
"	background-color: rgb(255, 170, 127);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	margin-top: 10px;\n"
"	background-color: rgb(249, 255, 143);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	background-color: rgb(255, 255, 127);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 111, 51))
        self.label.setStyleSheet(u"font: 20pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);")
        self.source_text = QTextEdit(self.centralwidget)
        self.source_text.setObjectName(u"source_text")
        self.source_text.setGeometry(QRect(30, 90, 301, 111))
        self.indent = QDial(self.centralwidget)
        self.indent.setObjectName(u"indent")
        self.indent.setGeometry(QRect(190, 20, 50, 64))
        self.indent_screen = QLCDNumber(self.centralwidget)
        self.indent_screen.setObjectName(u"indent_screen")
        self.indent_screen.setGeometry(QRect(250, 30, 81, 41))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 230, 131, 51))
        self.label_2.setStyleSheet(u"font: 20pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);")
        self.translation = QTextBrowser(self.centralwidget)
        self.translation.setObjectName(u"translation")
        self.translation.setGeometry(QRect(30, 290, 301, 111))
        self.encode = QPushButton(self.centralwidget)
        self.encode.setObjectName(u"encode")
        self.encode.setGeometry(QRect(30, 420, 131, 61))
        self.encode.setStyleSheet(u"font: 12pt \"Comic Sans MS\";\n"
"border-radius: 20px;\n"
"border: 1px solid; \n"
"background-color: rgb(255, 255, 255);")
        self.decode = QPushButton(self.centralwidget)
        self.decode.setObjectName(u"decode")
        self.decode.setGeometry(QRect(190, 420, 141, 61))
        self.decode.setStyleSheet(u"font: 12pt \"Comic Sans MS\";\n"
"border-radius: 20px;\n"
"border: 1px solid; \n"
"background-color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0441\u0442", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0432\u043e\u0434", None))
        self.encode.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.decode.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043a\u043e\u0434\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
    # retranslateUi


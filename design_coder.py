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
        MainWindow.resize(364, 530)
        MainWindow.setStyleSheet(u"QMainWindow \n"
"{\n"
"	\n"
"	background-color: rgb(124, 19, 21);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 111, 51))
        self.label.setStyleSheet(u"font: 20pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(30, 90, 301, 111))
        self.dial = QDial(self.centralwidget)
        self.dial.setObjectName(u"dial")
        self.dial.setGeometry(QRect(180, 20, 50, 64))
        self.lcdNumber = QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(250, 30, 81, 41))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 250, 131, 51))
        self.label_2.setStyleSheet(u"font: 20pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(30, 310, 301, 111))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 440, 131, 61))
        self.pushButton.setStyleSheet(u"font: 12pt \"Comic Sans MS\";\n"
"border-radius: 20px;\n"
"border: 1px solid; \n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(190, 440, 131, 61))
        self.pushButton_2.setStyleSheet(u"font: 12pt \"Comic Sans MS\";")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0441\u0442", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0432\u043e\u0434", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043a\u043e\u0434\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
    # retranslateUi


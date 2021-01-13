#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog
from PySide2 import QtCore
# импортируем связанный py файл с нашим ui файлом
from design_coder import Ui_MainWindow

class Coder:
    def encode_symbol(self, symbol, operation_type, indent=3):
        if operation_type == 'encode': 
            symbol_number = ord(symbol) +indent
        elif operation_type == 'decode': 
            symbol_number = ord(symbol) -indent
        new_symbol = chr(symbol_number)
        return new_symbol

    def translation(self, text, operation_type):
        translated = ''
        for symb in text:
            translated += self.encode_symbol(symb, operation_type)
        return translated

class MainWindow(QMainWindow, Coder):
    def __init__(self):
		# вызовем метод родительского класса
        super(MainWindow, self).__init__()

        # создадим объект
        self.ui = Ui_MainWindow()
        # инициализируем нашу форму
        self.ui.setupUi(self)

        # Соединим сигналы со слотами
        self.ui.encode.clicked.connect(self.pushed_button)
        self.ui.decode.clicked.connect(self.pushed_button)
        self.ui.indent.valueChanged.connect(self.set_indent)


    def set_indent(self):
        print(self.ui.indent.value())


    # функция при нажатии на кнопку
    def pushed_button(self):
        button = self.sender()
        object_name = button.objectName()

        source = self.ui.source_text.toPlainText()
        self.ui.translation.setText(self.translation(source, object_name)) 
       

        





if __name__ == "__main__":
    # Создадим Qt Application
    app = QApplication(sys.argv)
    # Создадим и покажем главное окно
    window = MainWindow()
    # Показываем окно
    window.show()
    # Запустим приложение
    sys.exit(app.exec_())




       

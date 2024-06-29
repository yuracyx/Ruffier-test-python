from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
                             QRadioButton, QPushButton, QButtonGroup)
from inst import *

class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.indexcalculate = 0
        self.initUI()

    def set_appear(self):
        self.setWindowTitle(name)
        self.resize(weight, height)
        self.move(x, y)

    def index(self):
        self.index_calculate = (4 * (int(self.exp.t1) + int(self.exp.t2) + int(self.exp.t3)) - 200) / 10
    def result(self):
        if int(self.exp.age) >= 15:
            if self.index_calculate > 15:
                return txt_res1
            elif self.index_calculate > 11 and self.index_calculate < 14.9:
                return txt_res2
            elif self.index_calculate > 6 and self.index_calculate < 10.9:
                return txt_res3
            elif self.index_calculate > 0.5 and self.index_calculate < 5.9:
                return txt_res4
            else:
                return txt_res5
        elif int(self.exp.age) >= 13 and int(self.exp.age) <= 14:
            if self.index_calculate > 16.5:
                return txt_res1
            elif self.index_calculate > 12.5 and self.index_calculate < 16.4:
                return txt_res2
            elif self.index_calculate > 7.5 and self.index_calculate < 12.4:
                return txt_res3
            elif self.index_calculate > 2 and self.index_calculate < 7.4:
                return txt_res4
            else:
                return txt_res5
        elif int(self.exp.age) >= 11 and int(self.exp.age) <= 12:
            if self.index_calculate > 18:
                return txt_res1
            elif self.index_calculate > 14 and self.index_calculate < 17.9:
                return txt_res2
            elif self.index_calculate > 9 and self.index_calculate < 13.9:
                return txt_res3
            elif self.index_calculate > 3.5 and self.index_calculate < 8.9:
                return txt_res4
            else:
                return txt_res5
        elif int(self.exp.age) >= 9 and int(self.exp.age) <= 10:
            if self.index_calculate > 19.5:
                return txt_res1
            elif self.index_calculate > 15.5 and self.index_calculate < 19.4:
                return txt_res2
            elif self.index_calculate > 10.5 and self.index_calculate < 15.4:
                return txt_res3
            elif self.index_calculate > 5 and self.index_calculate < 10.4:
                return txt_res4
            else:
                return txt_res5
        elif int(self.exp.age) >= 7 and int(self.exp.age) <= 8:
            if self.index_calculate > 21:
                return txt_res1
            elif self.index_calculate > 17 and self.index_calculate < 20.9:
                return txt_res2
            elif self.index_calculate > 12 and self.index_calculate < 16.9:
                return txt_res3
            elif self.index_calculate > 6.5 and self.index_calculate < 11.9:
                return txt_res4
            else:
                return txt_res5
    def initUI(self):
        self.index()
        result_text = self.result()
        self.surname = QLabel('ФИО: ' + self.exp.name)
        self.index = QLabel('Индекс Руфье: ' + str(self.index_calculate))
        self.result = QLabel('Работоспособность сердца: ' + result_text)
        self.vertical = QVBoxLayout()
        self.vertical.addWidget(self.surname, alignment=Qt.AlignCenter)
        self.vertical.addWidget(self.index, alignment=Qt.AlignCenter)
        self.vertical.addWidget(self.result, alignment=Qt.AlignCenter)
        self.setLayout(self.vertical)
        self.show()


from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
                             QRadioButton, QPushButton, QButtonGroup, QLineEdit)
from PyQt5.QtGui import QFont
from final_win import *
from inst import *

class Experiment():
    def __init__(self, name, age, t1, t2, t3):
        self.name = name
        self.age = age
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(name)
        self.resize(weight, height)
        self.move(x, y)

    def initUI(self):
        self.timer_label = QLabel('00:00:15')
        self.timer_label.setFont(QFont('Times', 36, QFont.Bold))
        self.line_1 = QLabel('Введите Ф.И.О.:')
        self.line_2 = QLineEdit()
        self.line_3 = QLabel('Полных лет:')
        self.line_4 = QLineEdit()
        self.line_5 = QLabel(instruction_2)
        self.line_6 = QPushButton('Начать тест')
        self.line_7 = QLineEdit()
        self.line_8 = QLabel(instruction_3)
        self.line_9 = QPushButton('Начать приседать')
        self.line_10 = QLabel(instruction_4)
        self.line_11 = QPushButton('Начать финальный тест')
        self.line_12 = QLineEdit()
        self.line_13 = QLineEdit()
        self.line_14 = QPushButton('Отправить результаты')

        self.vertical_r = QVBoxLayout()
        self.vertical_l = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        screen = [self.line_1, self.line_2, self.line_3, self.line_4, self.line_5, self.line_6, self.line_7,
                  self.line_8, self.line_9, self.line_10, self.line_11, self.line_12, self.line_13]

        self.horizontal.addLayout(self.vertical_l)
        self.horizontal.addLayout(self.vertical_r)

        for line in screen:
            self.vertical_l.addWidget(line, alignment=Qt.AlignLeft)

        self.vertical_l.addWidget(self.line_14, alignment=Qt.AlignCenter)
        self.vertical_r.addWidget(self.timer_label, alignment=Qt.AlignCenter)

        self.setLayout(self.horizontal)
        self.show()

    def connects(self):
        self.line_14.clicked.connect(self.next_click)
        self.line_6.clicked.connect(self.test_timer)
        self.line_9.clicked.connect(self.test_timer2)
        self.line_11.clicked.connect(self.test_timer3)
    def next_click(self):
        self.hide()
        self.exp = Experiment(self.line_2.text(),self.line_4.text(), self.line_7.text(), self.line_12.text(),
                              self.line_13.text())
        self.win_3 = FinalWin(self.exp)

    def test_timer(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.timer_label.setText(time.toString('hh:mm:ss'))
        self.timer_label.setStyleSheet('color:rgb(0, 0, 0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def test_timer2(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.timer_label.setText(time.toString('hh:mm:ss')[6:8])
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def test_timer3(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.timer_label.setText(time.toString('hh:mm:ss'))
        if int(time.toString('hh:mm:ss')[6:8]) >= 45:
            self.timer_label.setStyleSheet('color:rgb(0, 255, 0)')
        elif int(time.toString('hh:mm:ss')[6:8]) <= 15:
            self.timer_label.setStyleSheet('color:rgb(255, 0, 0)')
        else:
            self.timer_label.setStyleSheet('color:rgb(0, 0, 0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
                             QRadioButton, QPushButton, QButtonGroup)
from time import sleep
from second_win import *
from inst import *

class MainWin(QWidget):
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
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(instruction)
        self.button = QPushButton(btn_next)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text)
        self.layout.addWidget(self.instruction)
        self.layout.addWidget(self.button, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)
        self.show()
    def connects(self):
        self.button.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.win_2 = TestWin()


app = QApplication([])
app.setStyle('Fusion')
win_1 = MainWin()
app.exec_()


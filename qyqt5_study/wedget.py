import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from bs4 import BeautifulSoup as bs


class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('asdad', self)
        btn.resize(btn.sizeHint())
        btn.setToolTip("aaaaaaa")
        btn.move(20, 30)

        self.setGeometry(300, 300, 400, 500)
        self.setWindowTitle('첫번째 학습')
        self.show()


app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())

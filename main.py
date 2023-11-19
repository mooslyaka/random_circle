import sys
from random import randint
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

class QT(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
        self.do_paint = False

    def draw(self, qp):
        zxc = randint(10, 500)
        x = randint(0, 800)
        y = randint(0, 600)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(x, y, zxc, zxc)
    def run(self):
        self.do_paint = True
        self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QT()
    ex.show()
    sys.exit(app.exec())
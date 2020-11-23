import sys

from PySide2.QtWidgets import *
from PySide2.QtGui import *

class BuleungBuleung(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Buleung Buleung')
        self.setWindowIcon(QIcon('images/window_icon.png'))
        self.setFixedSize(1280, 800)
        bg = QLabel(self)
        pixmap = QPixmap('images/main.png')
        bg.setPixmap(pixmap)
        bg.setFixedSize(1280, 800)

        #버튼
        start = QPushButton("start", self)
        start.setGeometry(395, 300, 490, 200)
        start.setStyleSheet('QPushButton{background-color: rgba(0, 0, 0, 0.0)}')
        start.mousePressEvent(self.move_game_choice())
        self.show()

    def move_game_choice(self):
        self.pixmap = QPixmap('images/main_game_choice.png')
        self.bg.setPixmap(self.pixmap)

class BuleungBuleung(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Buleung Buleung')
        self.setWindowIcon(QIcon('images/window_icon.png'))
        self.setFixedSize(1280, 800)
        bg = QLabel(self)
        bg.setPixmap(QPixmap('images/main.png'))
        bg.setFixedSize(1280, 800)

        #버튼
        start = QPushButton("start", self)
        start.setGeometry(395, 300, 490, 200)
        start.setStyleSheet('QPushButton{background-color: rgba(0, 0, 0, 0.0)}')
        start.mousePressEvent(bg.setPixmap(QPixmap('images/main_game_choice.png')))
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = BuleungBuleung()
    sys.exit(app.exec_())
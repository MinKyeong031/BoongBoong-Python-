import sys
import pygame

from PySide2 import QtGui
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QLabel, QPushButton, QWidget, QMessageBox, QApplication, QDesktopWidget, \
    QGraphicsOpacityEffect


class BuleungBuleung(QWidget):
    def __init__(self):
        super().__init__()
        self.main_buleung_buleunng()
        self.main_music = 'music/backgroundmusic.mp3'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.main_music)
        pygame.mixer.music.play(-1)

    def main_buleung_buleunng(self):
        #메인페이지 사진
        self.main_background_lb = QLabel(self)
        main_background = QtGui.QPixmap("images/main.png")
        self.main_background_lb.setFixedSize(1280, 800)
        self.main_background_lb.setPixmap(main_background)

        #메인페이지 시작버튼
        main_start_btn = QPushButton(self.main_background_lb)
        main_start_btn.setGeometry(395, 300, 490, 200)
        main_start_btn.clicked.connect(self.main_start_click)
        opacity = QGraphicsOpacityEffect(main_start_btn)
        opacity.setOpacity(0)
        main_start_btn.setGraphicsEffect(opacity)

        #메인페이지 게임 방법 버튼
        main_rule_btn = QPushButton(self.main_background_lb)
        main_rule_btn.setGeometry(1050, 470, 235, 130)
        main_rule_btn.clicked.connect(self.main_rule_click)
        opacity = QGraphicsOpacityEffect(main_rule_btn)
        opacity.setOpacity(0)
        main_rule_btn.setGraphicsEffect(opacity)

        #메인페이지 랭킹 버튼
        main_rank_btn = QPushButton(self)
        main_rank_btn.setGeometry(1050, 615, 235, 130)
        main_rank_btn.clicked.connect(self.main_rank_click)
        opacity = QGraphicsOpacityEffect(main_rank_btn)
        opacity.setOpacity(0)
        main_rank_btn.setGraphicsEffect(opacity)

        #실행 창
        self.setWindowTitle('新부릉부릉')
        self.setWindowIcon(QIcon('images/window_icon.png'))
        self.setFixedSize(1280, 800)
        cursor = QtGui.QCursor(QtGui.QPixmap('images/cusor.png'))
        self.setCursor(cursor)
        self.center()
        self.show()

    def main_start_click(self):
        self.game_choice()

    def main_rule_click(self):
        self.rule_notice()

    def main_rank_click(self):
        self.rank_choice()

    def game_choice(self):
        self.main_start_background_lb = QLabel(self)
        main_start_background_lb = QtGui.QPixmap("images/main_game_choice.png")
        self.main_start_background_lb.setFixedSize(1280, 800)
        self.main_start_background_lb.setPixmap(main_start_background_lb)
        self.main_background_lb.setVisible(False)
        self.main_start_background_lb.setVisible(True)

    def rule_notice(self):
        self.main_rule_background_lb = QLabel(self)
        main_rule_background_lb = QtGui.QPixmap("images/main_rule_notice.png")
        self.main_rule_background_lb.setFixedSize(1280, 800)
        self.main_rule_background_lb.setPixmap(main_rule_background_lb)
        self.main_background_lb.setVisible(False)
        self.main_rule_background_lb.setVisible(True)

    def rank_choice(self):
        self.main_rank_background_lb = QLabel(self)
        main_rank_background_lb = QtGui.QPixmap("images/main_rank_choice.png")
        self.main_rank_background_lb.setFixedSize(1280, 800)
        self.main_rank_background_lb.setPixmap(main_rank_background_lb)
        self.main_background_lb.setVisible(False)
        self.main_rank_background_lb.setVisible(True)

    def center(self):
        window_xy = self.frameGeometry()
        center_xy = QDesktopWidget().availableGeometry().center()
        window_xy.moveCenter(center_xy)
        self.move(window_xy.topLeft())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '게임 종료', '新부릉부릉을 종료하시겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = BuleungBuleung()
    sys.exit(app.exec_())
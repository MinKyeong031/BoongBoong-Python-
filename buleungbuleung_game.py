import csv
import sys

import pygame
import random
import time
import pandas as pd

from PySide2 import QtGui
from PySide2.QtGui import QIcon, Qt, QFont
from PySide2.QtWidgets import QLabel, QPushButton, QWidget, QMessageBox, QApplication, QDesktopWidget, QGraphicsOpacityEffect, QLineEdit

#TODO 주석, 파일입출력
class BuleungBuleung(QWidget):
    game_q = ["급정지", "출발", "좌회전", "우회전", "후진", "방지턱"]
    game_life = 3
    score = 0
    begin = 0
    now_q = 0
    level = 0
    lv1_cnt = 0
    rank_name = ""
    rank_score = 0
    rank_value = ""

    now_game_life = "images/game_life1.png"
    play_sounds = []
    pygame.init()
    pygame.mixer.init()
    play_sounds.append(pygame.mixer.Sound("music/stop.wav"))
    play_sounds.append(pygame.mixer.Sound("music/start.wav"))
    play_sounds.append(pygame.mixer.Sound("music/left.wav"))
    play_sounds.append(pygame.mixer.Sound("music/right.wav"))
    play_sounds.append(pygame.mixer.Sound("music/back.wav"))
    play_sounds.append(pygame.mixer.Sound("music/bump.wav"))#5
    play_sounds.append(pygame.mixer.Sound("music/stop_q.wav"))
    play_sounds.append(pygame.mixer.Sound("music/start_q.wav"))
    play_sounds.append(pygame.mixer.Sound("music/left_q.wav"))
    play_sounds.append(pygame.mixer.Sound("music/right_q.wav"))
    play_sounds.append(pygame.mixer.Sound("music/back_q.wav"))
    play_sounds.append(pygame.mixer.Sound("music/bump_q.wav"))#11
    play_sounds.append(pygame.mixer.Sound("music/backgroundmusic.wav"))
    play_sounds.append(pygame.mixer.Sound("music/game_start.wav"))
    play_sounds.append(pygame.mixer.Sound("music/fail.wav"))
    play_sounds.append(pygame.mixer.Sound("music/result_input.wav"))#15


    def __init__(self):
        super().__init__()
        self.main_buleung_buleunng()
        self.play_sounds[12].play(-1)
        self.play_sounds[12].set_volume(0.4)

    # 메인페이지
    def main_buleung_buleunng(self):
        # 메인페이지 사진
        self.main_background_lb = QLabel(self)
        main_background_bg = QtGui.QPixmap("images/main.png")
        self.main_background_lb.setFixedSize(1280, 800)
        self.main_background_lb.setPixmap(main_background_bg)

        # 메인페이지 시작버튼
        main_start_btn = QPushButton(self.main_background_lb)
        main_start_btn.setGeometry(395, 300, 490, 200)
        main_start_btn.clicked.connect(self.go_game_choice)
        opacity = QGraphicsOpacityEffect(main_start_btn)
        opacity.setOpacity(0)
        main_start_btn.setGraphicsEffect(opacity)

        # 메인페이지 게임 방법 버튼
        main_rule_btn = QPushButton(self.main_background_lb)
        main_rule_btn.setGeometry(1050, 470, 235, 130)
        main_rule_btn.clicked.connect(self.go_rule_notice)
        opacity = QGraphicsOpacityEffect(main_rule_btn)
        opacity.setOpacity(0)
        main_rule_btn.setGraphicsEffect(opacity)

        # 메인페이지 랭킹 버튼
        main_rank_btn = QPushButton(self)
        main_rank_btn.setGeometry(1050, 615, 235, 130)
        main_rank_btn.clicked.connect(self.go_rank_choice)
        opacity = QGraphicsOpacityEffect(main_rank_btn)
        opacity.setOpacity(0)
        main_rank_btn.setGraphicsEffect(opacity)

        # 실행 창
        self.setWindowTitle('新부릉부릉')
        self.setWindowIcon(QIcon('images/window_icon.png'))
        self.setFixedSize(1280, 800)
        cursor = QtGui.QCursor(QtGui.QPixmap('images/cusor.png'))
        self.setCursor(cursor)
        self.center()
        self.show()

        self.main_background_lb.setVisible(True)


    def go_game_choice(self):
        self.game_choice()
    def go_rule_notice(self):
        self.rule_notice()
    def go_rank_choice(self):
        self.rank_choice()

    # 게임 난이도 선택 페이지
    def game_choice(self):
        # 게임 난이도 선택 페이지 사진
        self.main_start_background_lb = QLabel(self)
        main_start_background_bg = QtGui.QPixmap("images/main_game_choice.png")
        self.main_start_background_lb.setFixedSize(1280, 800)
        self.main_start_background_lb.setPixmap(main_start_background_bg)

        # 취소 버튼
        start_exit_btn = QPushButton(self.main_start_background_lb)
        start_exit_btn.setGeometry(925, 220, 60, 60)
        opacity = QGraphicsOpacityEffect(start_exit_btn)
        opacity.setOpacity(0)
        start_exit_btn.setGraphicsEffect(opacity)
        start_exit_btn.clicked.connect(self.go_start_main_buleung_buleunng)

        # 난이도 1 선택 버튼
        start_lv1_btn = QPushButton(self.main_start_background_lb)
        start_lv1_btn.setGeometry(340, 320, 140, 140)
        opacity = QGraphicsOpacityEffect(start_lv1_btn)
        opacity.setOpacity(0)
        start_lv1_btn.setGraphicsEffect(opacity)
        start_lv1_btn.clicked.connect(self.go_game1_buleung_buleunng)

        # 난이도 2 선택 버튼
        start_lv2_btn = QPushButton(self.main_start_background_lb)
        start_lv2_btn.setGeometry(500, 430, 140, 140)
        opacity = QGraphicsOpacityEffect(start_lv2_btn)
        opacity.setOpacity(0)
        start_lv2_btn.setGraphicsEffect(opacity)
        start_lv2_btn.clicked.connect(self.go_game2_buleung_buleunng)

        # 난이도 3 선택 버튼
        start_lv3_btn = QPushButton(self.main_start_background_lb)
        start_lv3_btn.setGeometry(655, 320, 140, 140)
        opacity = QGraphicsOpacityEffect(start_lv3_btn)
        opacity.setOpacity(0)
        start_lv3_btn.setGraphicsEffect(opacity)
        start_lv3_btn.clicked.connect(self.go_game3_buleung_buleunng)

        # 난이도 4 선택 버튼
        start_lv4_btn = QPushButton(self.main_start_background_lb)
        start_lv4_btn.setGeometry(812, 430, 140, 140)
        opacity = QGraphicsOpacityEffect(start_lv4_btn)
        opacity.setOpacity(0)
        start_lv4_btn.setGraphicsEffect(opacity)
        start_lv4_btn.clicked.connect(self.go_game4_buleung_buleunng)

        self.main_background_lb.setVisible(False)
        self.main_start_background_lb.setVisible(True)

    def go_start_main_buleung_buleunng(self):
        self.main_background_lb.setVisible(True)
        self.main_start_background_lb.setVisible(False)

    def go_game1_buleung_buleunng(self):
        self.play_sounds[13].play(0)
        time.sleep(4)
        self.game1_buleung_buleunng()
    def go_game2_buleung_buleunng(self):
        self.play_sounds[13].play(0)
        time.sleep(4)
        self.game2_buleung_buleunng("images/game_life1.png")
    def go_game3_buleung_buleunng(self):
        self.play_sounds[13].play(0)
        time.sleep(4)
        self.game3_buleung_buleunng("images/game_life1.png")
    def go_game4_buleung_buleunng(self):
        self.play_sounds[13].play(0)
        time.sleep(4)
        self.game4_buleung_buleunng("images/game_life1.png")

    # 게임 페이지1
    def game1_buleung_buleunng(self):
        self.level = 1
        # 게임 페이지 사진
        self.game1_background_lb = QLabel(self)
        game1_background_bg = QtGui.QPixmap("images/game_life1.png")
        self.game1_background_lb.setFixedSize(1280, 800)
        self.game1_background_lb.setPixmap(game1_background_bg)

        # 정답 버튼
        stop_btn1 = QPushButton(self.game1_background_lb)
        stop_btn1.setGeometry(10, 380, 200, 200)
        opacity = QGraphicsOpacityEffect(stop_btn1)
        opacity.setOpacity(0)
        stop_btn1.setGraphicsEffect(opacity)

        start_btn1 = QPushButton(self.game1_background_lb)
        start_btn1.setGeometry(224, 576, 200, 200)
        opacity = QGraphicsOpacityEffect(start_btn1)
        opacity.setOpacity(0)
        start_btn1.setGraphicsEffect(opacity)

        left_btn1 = QPushButton(self.game1_background_lb)
        left_btn1.setGeometry(434, 380, 200, 200)
        opacity = QGraphicsOpacityEffect(left_btn1)
        opacity.setOpacity(0)
        left_btn1.setGraphicsEffect(opacity)

        right_btn1 = QPushButton(self.game1_background_lb)
        right_btn1.setGeometry(648, 576, 200, 200)
        opacity = QGraphicsOpacityEffect(right_btn1)
        opacity.setOpacity(0)
        right_btn1.setGraphicsEffect(opacity)

        back_btn1 = QPushButton(self.game1_background_lb)
        back_btn1.setGeometry(858, 380, 200, 200)
        opacity = QGraphicsOpacityEffect(back_btn1)
        opacity.setOpacity(0)
        back_btn1.setGraphicsEffect(opacity)

        bump_btn1 = QPushButton(self.game1_background_lb)
        bump_btn1.setGeometry(1072, 576, 200, 200)
        opacity = QGraphicsOpacityEffect(bump_btn1)
        opacity.setOpacity(0)
        bump_btn1.setGraphicsEffect(opacity)

        # 문제
        self.begin = time.time()
        random_q1 = random.randint(0, 5)
        self.now_q = random_q1
        game_q_label1 = QLabel(self.game_q[random_q1], self.game1_background_lb)
        game_q_label1.setGeometry(385, 219, 510, 100)
        game_q_label1.setFont(QFont("나눔바른펜", 35))
        game_q_label1.setAlignment(Qt.AlignCenter)

        #힌트(난이도1에만 해당)
        if random_q1 == 0:
            opacity = QGraphicsOpacityEffect(stop_btn1)
            opacity.setOpacity(0.3)
            stop_btn1.setGraphicsEffect(opacity)
            stop_btn1.setStyleSheet("background-color:#FF0000; border-radius: 100px")
        elif random_q1 == 1:
            opacity = QGraphicsOpacityEffect(start_btn1)
            opacity.setOpacity(0.3)
            start_btn1.setGraphicsEffect(opacity)
            start_btn1.setStyleSheet("background-color:#FF0000; border-radius: 100px")
        elif random_q1 == 2:
            opacity = QGraphicsOpacityEffect(left_btn1)
            opacity.setOpacity(0.3)
            left_btn1.setGraphicsEffect(opacity)
            left_btn1.setStyleSheet("background-color:#FF0000; border-radius: 100px")
        elif random_q1 == 3:
            opacity = QGraphicsOpacityEffect(right_btn1)
            opacity.setOpacity(0.3)
            right_btn1.setGraphicsEffect(opacity)
            right_btn1.setStyleSheet("background-color:#FF0000; border-radius: 100px")
        elif random_q1 == 4:
            opacity = QGraphicsOpacityEffect(back_btn1)
            opacity.setOpacity(0.3)
            back_btn1.setGraphicsEffect(opacity)
            back_btn1.setStyleSheet("background-color:#FF0000; border-radius: 100px")
        elif random_q1 == 5:
            opacity = QGraphicsOpacityEffect(bump_btn1)
            opacity.setOpacity(0.3)
            bump_btn1.setGraphicsEffect(opacity)
            bump_btn1.setStyleSheet("background-color:#FF0000; border-radius: 100px")
        self.play_sounds[self.now_q+6].play(0)

        if random_q1 == 0:
            stop_btn1.clicked.connect(self.game_o)
            start_btn1.clicked.connect(self.game_x)
            left_btn1.clicked.connect(self.game_x)
            right_btn1.clicked.connect(self.game_x)
            back_btn1.clicked.connect(self.game_x)
            bump_btn1.clicked.connect(self.game_x)
        elif random_q1 == 1:
            stop_btn1.clicked.connect(self.game_x)
            start_btn1.clicked.connect(self.game_o)
            left_btn1.clicked.connect(self.game_x)
            right_btn1.clicked.connect(self.game_x)
            back_btn1.clicked.connect(self.game_x)
            bump_btn1.clicked.connect(self.game_x)
        elif random_q1 == 2:
            stop_btn1.clicked.connect(self.game_x)
            start_btn1.clicked.connect(self.game_x)
            left_btn1.clicked.connect(self.game_o)
            right_btn1.clicked.connect(self.game_x)
            back_btn1.clicked.connect(self.game_x)
            bump_btn1.clicked.connect(self.game_x)
        elif random_q1 == 3:
            stop_btn1.clicked.connect(self.game_x)
            start_btn1.clicked.connect(self.game_x)
            left_btn1.clicked.connect(self.game_x)
            right_btn1.clicked.connect(self.game_o)
            back_btn1.clicked.connect(self.game_x)
            bump_btn1.clicked.connect(self.game_x)
        elif random_q1 == 4:
            stop_btn1.clicked.connect(self.game_x)
            start_btn1.clicked.connect(self.game_x)
            left_btn1.clicked.connect(self.game_x)
            right_btn1.clicked.connect(self.game_x)
            back_btn1.clicked.connect(self.game_o)
            bump_btn1.clicked.connect(self.game_x)
        elif random_q1 == 5:
            stop_btn1.clicked.connect(self.game_x)
            start_btn1.clicked.connect(self.game_x)
            left_btn1.clicked.connect(self.game_x)
            right_btn1.clicked.connect(self.game_x)
            back_btn1.clicked.connect(self.game_x)
            bump_btn1.clicked.connect(self.game_o)
        self.main_start_background_lb.setVisible(False)
        self.game1_background_lb.setVisible(True)

    # 게임 페이지2
    def game2_buleung_buleunng(self, life_img):
        self.level = 2
        self.now_game_life = life_img
        # 게임 페이지 사진
        self.game2_background_lb = QLabel(self)
        game2_background_bg = QtGui.QPixmap(life_img)
        self.game2_background_lb.setFixedSize(1280, 800)
        self.game2_background_lb.setPixmap(game2_background_bg)

        # 정답 버튼
        stop_btn2 = QPushButton(self.game2_background_lb)
        stop_btn2.setGeometry(10, 380, 200, 200)
        opacity = QGraphicsOpacityEffect(stop_btn2)
        opacity.setOpacity(0)
        stop_btn2.setGraphicsEffect(opacity)

        start_btn2 = QPushButton(self.game2_background_lb)
        start_btn2.setGeometry(224, 576, 200, 200)
        opacity = QGraphicsOpacityEffect(start_btn2)
        opacity.setOpacity(0)
        start_btn2.setGraphicsEffect(opacity)

        left_btn2 = QPushButton(self.game2_background_lb)
        left_btn2.setGeometry(434, 380, 200, 200)
        opacity = QGraphicsOpacityEffect(left_btn2)
        opacity.setOpacity(0)
        left_btn2.setGraphicsEffect(opacity)

        right_btn2 = QPushButton(self.game2_background_lb)
        right_btn2.setGeometry(648, 576, 200, 200)
        opacity = QGraphicsOpacityEffect(right_btn2)
        opacity.setOpacity(0)
        right_btn2.setGraphicsEffect(opacity)

        back_btn2 = QPushButton(self.game2_background_lb)
        back_btn2.setGeometry(858, 380, 200, 200)
        opacity = QGraphicsOpacityEffect(back_btn2)
        opacity.setOpacity(0)
        back_btn2.setGraphicsEffect(opacity)

        bump_btn2 = QPushButton(self.game2_background_lb)
        bump_btn2.setGeometry(1072, 576, 200, 200)
        opacity = QGraphicsOpacityEffect(bump_btn2)
        opacity.setOpacity(0)
        bump_btn2.setGraphicsEffect(opacity)

        # 문제
        self.begin = time.time()
        random_q2 = random.randint(0, 5)
        self.now_q = random_q2
        game_q_label2 = QLabel(self.game_q[random_q2], self.game2_background_lb)
        game_q_label2.setGeometry(385, 219, 510, 100)
        game_q_label2.setFont(QFont("나눔바른펜", 35))
        game_q_label2.setAlignment(Qt.AlignCenter)
        self.play_sounds[self.now_q+6].play(0)

        if random_q2 == 0:
            stop_btn2.clicked.connect(self.game_o)
            start_btn2.clicked.connect(self.game_x)
            left_btn2.clicked.connect(self.game_x)
            right_btn2.clicked.connect(self.game_x)
            back_btn2.clicked.connect(self.game_x)
            bump_btn2.clicked.connect(self.game_x)
        elif random_q2 == 1:
            stop_btn2.clicked.connect(self.game_x)
            start_btn2.clicked.connect(self.game_o)
            left_btn2.clicked.connect(self.game_x)
            right_btn2.clicked.connect(self.game_x)
            back_btn2.clicked.connect(self.game_x)
            bump_btn2.clicked.connect(self.game_x)
        elif random_q2 == 2:
            stop_btn2.clicked.connect(self.game_x)
            start_btn2.clicked.connect(self.game_x)
            left_btn2.clicked.connect(self.game_o)
            right_btn2.clicked.connect(self.game_x)
            back_btn2.clicked.connect(self.game_x)
            bump_btn2.clicked.connect(self.game_x)
        elif random_q2 == 3:
            stop_btn2.clicked.connect(self.game_x)
            start_btn2.clicked.connect(self.game_x)
            left_btn2.clicked.connect(self.game_x)
            right_btn2.clicked.connect(self.game_o)
            back_btn2.clicked.connect(self.game_x)
            bump_btn2.clicked.connect(self.game_x)
        elif random_q2 == 4:
            stop_btn2.clicked.connect(self.game_x)
            start_btn2.clicked.connect(self.game_x)
            left_btn2.clicked.connect(self.game_x)
            right_btn2.clicked.connect(self.game_x)
            back_btn2.clicked.connect(self.game_o)
            bump_btn2.clicked.connect(self.game_x)
        elif random_q2 == 5:
            stop_btn2.clicked.connect(self.game_x)
            start_btn2.clicked.connect(self.game_x)
            left_btn2.clicked.connect(self.game_x)
            right_btn2.clicked.connect(self.game_x)
            back_btn2.clicked.connect(self.game_x)
            bump_btn2.clicked.connect(self.game_o)
        self.main_start_background_lb.setVisible(False)
        self.game2_background_lb.setVisible(True)

    # 게임 페이지3
    def game3_buleung_buleunng(self, life_img):
        self.level = 3
        self.now_game_life = life_img
        # 게임 페이지 사진
        self.game3_background_lb = QLabel(self)
        game3_background_bg = QtGui.QPixmap(life_img)
        self.game3_background_lb.setFixedSize(1280, 800)
        self.game3_background_lb.setPixmap(game3_background_bg)

        # 정답 버튼
        stop_btn3 = QPushButton(self.game3_background_lb)
        stop_btn3.setGeometry(10, 380, 200, 200)
        opacity = QGraphicsOpacityEffect(stop_btn3)
        opacity.setOpacity(0)
        stop_btn3.setGraphicsEffect(opacity)

        start_btn3 = QPushButton(self.game3_background_lb)
        start_btn3.setGeometry(224, 576, 200, 200)
        opacity = QGraphicsOpacityEffect(start_btn3)
        opacity.setOpacity(0)
        start_btn3.setGraphicsEffect(opacity)

        left_btn3 = QPushButton(self.game3_background_lb)
        left_btn3.setGeometry(434, 380, 200, 200)
        opacity = QGraphicsOpacityEffect(left_btn3)
        opacity.setOpacity(0)
        left_btn3.setGraphicsEffect(opacity)

        right_btn3 = QPushButton(self.game3_background_lb)
        right_btn3.setGeometry(648, 576, 200, 200)
        opacity = QGraphicsOpacityEffect(right_btn3)
        opacity.setOpacity(0)
        right_btn3.setGraphicsEffect(opacity)

        back_btn3 = QPushButton(self.game3_background_lb)
        back_btn3.setGeometry(858, 380, 200, 200)
        opacity = QGraphicsOpacityEffect(back_btn3)
        opacity.setOpacity(0)
        back_btn3.setGraphicsEffect(opacity)

        bump_btn3 = QPushButton(self.game3_background_lb)
        bump_btn3.setGeometry(1072, 576, 200, 200)
        opacity = QGraphicsOpacityEffect(bump_btn3)
        opacity.setOpacity(0)
        bump_btn3.setGraphicsEffect(opacity)

        # 문제
        self.begin = time.time()
        random_q3 = random.randint(0, 5)
        self.now_q = random_q3
        game_q_label3 = QLabel(self.game_q[random_q3], self.game3_background_lb)
        game_q_label3.setGeometry(385, 219, 510, 100)
        game_q_label3.setFont(QFont("나눔바른펜", 35))
        game_q_label3.setAlignment(Qt.AlignCenter)
        self.play_sounds[self.now_q+6].play(0)

        if random_q3 == 0:
            stop_btn3.clicked.connect(self.game_o)
            start_btn3.clicked.connect(self.game_x)
            left_btn3.clicked.connect(self.game_x)
            right_btn3.clicked.connect(self.game_x)
            back_btn3.clicked.connect(self.game_x)
            bump_btn3.clicked.connect(self.game_x)
        elif random_q3 == 1:
            stop_btn3.clicked.connect(self.game_x)
            start_btn3.clicked.connect(self.game_o)
            left_btn3.clicked.connect(self.game_x)
            right_btn3.clicked.connect(self.game_x)
            back_btn3.clicked.connect(self.game_x)
            bump_btn3.clicked.connect(self.game_x)
        elif random_q3 == 2:
            stop_btn3.clicked.connect(self.game_x)
            start_btn3.clicked.connect(self.game_x)
            left_btn3.clicked.connect(self.game_o)
            right_btn3.clicked.connect(self.game_x)
            back_btn3.clicked.connect(self.game_x)
            bump_btn3.clicked.connect(self.game_x)
        elif random_q3 == 3:
            stop_btn3.clicked.connect(self.game_x)
            start_btn3.clicked.connect(self.game_x)
            left_btn3.clicked.connect(self.game_x)
            right_btn3.clicked.connect(self.game_o)
            back_btn3.clicked.connect(self.game_x)
            bump_btn3.clicked.connect(self.game_x)
        elif random_q3 == 4:
            stop_btn3.clicked.connect(self.game_x)
            start_btn3.clicked.connect(self.game_x)
            left_btn3.clicked.connect(self.game_x)
            right_btn3.clicked.connect(self.game_x)
            back_btn3.clicked.connect(self.game_o)
            bump_btn3.clicked.connect(self.game_x)
        elif random_q3 == 5:
            stop_btn3.clicked.connect(self.game_x)
            start_btn3.clicked.connect(self.game_x)
            left_btn3.clicked.connect(self.game_x)
            right_btn3.clicked.connect(self.game_x)
            back_btn3.clicked.connect(self.game_x)
            bump_btn3.clicked.connect(self.game_o)
        self.main_start_background_lb.setVisible(False)
        self.game3_background_lb.setVisible(True)

    # 게임 페이지4
    def game4_buleung_buleunng(self, life_img):
        self.level = 4
        self.now_game_life = life_img
        # 게임 페이지 사진
        self.game4_background_lb = QLabel(self)
        game4_background_bg = QtGui.QPixmap(life_img)
        self.game4_background_lb.setFixedSize(1280, 800)
        self.game4_background_lb.setPixmap(game4_background_bg)

        # 정답 버튼
        stop_btn4 = QPushButton(self.game4_background_lb)
        stop_btn4.setGeometry(10, 380, 200, 200)
        opacity = QGraphicsOpacityEffect(stop_btn4)
        opacity.setOpacity(0)
        stop_btn4.setGraphicsEffect(opacity)

        start_btn4 = QPushButton(self.game4_background_lb)
        start_btn4.setGeometry(224, 576, 200, 200)
        opacity = QGraphicsOpacityEffect(start_btn4)
        opacity.setOpacity(0)
        start_btn4.setGraphicsEffect(opacity)

        left_btn4 = QPushButton(self.game4_background_lb)
        left_btn4.setGeometry(434, 380, 200, 200)
        opacity = QGraphicsOpacityEffect(left_btn4)
        opacity.setOpacity(0)
        left_btn4.setGraphicsEffect(opacity)

        right_btn4 = QPushButton(self.game4_background_lb)
        right_btn4.setGeometry(648, 576, 200, 200)
        opacity = QGraphicsOpacityEffect(right_btn4)
        opacity.setOpacity(0)
        right_btn4.setGraphicsEffect(opacity)

        back_btn4 = QPushButton(self.game4_background_lb)
        back_btn4.setGeometry(858, 380, 200, 200)
        opacity = QGraphicsOpacityEffect(back_btn4)
        opacity.setOpacity(0)
        back_btn4.setGraphicsEffect(opacity)

        bump_btn4 = QPushButton(self.game4_background_lb)
        bump_btn4.setGeometry(1072, 576, 200, 200)
        opacity = QGraphicsOpacityEffect(bump_btn4)
        opacity.setOpacity(0)
        bump_btn4.setGraphicsEffect(opacity)

        # 문제
        self.begin = time.time()
        random_q4 = random.randint(0, 5)
        self.now_q = random_q4
        game_q_label4 = QLabel(self.game_q[random_q4], self.game4_background_lb)
        game_q_label4.setGeometry(385, 219, 510, 100)
        game_q_label4.setFont(QFont("나눔바른펜", 35))
        game_q_label4.setAlignment(Qt.AlignCenter)
        self.play_sounds[self.now_q+6].play(0)

        if random_q4 == 0:
            stop_btn4.clicked.connect(self.game_o)
            start_btn4.clicked.connect(self.game_x)
            left_btn4.clicked.connect(self.game_x)
            right_btn4.clicked.connect(self.game_x)
            back_btn4.clicked.connect(self.game_x)
            bump_btn4.clicked.connect(self.game_x)
        elif random_q4 == 1:
            stop_btn4.clicked.connect(self.game_x)
            start_btn4.clicked.connect(self.game_o)
            left_btn4.clicked.connect(self.game_x)
            right_btn4.clicked.connect(self.game_x)
            back_btn4.clicked.connect(self.game_x)
            bump_btn4.clicked.connect(self.game_x)
        elif random_q4 == 2:
            stop_btn4.clicked.connect(self.game_x)
            start_btn4.clicked.connect(self.game_x)
            left_btn4.clicked.connect(self.game_o)
            right_btn4.clicked.connect(self.game_x)
            back_btn4.clicked.connect(self.game_x)
            bump_btn4.clicked.connect(self.game_x)
        elif random_q4 == 3:
            stop_btn4.clicked.connect(self.game_x)
            start_btn4.clicked.connect(self.game_x)
            left_btn4.clicked.connect(self.game_x)
            right_btn4.clicked.connect(self.game_o)
            back_btn4.clicked.connect(self.game_x)
            bump_btn4.clicked.connect(self.game_x)
        elif random_q4 == 4:
            stop_btn4.clicked.connect(self.game_x)
            start_btn4.clicked.connect(self.game_x)
            left_btn4.clicked.connect(self.game_x)
            right_btn4.clicked.connect(self.game_x)
            back_btn4.clicked.connect(self.game_o)
            bump_btn4.clicked.connect(self.game_x)
        elif random_q4 == 5:
            stop_btn4.clicked.connect(self.game_x)
            start_btn4.clicked.connect(self.game_x)
            left_btn4.clicked.connect(self.game_x)
            right_btn4.clicked.connect(self.game_x)
            back_btn4.clicked.connect(self.game_x)
            bump_btn4.clicked.connect(self.game_o)
        self.main_start_background_lb.setVisible(False)
        self.game4_background_lb.setVisible(True)

    def game_o(self):
        end = time.time()
        result = round(end - self.begin, 1)
        if self.level == 1:
            self.play_sounds[self.now_q].play(0)
            time.sleep(1)
            if self.lv1_cnt >= 10:
                self.main_buleung_buleunng()
            else:
                self.lv1_cnt += 1
                self.game1_buleung_buleunng()
        elif self.level == 2:
            if result > 3.0:
                self.game_x()
            else:
                self.score += 10*result
                self.play_sounds[self.now_q].play(0)
                time.sleep(1)
                self.game2_buleung_buleunng(self.now_game_life)
        elif self.level == 3:
            if result > 2.0:
                self.game_x()
            else:
                self.score += 10*result
                self.play_sounds[self.now_q].play(0)
                time.sleep(1)
                self.game3_buleung_buleunng(self.now_game_life)
        elif self.level == 4:
            if result > 1.5:
                self.game_x()
            else:
                self.score += 10*result
                self.play_sounds[self.now_q].play(0)
                time.sleep(1)
                self.game4_buleung_buleunng(self.now_game_life)

    def game_x(self):
        self.game_life -= 1
        self.play_sounds[14].play(0)
        time.sleep(1)
        if self.level == 1:
            if self.lv1_cnt >= 10:
                self.main_buleung_buleunng()
            else:
                self.lv1_cnt += 1
                self.game1_buleung_buleunng()
        elif self.level == 2:
            if self.game_life == 2:
                self.game2_buleung_buleunng("images/game_life2.png")
            elif self.game_life == 1:
                self.game2_buleung_buleunng("images/game_life3.png")
            elif self.game_life == 0:
                self.end_game2_buleung_buleunng()
        elif self.level == 3:
            if self.game_life == 2:
                self.game3_buleung_buleunng("images/game_life2.png")
            elif self.game_life == 1:
                self.game3_buleung_buleunng("images/game_life3.png")
            elif self.game_life == 0:
                self.end_game3_buleung_buleunng()
        elif self.level == 4:
            if self.game_life == 2:
                self.game4_buleung_buleunng("images/game_life2.png")
            elif self.game_life == 1:
                self.game4_buleung_buleunng("images/game_life3.png")
            elif self.game_life == 0:
                self.end_game4_buleung_buleunng()

    # 레벨2 게임 끝 페이지
    def end_game2_buleung_buleunng(self):
        # 레벨2 게임 끝 페이지 사진
        self.end_game2_background_lb = QLabel(self)
        end_game2_background_bg = QtGui.QPixmap("images/game_end.png")
        self.end_game2_background_lb.setFixedSize(1280, 800)
        self.end_game2_background_lb.setPixmap(end_game2_background_bg)

        # 입력 확인 버튼
        input_ok_btn2 = QPushButton(self.end_game2_background_lb)
        input_ok_btn2.setGeometry(530, 590, 220, 100)
        opacity = QGraphicsOpacityEffect(input_ok_btn2)
        opacity.setOpacity(0)
        input_ok_btn2.setGraphicsEffect(opacity)
        input_ok_btn2.clicked.connect(self.rank2_buleung_buleunng)

        score_label2 = QLabel(str(int(self.score)), self.end_game2_background_lb)
        score_label2.setGeometry(650, 280, 200, 80)
        score_label2.setFont(QFont("나눔바른펜", 35))

        name_input2 = QLineEdit(self.end_game2_background_lb)
        name_input2.setGeometry(650, 417, 330, 90)
        name_input2.setFont(QFont("나눔바른펜", 35))
        name_input2.setStyleSheet("background-color: #E9FFFC;" "border-style: solid;" "border-width: 0px;")

        self.game2_background_lb.setVisible(False)
        self.end_game2_background_lb.setVisible(True)
        self.play_sounds[15].play(0)
    def rank2_buleung_buleunng(self):
        file = open("files/lv2_rank.csv", 'a', newline='', encoding="utf-8")
        write = csv.writer(file)
        print(self.name_input2.text())
        write.writerow([self.name_input2.text(), self.score])
        file.close()
        self.end_game2_background_lb.setVisible(False)
        self.rank2_buleung_bluleung()

    # 레벨3 게임 끝 페이지
    def end_game3_buleung_buleunng(self):
        # 레벨3 게임 끝 페이지 사진
        self.end_game3_background_lb = QLabel(self)
        end_game3_background_bg = QtGui.QPixmap("images/game_end.png")
        self.end_game3_background_lb.setFixedSize(1280, 800)
        self.end_game3_background_lb.setPixmap(end_game3_background_bg)

        # 입력 확인 버튼
        input_ok_btn3 = QPushButton(self.end_game3_background_lb)
        input_ok_btn3.setGeometry(530, 590, 220, 100)
        opacity = QGraphicsOpacityEffect(input_ok_btn3)
        opacity.setOpacity(0)
        input_ok_btn3.setGraphicsEffect(opacity)
        input_ok_btn3.clicked.connect(self.rank3_buleung_buleunng)

        score_label3 = QLabel(str(int(self.score)), self.end_game3_background_lb)
        score_label3.setGeometry(650, 280, 200, 80)
        score_label3.setFont(QFont("나눔바른펜", 35))

        name_input3 = QLineEdit(self.end_game3_background_lb)
        name_input3.setGeometry(650, 417, 330, 90)
        name_input3.setFont(QFont("나눔바른펜", 35))
        name_input3.setStyleSheet("background-color: #E9FFFC;" "border-style: solid;" "border-width: 0px;")

        self.game3_background_lb.setVisible(False)
        self.end_game3_background_lb.setVisible(True)
        self.play_sounds[15].play(0)
    def rank3_buleung_buleunng(self):
        file = open("files/lv3_rank.csv", 'a', newline='', encoding="utf-8")
        write = csv.writer(file)
        print(self.name_input3.text())
        write.writerow([self.name_input3.text(), self.score])
        file.close()
        self.end_game3_background_lb.setVisible(False)
        self.rank3_buleung_bluleung()

    # 레벨4 게임 끝 페이지
    def end_game4_buleung_buleunng(self):
        # 레벨4 게임 끝 페이지 사진
        self.end_game4_background_lb = QLabel(self)
        end_game4_background_bg = QtGui.QPixmap("images/game_end.png")
        self.end_game4_background_lb.setFixedSize(1280, 800)
        self.end_game4_background_lb.setPixmap(end_game4_background_bg)

        # 입력 확인 버튼
        input_ok_btn4 = QPushButton(self.end_game4_background_lb)
        input_ok_btn4.setGeometry(530, 590, 220, 100)
        opacity = QGraphicsOpacityEffect(input_ok_btn4)
        opacity.setOpacity(0)
        input_ok_btn4.setGraphicsEffect(opacity)
        input_ok_btn4.clicked.connect(self.rank4_buleung_buleunng)

        score_label4 = QLabel(str(int(self.score)), self.end_game4_background_lb)
        score_label4.setGeometry(650, 280, 200, 80)
        score_label4.setFont(QFont("나눔바른펜", 35))

        name_input4 = QLineEdit(self.end_game4_background_lb)
        name_input4.setGeometry(650, 417, 330, 90)
        name_input4.setFont(QFont("나눔바른펜", 35))
        name_input4.setStyleSheet("background-color: #E9FFFC;" "border-style: solid;" "border-width: 0px;")

        self.game4_background_lb.setVisible(False)
        self.end_game4_background_lb.setVisible(True)
        self.play_sounds[15].play(0)
    def rank4_buleung_buleunng(self):
        file = open("files/lv4_rank.csv", 'a', newline='', encoding="utf-8")
        write = csv.writer(file)
        print(self.name_input4.text())
        write.writerow([self.name_input4.text(), self.score])
        file.close()
        self.end_game4_background_lb.setVisible(False)
        self.rank4_buleung_bluleung()

    # 게임 방법 페이지
    def rule_notice(self):
        # 게임 방법 페이지 사진
        self.main_rule_background_lb = QLabel(self)
        main_rule_background_bg = QtGui.QPixmap("images/main_rule_notice.png")
        self.main_rule_background_lb.setFixedSize(1280, 800)
        self.main_rule_background_lb.setPixmap(main_rule_background_bg)

        # 취소 버튼
        rule_exit_btn = QPushButton(self.main_rule_background_lb)
        rule_exit_btn.setGeometry(1100, 80, 60, 60)
        opacity = QGraphicsOpacityEffect(rule_exit_btn)
        opacity.setOpacity(0)
        rule_exit_btn.setGraphicsEffect(opacity)
        rule_exit_btn.clicked.connect(self.go_rule_main_buleung_buleunng)

        self.main_background_lb.setVisible(False)
        self.main_rule_background_lb.setVisible(True)

    def go_rule_main_buleung_buleunng(self):
        self.main_background_lb.setVisible(True)
        self.main_rule_background_lb.setVisible(False)

    # 순위 난이도 선택 페이지
    def rank_choice(self):
        # 순위 난이도 선택 페이지 사진
        self.main_rank_background_lb = QLabel(self)
        main_rank_background_bg = QtGui.QPixmap("images/main_rank_choice.png")
        self.main_rank_background_lb.setFixedSize(1280, 800)
        self.main_rank_background_lb.setPixmap(main_rank_background_bg)

        # 취소 버튼
        rank_exit_btn = QPushButton(self.main_rank_background_lb)
        rank_exit_btn.setGeometry(920, 255, 60, 60)
        opacity = QGraphicsOpacityEffect(rank_exit_btn)
        opacity.setOpacity(0)
        rank_exit_btn.setGraphicsEffect(opacity)
        rank_exit_btn.clicked.connect(self.go_rank_main_buleung_buleunng)

        # 난이도 2 선택 버튼
        rank_lv2_btn = QPushButton(self.main_rank_background_lb)
        rank_lv2_btn.setGeometry(370, 385, 140, 140)
        opacity = QGraphicsOpacityEffect(rank_lv2_btn)
        opacity.setOpacity(0)
        rank_lv2_btn.setGraphicsEffect(opacity)
        rank_lv2_btn.clicked.connect(self.go_rank_lv2)

        # 난이도 3 선택 버튼
        rank_lv3_btn = QPushButton(self.main_rank_background_lb)
        rank_lv3_btn.setGeometry(570, 385, 140, 140)
        opacity = QGraphicsOpacityEffect(rank_lv3_btn)
        opacity.setOpacity(0)
        rank_lv3_btn.setGraphicsEffect(opacity)
        rank_lv3_btn.clicked.connect(self.go_rank_lv3)

        # 난이도 4 선택 버튼
        rank_lv4_btn = QPushButton(self.main_rank_background_lb)
        rank_lv4_btn.setGeometry(770, 385, 140, 140)
        opacity = QGraphicsOpacityEffect(rank_lv4_btn)
        opacity.setOpacity(0)
        rank_lv4_btn.setGraphicsEffect(opacity)
        rank_lv4_btn.clicked.connect(self.go_rank_lv4)

        self.main_background_lb.setVisible(False)
        self.main_rank_background_lb.setVisible(True)

    def go_rank_main_buleung_buleunng(self):
        self.main_background_lb.setVisible(True)
        self.main_rank_background_lb.setVisible(False)

    def go_rank_lv2(self):
        self.main_rank_background_lb.setVisible(False)
        self.rank2_buleung_bluleung()

    def go_rank_lv3(self):
        self.main_rank_background_lb.setVisible(False)
        self.rank3_buleung_bluleung()

    def go_rank_lv4(self):
        self.main_rank_background_lb.setVisible(False)
        self.rank4_buleung_bluleung()

    # 난이도 2 랭크 페이지
    def rank2_buleung_bluleung(self):
        # 난이도 2 랭크 페이지 사진
        self.rank2_background_lb = QLabel(self)
        rank2_background_bg = QtGui.QPixmap("images/main_rank2.png")
        self.rank2_background_lb.setFixedSize(1280, 800)
        self.rank2_background_lb.setPixmap(rank2_background_bg)

        # 취소 버튼
        rank2_exit_btn = QPushButton(self.rank2_background_lb)
        rank2_exit_btn.setGeometry(1100, 80, 60, 60)
        opacity = QGraphicsOpacityEffect(rank2_exit_btn)
        opacity.setOpacity(0)
        rank2_exit_btn.setGraphicsEffect(opacity)
        rank2_exit_btn.clicked.connect(self.go_rank2_main_buleung_buleunng)

        df = pd.read_csv("files/lv2_rank.csv")
        df = df.sort_values(by=['score'], ignore_index = True, ascending = False)

        self.rank_name = df.iloc[0,1]
        self.rank_score = df.iloc[0,2]
        self.rank_value = self.rank_name + "\t" + self.rank_score
        rank21_label = QLabel(self.rank_value, self.rank2_background_lb)
        rank21_label.setGeometry(220, 200, 350, 60)
        rank21_label.setFont(QFont("나눔바른펜", 35))

        self.rank_name = df.iloc[1,1]
        self.rank_score = df.iloc[1,2]
        self.rank_value = self.rank_name + "\t" + self.rank_score
        rank22_label = QLabel(self.rank_value, self.rank2_background_lb)
        rank22_label.setGeometry(220, 305, 350, 60)
        rank22_label.setFont(QFont("나눔바른펜", 35))

        self.rank_name = df.iloc[2,1]
        self.rank_score = df.iloc[2,2]
        self.rank_value = self.rank_name + "\t" + self.rank_score
        rank23_label = QLabel(self.rank_value, self.rank2_background_lb)
        rank23_label.setGeometry(220, 410, 350, 60)
        rank23_label.setFont(QFont("나눔바른펜", 35))

        self.rank_name = df.iloc[3,1]
        self.rank_score = df.iloc[3,2]
        self.rank_value = self.rank_name + "\t" + self.rank_score
        rank24_label = QLabel(self.rank_value, self.rank2_background_lb)
        rank24_label.setGeometry(220, 515, 350, 60)
        rank24_label.setFont(QFont("나눔바른펜", 35))

        self.rank_name = df.iloc[4,1]
        self.rank_score = df.iloc[4,2]
        self.rank_value = self.rank_name + "\t" + self.rank_score
        rank25_label = QLabel(self.rank_value, self.rank2_background_lb)
        rank25_label.setGeometry(220, 620, 350, 60)
        rank25_label.setFont(QFont("나눔바른펜", 35))

        self.rank_name = df.iloc[5,1]
        self.rank_score = df.iloc[5,2]
        self.rank_value = self.rank_name + "\t" + self.rank_score
        rank26_label = QLabel(self.rank_value, self.rank2_background_lb)
        rank26_label.setGeometry(720, 200, 350, 60)
        rank26_label.setFont(QFont("나눔바른펜", 35))

        self.rank_name = df.iloc[6,1]
        self.rank_score = df.iloc[6,2]
        self.rank_value = self.rank_name + "\t" + self.rank_score
        rank27_label = QLabel(self.rank_value, self.rank2_background_lb)
        rank27_label.setGeometry(720, 305, 350, 60)
        rank27_label.setFont(QFont("나눔바른펜", 35))

        self.rank_name = df.iloc[7,1]
        self.rank_score = df.iloc[7,2]
        self.rank_value = self.rank_name + "\t" + self.rank_score
        rank28_label = QLabel(self.rank_value, self.rank2_background_lb)
        rank28_label.setGeometry(720, 410, 350, 60)
        rank28_label.setFont(QFont("나눔바른펜", 35))

        self.rank_name = df.iloc[8,1]
        self.rank_score = df.iloc[8,2]
        self.rank_value = self.rank_name + "\t" + self.rank_score
        rank29_label = QLabel(self.rank_value, self.rank2_background_lb)
        rank29_label.setGeometry(720, 515, 350, 60)
        rank29_label.setFont(QFont("나눔바른펜", 35))

        self.rank_name = df.iloc[9,1]
        self.rank_score = df.iloc[9,2]
        self.rank_value = self.rank_name + "\t" + self.rank_score
        rank20_label = QLabel(self.rank_value, self.rank2_background_lb)
        rank20_label.setGeometry(760, 620, 350, 60)
        rank20_label.setFont(QFont("나눔바른펜", 35))

        self.rank2_background_lb.setVisible(True)
    def go_rank2_main_buleung_buleunng(self):
        self.rank2_background_lb.setVisible(False)
        self.main_buleung_buleunng()


    # 난이도 3 랭크 페이지
    def rank3_buleung_bluleung(self):
        # 난이도 3 랭크 페이지 사진
        self.rank3_background_lb = QLabel(self)
        rank3_background_bg = QtGui.QPixmap("images/main_rank3.png")
        self.rank3_background_lb.setFixedSize(1280, 800)
        self.rank3_background_lb.setPixmap(rank3_background_bg)

        # 취소 버튼
        rank3_exit_btn = QPushButton(self.rank3_background_lb)
        rank3_exit_btn.setGeometry(1100, 80, 60, 60)
        opacity = QGraphicsOpacityEffect(rank3_exit_btn)
        opacity.setOpacity(0)
        rank3_exit_btn.setGraphicsEffect(opacity)
        rank3_exit_btn.clicked.connect(self.go_rank3_main_buleung_buleunng)

        df = pd.read_csv("files/lv3_rank.csv")
        df = df.sort_values(by=['score'], ignore_index = True, ascending = False)

        self.rank_name = df.iloc[0,1]
        self.rank_score = df.iloc[0,2]
        self.rank_value = self.rank_name + "\t" + self.rank_score
        rank31_label = QLabel(self.rank_value, self.rank3_background_lb)
        rank31_label.setGeometry(220, 200, 350, 60)
        rank31_label.setFont(QFont("나눔바른펜", 35))

        self.rank_name = df.iloc[1,1]
        self.rank_score = df.iloc[1,2]
        self.rank_value = self.rank_name + "\t" + self.rank_score
        rank32_label = QLabel(self.rank_value, self.rank3_background_lb)
        rank32_label.setGeometry(220, 305, 350, 60)
        rank32_label.setFont(QFont("나눔바른펜", 35))

        self.rank_name = df.iloc[2,1]
        self.rank_score = df.iloc[2,2]
        self.rank_value = self.rank_name + "\t" + self.rank_score
        rank33_label = QLabel(self.rank_value, self.rank3_background_lb)
        rank33_label.setGeometry(220, 410, 350, 60)
        rank33_label.setFont(QFont("나눔바른펜", 35))

        self.rank_name = df.iloc[3,1]
        self.rank_score = df.iloc[3,2]
        self.rank_value = self.rank_name + "\t" + self.rank_score
        rank34_label = QLabel(self.rank_value, self.rank3_background_lb)
        rank34_label.setGeometry(220, 515, 350, 60)
        rank34_label.setFont(QFont("나눔바른펜", 35))

        self.rank_name = df.iloc[4,1]
        self.rank_score = df.iloc[4,2]
        self.rank_value = self.rank_name + "\t" + self.rank_score
        rank35_label = QLabel(self.rank_value, self.rank3_background_lb)
        rank35_label.setGeometry(220, 620, 350, 60)
        rank35_label.setFont(QFont("나눔바른펜", 35))

        self.rank_name = df.iloc[5,1]
        self.rank_score = df.iloc[5,2]
        self.rank_value = self.rank_name + "\t" + self.rank_score
        rank36_label = QLabel(self.rank_value, self.rank3_background_lb)
        rank36_label.setGeometry(720, 200, 350, 60)
        rank36_label.setFont(QFont("나눔바른펜", 35))

        self.rank_name = df.iloc[6,1]
        self.rank_score = df.iloc[6,2]
        self.rank_value = self.rank_name + "\t" + self.rank_score
        rank37_label = QLabel(self.rank_value, self.rank3_background_lb)
        rank37_label.setGeometry(720, 305, 350, 60)
        rank37_label.setFont(QFont("나눔바른펜", 35))

        self.rank_name = df.iloc[7,1]
        self.rank_score = df.iloc[7,2]
        self.rank_value = self.rank_name + "\t" + self.rank_score
        rank38_label = QLabel(self.rank_value, self.rank3_background_lb)
        rank38_label.setGeometry(720, 410, 350, 60)
        rank38_label.setFont(QFont("나눔바른펜", 35))

        self.rank_name = df.iloc[8,1]
        self.rank_score = df.iloc[8,2]
        self.rank_value = self.rank_name + "\t" + self.rank_score
        rank39_label = QLabel(self.rank_value, self.rank3_background_lb)
        rank39_label.setGeometry(720, 515, 350, 60)
        rank39_label.setFont(QFont("나눔바른펜", 35))

        self.rank_name = df.iloc[9,1]
        self.rank_score = df.iloc[9,2]
        self.rank_value = self.rank_name + "\t" + self.rank_score
        rank30_label = QLabel(self.rank_value, self.rank3_background_lb)
        rank30_label.setGeometry(760, 620, 350, 60)
        rank30_label.setFont(QFont("나눔바른펜", 35))

        self.rank3_background_lb.setVisible(True)
    def go_rank3_main_buleung_buleunng(self):
        self.rank3_background_lb.setVisible(False)
        self.main_buleung_buleunng()

    # 난이도 4 랭크 페이지
    def rank4_buleung_bluleung(self):
        # 난이도 4 랭크 페이지 사진
        self.rank4_background_lb = QLabel(self)
        rank4_background_bg = QtGui.QPixmap("images/main_rank4.png")
        self.rank4_background_lb.setFixedSize(1280, 800)
        self.rank4_background_lb.setPixmap(rank4_background_bg)

        # 취소 버튼
        rank4_exit_btn = QPushButton(self.rank4_background_lb)
        rank4_exit_btn.setGeometry(1100, 80, 60, 60)
        opacity = QGraphicsOpacityEffect(rank4_exit_btn)
        opacity.setOpacity(0)
        rank4_exit_btn.setGraphicsEffect(opacity)
        rank4_exit_btn.clicked.connect(self.go_rank4_main_buleung_buleunng)

        df = pd.read_csv("files/lv4_rank.csv")
        df = df.sort_values(by=['score'], ignore_index = True, ascending = False)

        self.rank_name = df.iloc[0,1]
        self.rank_score = df.iloc[0,2]
        self.rank_value = self.rank_name + "\t" + self.rank_score
        rank41_label = QLabel(self.rank_value, self.rank4_background_lb)
        rank41_label.setGeometry(220, 200, 350, 60)
        rank41_label.setFont(QFont("나눔바른펜", 35))

        self.rank_name = df.iloc[1,1]
        self.rank_score = df.iloc[1,2]
        self.rank_value = self.rank_name + "\t" + self.rank_score
        rank42_label = QLabel(self.rank_value, self.rank4_background_lb)
        rank42_label.setGeometry(220, 305, 350, 60)
        rank42_label.setFont(QFont("나눔바른펜", 35))

        self.rank_name = df.iloc[2,1]
        self.rank_score = df.iloc[2,2]
        self.rank_value = self.rank_name + "\t" + self.rank_score
        rank43_label = QLabel(self.rank_value, self.rank4_background_lb)
        rank43_label.setGeometry(220, 410, 350, 60)
        rank43_label.setFont(QFont("나눔바른펜", 35))

        self.rank_name = df.iloc[3,1]
        self.rank_score = df.iloc[3,2]
        self.rank_value = self.rank_name + "\t" + self.rank_score
        rank44_label = QLabel(self.rank_value, self.rank4_background_lb)
        rank44_label.setGeometry(220, 515, 350, 60)
        rank44_label.setFont(QFont("나눔바른펜", 35))

        self.rank_name = df.iloc[4,1]
        self.rank_score = df.iloc[4,2]
        self.rank_value = self.rank_name + "\t" + self.rank_score
        rank45_label = QLabel(self.rank_value, self.rank4_background_lb)
        rank45_label.setGeometry(220, 620, 350, 60)
        rank45_label.setFont(QFont("나눔바른펜", 35))

        self.rank_name = df.iloc[5,1]
        self.rank_score = df.iloc[5,2]
        self.rank_value = self.rank_name + "\t" + self.rank_score
        rank46_label = QLabel(self.rank_value, self.rank4_background_lb)
        rank46_label.setGeometry(720, 200, 350, 60)
        rank46_label.setFont(QFont("나눔바른펜", 35))

        self.rank_name = df.iloc[6,1]
        self.rank_score = df.iloc[6,2]
        self.rank_value = self.rank_name + "\t" + self.rank_score
        rank47_label = QLabel(self.rank_value, self.rank4_background_lb)
        rank47_label.setGeometry(720, 305, 350, 60)
        rank47_label.setFont(QFont("나눔바른펜", 35))

        self.rank_name = df.iloc[7,1]
        self.rank_score = df.iloc[7,2]
        self.rank_value = self.rank_name + "\t" + self.rank_score
        rank48_label = QLabel(self.rank_value, self.rank4_background_lb)
        rank48_label.setGeometry(720, 410, 350, 60)
        rank48_label.setFont(QFont("나눔바른펜", 35))

        self.rank_name = df.iloc[8,1]
        self.rank_score = df.iloc[8,2]
        self.rank_value = self.rank_name + "\t" + self.rank_score
        rank49_label = QLabel(self.rank_value, self.rank4_background_lb)
        rank49_label.setGeometry(720, 515, 350, 60)
        rank49_label.setFont(QFont("나눔바른펜", 35))

        self.rank_name = df.iloc[9,1]
        self.rank_score = df.iloc[9,2]
        self.rank_value = self.rank_name + "\t" + self.rank_score
        rank40_label = QLabel(self.rank_value, self.rank4_background_lb)
        rank40_label.setGeometry(760, 620, 350, 60)
        rank40_label.setFont(QFont("나눔바른펜", 35))

        self.rank4_background_lb.setVisible(True)
    def go_rank4_main_buleung_buleunng(self):
        self.rank4_background_lb.setVisible(False)
        self.main_buleung_buleunng()

    # ESC키 누를 시 동작
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.main_buleung_buleunng()

    # 화면 중간에 표시
    def center(self):
        window_xy = self.frameGeometry()
        center_xy = QDesktopWidget().availableGeometry().center()
        window_xy.moveCenter(center_xy)
        self.move(window_xy.topLeft())

    # 프로그램 종료 시
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '게임 종료', '新부릉부릉을 종료하시겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


# 프로그램 실행
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = BuleungBuleung()
    sys.exit(app.exec_())
from PyQt5.QtWidgets import (QPushButton, QRadioButton, QLabel,
                              QSpinBox, QGroupBox, QButtonGroup,
                                QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import Qt

btn_menu = QPushButton('Меню')
btn_rest = QPushButton('Відпочити')
spin = QSpinBox()
spin.setValue(30)

menu_main_line = QVBoxLayout()

menu_btn1 = QPushButton('Розпочати тестування')
menu_btn2 = QPushButton('Розпочати навчання')
menu_btn3 = QPushButton('Вийти')
menu_main_line.addWidget(menu_btn1)
menu_main_line.addWidget(menu_btn2)
menu_main_line.addWidget(menu_btn3)

learn_main_line = QVBoxLayout()

learn_btn_menu = QPushButton('Меню')
learn_main_line.addWidget(learn_btn_menu)

quest_lb = QLabel('Яблуко')
rbGroupBox = QGroupBox('Варіанти відповіді')
btn_ans = QPushButton('Відповісти')
button_group = QButtonGroup()

rb1 = QRadioButton('1')
rb2 = QRadioButton('2')
rb3 = QRadioButton('3')
rb4 = QRadioButton('4')
rbuttons = [rb1, rb2, rb3, rb4]
button_group.addButton(rbuttons[0])
button_group.addButton(rbuttons[1])
button_group.addButton(rbuttons[2])
button_group.addButton(rbuttons[3])

main_box_line = QHBoxLayout()
box_line1  = QVBoxLayout()
box_line2  = QVBoxLayout()

box_line1.addWidget(rbuttons[0])
box_line2.addWidget(rbuttons[1])
box_line1.addWidget(rbuttons[2])
box_line2.addWidget(rbuttons[3])

main_box_line.addLayout(box_line1)
main_box_line.addLayout(box_line2)
rbGroupBox.setLayout(main_box_line)

ansGroupBox = QGroupBox('Результати теста')
main_box2_line = QVBoxLayout()
result_lb = QLabel('Правильно')
right_ans_lb = QLabel()
main_box2_line.addWidget(result_lb, alignment=Qt.AlignTop)
main_box2_line.addWidget(right_ans_lb, alignment=Qt.AlignCenter)
ansGroupBox.setLayout(main_box2_line)
ansGroupBox.hide()

main_line_quiz = QVBoxLayout()
line1_quiz = QHBoxLayout()
line1_quiz.addWidget(btn_menu)
line1_quiz.addStretch(1)
line1_quiz.addWidget(btn_rest)
line1_quiz.addWidget(spin)
line1_quiz.addWidget(QLabel('хвилин'))

main_line_quiz.addLayout(line1_quiz, stretch=1)
main_line_quiz.addWidget(quest_lb, alignment=Qt.AlignCenter, stretch=1)
main_line_quiz.addWidget(rbGroupBox, stretch=5)
main_line_quiz.addWidget(ansGroupBox, stretch=5)
main_line_quiz.addWidget(btn_ans, stretch=1)

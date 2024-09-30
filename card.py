from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from random import shuffle

app = QApplication([])

from layout_quiz import *
from questions import *

i = 0

true_score = 0

window = QWidget()
window.resize(600, 500)
window.setWindowTitle('Memory Card')
window.setLayout(main_line_quiz)
window.show()
shuffle(questions)
shuffle(rbuttons)
questions[i].show_q(quest_lb, rbuttons)

window.hide()

def click_ok():
    global i
    global rbuttons
    global true_score

    if btn_ans.text() == 'Відповісти':
        rbGroupBox.hide()
        ansGroupBox.show()
        right_ans_lb.setText(rbuttons[0].text())
        btn_ans.setText('Наступне питання')
        if rbuttons[0].isChecked():
            result_lb.setText('Правильно')
            true_score += 1
        else:
            result_lb.setText('Неправильно')
    else:
        if i >= len(questions) - 1:
            window.hide()

            grade = true_score / 20 * 12

            score = QMessageBox()
            score.setWindowTitle('Memory Card')
            score.setText(f'Ти завершив тест!\nКількість правильних відповідей: {true_score}\nОцінка: {round(grade, 1)}')
            score.exec()

        else:
            shuffle(rbuttons)
            rbGroupBox.show()
            ansGroupBox.hide()
            btn_ans.setText('Відповісти')
            i += 1
            
            questions[i].show_q(quest_lb, rbuttons)
    
btn_ans.clicked.connect(click_ok)

menu = QApplication([])
menu_window = QWidget()
menu_window.resize(300, 150)
menu_window.setWindowTitle('Memory Card Menu')
menu_window.setLayout(menu_main_line)

learn = QApplication([])
learn_window = QWidget()
learn_window.resize(400, 700)
learn_window.setWindowTitle('Memory Card Learning')
learn_window.setLayout(learn_main_line)

learn_window.hide()
menu_window.show()

def menu_act():
    window.hide()
    menu_window.show()

def menu1_act():
    menu_window.hide()
    window.show()

def menu2_act():
    menu_window.hide()
    learn_window.show()

def learn_menu_act():
    learn_window.hide()
    menu_window.show()

def exit():
    app.exit()

btn_menu.clicked.connect(menu_act)
menu_btn1.clicked.connect(menu1_act)
menu_btn2.clicked.connect(menu2_act)
menu_btn3.clicked.connect(exit)
learn_btn_menu.clicked.connect(learn_menu_act)

app.exec()
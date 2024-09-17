from PyQt5.QtWidgets import QApplication, QWidget
from random import shuffle

app = QApplication([])

from layout_quiz import *
from questions import *

i = 0

window = QWidget()
window.resize(600, 500)
window.setWindowTitle('Memory Card')
window.setLayout(main_line_quiz)
window.show()
shuffle(questions)
questions[i].show_q(quest_lb, rb1, rb2, rb3, rb4)

def click_ok():
    global i
    if btn_ans.text() == 'Відповісти':
        rbGroupBox.hide()
        ansGroupBox.show()
        right_ans_lb.setText(rb1.text())
        btn_ans.setText('Наступне питання')
        if rb1.isChecked():
            result_lb.setText('Правильно')
        else:
            result_lb.setText('Неправильно')
    else:
        rbGroupBox.show()
        ansGroupBox.hide()
        btn_ans.setText('Відповісти')
        i += 1
        try:
            questions[i].show_q(quest_lb, rb1, rb2, rb3, rb4)
        except:
            app.exit()# prob do a counter here or some shi

    
btn_ans.clicked.connect(click_ok)

menu = QApplication([])
menu_window = QWidget()
menu_window.resize(300, 150)
menu_window.setWindowTitle('Меню')
menu_window.setLayout(menu_main_line)

window.hide()
menu_window.show()

def menu_act():
    menu_window.show()
    window.hide()

def menu1_act():
    window.show()
    menu_window.hide()

def exit():
    app.exit()

btn_menu.clicked.connect(menu_act)
menu_btn1.clicked.connect(menu1_act)
menu_btn3.clicked.connect(exit)

app.exec()
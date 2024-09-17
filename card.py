from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication([])

from layout_quiz import *

window = QWidget()
window.resize(600, 500)
window.setWindowTitle('Memory Card')
window.setLayout(main_line_quiz)
window.show()

def click_ok():
    if btn_ans.text() == 'Відповісти':
        rbGroupBox.hide()
        ansGroupBox.show()
        btn_ans.setText('Наступне питання')
    else:
        rbGroupBox.show()
        ansGroupBox.hide()
        btn_ans.setText('Відповісти')
    
btn_ans.clicked.connect(click_ok)

menu = QApplication([])
menu_window = QWidget()
menu_window.resize(200, 100)
menu_window.setWindowTitle('Меню')
menu_window.setLayout(menu_main_line)

def menu_act():
    menu_window.show()

btn_menu.clicked.connect(menu_act)



app.exec()
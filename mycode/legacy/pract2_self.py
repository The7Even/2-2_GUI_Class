import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import QThread, Qt, pyqtSignal
from PyQt5.QtGui import QPixmap

app = QApplication(sys.argv)

class AutoHateThread(QThread):
    tick_signal = pyqtSignal()

    def run(self):
        while True:
            time.sleep(1)
            self.tick_signal.emit()

def update_ui_text():
    if Lbl3.isHidden():
        Lbl3.show()
        
    text = f"Hate Monday Counter : {hate_monday_count}"
    if hate_rate > 1:
        text += f" | Hate Rate : {hate_rate}"
    if auto_hate > 0:
        text += f" | Auto Hate : {auto_hate}/s"
    Lbl3.setText(text)

    if hate_monday_count >= 100 or auto_hate > 0:
        window2.setFixedSize(400, 200)
    elif hate_monday_count >= 20 or hate_rate > 1:
        window2.setFixedSize(400, 150)

    if hate_monday_count >= 2147483648:
        Lbl3.setText("STOP hating Monday")
        window2.setFixedSize(400, 100)
        Lbl2.setText("We love Monday")
        Button1.hide()
        

def on_click():
    if Lbl3.isHidden():
        Lbl3.show()
    
    global hate_monday_count
    global hate_rate
    hate_monday_count += hate_rate
    update_ui_text()

def upgrade_hate():
    global hate_rate
    global hate_monday_count
    global rate_cost
    if hate_monday_count >= rate_cost:
        hate_monday_count -= rate_cost
        hate_rate *= 2
        rate_cost *= 2
        Lbl4.setText(f"Hate Rate Price : {rate_cost}")
        update_ui_text()

def upgrade_auto():
    global hate_monday_count
    global hate_rate
    global auto_hate
    global auto_cost
    if hate_monday_count >= auto_cost:
        hate_monday_count -= auto_cost
        auto_hate += 1
        auto_cost += 100
        Lbl6.setText(f"Auto Hate Price : {auto_cost}")
        update_ui_text()

def on_auto_tick():
    global hate_monday_count
    global auto_hate
    if auto_hate > 0:
        hate_monday_count += auto_hate
        update_ui_text()

def new_window():
    global hate_rate
    if Ledit1.text() == "Monday":
        window3.show()

    if Ledit1.text() == "Sunday":
        global grant
        if grant == 0:
            Lbl5.setText("Sunday is Best. Bonus Granted.")
            hate_rate *= 1000
            grant = 1
            update_ui_text()

def change_Label():
    Lbl5.setText(Ledit1.text())

def Clear_Label():
    Lbl5.setText("You have successfully entered Monday.")
    Ledit1.clear()

hate_monday_count = 0
hate_rate = 1
auto_hate = 0
rate_cost = 20
auto_cost = 100
grant = 0

window1 = QWidget()
window1.setWindowTitle("1st Window")
window1.setStyleSheet("background-color: black;")
window1.setFixedSize(400, 300)

window2 = QWidget()
window2.setWindowTitle("2nd Window")
window2.setStyleSheet("background-color: white;")
window2.setFixedSize(400, 100)

Lbl1 = QLabel("9/14 Monday.", window1)
Lbl1.resize(400, 100)
Lbl1.setStyleSheet("font-family: 'SUIT ExtraBold'; font-size: 28px; color: white;")
Lbl1.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft)

Lbl2 = QLabel("We hate Monday.", window2)
Lbl2.resize(400, 100)
Lbl2.setStyleSheet("font-family: 'SUIT ExtraBold'; font-size: 28px; color: black; background-color: transparent;")
Lbl2.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)

Lbl3 = QLabel("Hate Monday Counter : 0", window2)
Lbl3.resize(400, 100)
Lbl3.setStyleSheet("font-family: 'SUIT ExtraBold'; font-size: 12px; color: black; background-color: transparent;")
Lbl3.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft)
Lbl3.hide()

Lbl4 = QLabel("Hate Rate Price : 20", window2)
Lbl4.resize(400, 150)
Lbl4.setStyleSheet("font-family: 'SUIT ExtraBold'; font-size: 14px; color: black; background-color: transparent;")
Lbl4.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight)

Lbl6 = QLabel("Auto Hate Price : 100", window2)
Lbl6.resize(400, 200)
Lbl6.setStyleSheet("font-family: 'SUIT ExtraBold'; font-size: 14px; color: black; background-color: transparent;")
Lbl6.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)

Ledit1 = QLineEdit(window1)
Ledit1.resize(400, 20)
Ledit1.setStyleSheet("font-family: 'SUIT'; font-size: 14px; color: black; background-color: white;")
Ledit1.setPlaceholderText("Enter Monday.")

Button1 = QPushButton("Hate Monday Button", window2)
Button1.setStyleSheet("background-color: black; color: white; font-family: 'SUIT'; font-size: 16px;")
Button1.move(100,40)
Button1.resize(200, 20)
Button1.clicked.connect(on_click)

Button2 = QPushButton("Upgrade Hate Rate", window2)
Button2.setStyleSheet("background-color: black; color: white; font-family: 'SUIT'; font-size: 16px;")
Button2.move(10, 110)
Button2.resize(180, 30)
Button2.clicked.connect(upgrade_hate)

Button3 = QPushButton("Auto Hate Monday", window2)
Button3.setStyleSheet("background-color: black; color: white; font-family: 'SUIT'; font-size: 16px;")
Button3.move(10, 160)
Button3.resize(180, 30)
Button3.clicked.connect(upgrade_auto)

window1.show()
window2.show()

window3 = QWidget()
window3.setWindowTitle("3rd Window")
window3.setFixedSize(600, 100)
window3.setStyleSheet("background-color: white;")

Lbl5 = QLabel("You have successfully entered Monday.", window3)
Lbl5.resize(600, 60)
Lbl5.setStyleSheet("font-family: 'SUIT ExtraBold'; font-size: 28px; color: black; background-color: transparent;")
Lbl5.setAlignment(Qt.AlignmentFlag.AlignCenter)

Button4 = QPushButton("Change Label", window3)
Button4.setStyleSheet("background-color: black; color: white; font-family: 'SUIT'; font-size: 16px;")
Button4.move(50, 60)
Button4.resize(200, 30)
Button4.clicked.connect(change_Label)

Button5 = QPushButton("Clear", window3)
Button5.setStyleSheet("background-color: black; color: white; font-family: 'SUIT'; font-size: 16px;")
Button5.move(350, 60)
Button5.resize(200, 30)
Button5.clicked.connect(Clear_Label)

Ledit1.returnPressed.connect(new_window)

auto_thread = AutoHateThread()
auto_thread.tick_signal.connect(on_auto_tick)
auto_thread.start()

pixmap = QPixmap(r"C:\Users\USER\Desktop\KIT\26-02 files\GUI Programming\1st\mycode\image.png")
image_Label = QLabel(window1)
image_Label.setPixmap(pixmap)
image_Label.setGeometry(0, 100, 400, 200)
image_Label.setScaledContents(True)
image_Label.show()

sys.exit(app.exec_())
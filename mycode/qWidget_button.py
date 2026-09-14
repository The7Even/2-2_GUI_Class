import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtCore import Qt

pressbutton = 0

def on_click():
    global pressbutton
    pressbutton += 1
    print(f"버튼이 {pressbutton}회 눌렸습니다.")

    if pressbutton == 10:
        print("버튼이 너무 아파해서 도망갔습니다.")
        button.hide()

app = QApplication(sys.argv)
window = QWidget()
window.resize(300,50)

button = QPushButton("확인", window)
button.clicked.connect(on_click)


window.show()
sys.exit(app.exec())
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

from PyQt5.QtGui import QPixmap

from pathlib import Path

number = 1

def change():
    global number
    if number == 1:
        number = 2
    else:
        number = 1
    update()
    

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("실습 2 - 사용자 정보 입력")
window.setFixedSize(450, 350)


image_label = QLabel(window)
image_label.setGeometry(100, 50, 300, 400) # 위치 (100, 50), 크기 300x400
image_label.setScaledContents(True)

def update():
    img_path = Path(__file__).parent.parent / "assets" / f"{number}.png"
    pixmap = QPixmap(str(img_path))
    image_label.setPixmap(pixmap)

Button1 = QPushButton("Change Image", window)
Button1.setFixedSize(450, 50)
Button1.clicked.connect(change)

update()
window.show()
sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)
window = QWidget()
window.resize(300,150)

def on_click():
    lbl.setText("안녕히가세요.")

lbl = QLabel("안녕하세요", window)
lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
lbl.resize(window.size())

button = QPushButton("Press me!", window)
button.move(180,100)
button.clicked.connect(on_click)

window.show()
sys.exit(app.exec())
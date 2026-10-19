import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class startWindow(QMainWindow):
    clicked = pyqtSignal()
    keyboard_input = pyqtSignal(str)
    signal3 = pyqtSignal(int, int)

    def __init__(self):
        super().__init__()
        self.count = 0
        self.init_ui()

        self.clicked.connect(self.count_click)
        self.keyboard_input.connect(self.keyboard_input_slot)
        self.keyboard_input.connect(self.count_click)
        self.signal3.connect(self.signal3_slot)

    def init_ui(self):
        self.setWindowTitle("Click Counter")
        self.setGeometry(100, 100, 300, 200)
        layout = QVBoxLayout()

        self.label = QLabel("0 times clicked.")
        layout.addWidget(self.label)

        self.label3 = QLabel("Input : ")
        layout.addWidget(self.label3)

        self.label2 = QLabel("Click me")
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label2.setStyleSheet("background-color: #c0c0ff;")
        layout.addWidget(self.label2)

        self.label4 = QLabel("Pos : [0, 0]")
        layout.addWidget(self.label4)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()

    def mousePressEvent(self, event):
        if self.label2.geometry().contains(event.pos()):
            self.clicked.emit()

    def count_click(self):
        self.count += 1
        self.label.setText(f"{self.count} times clicked.")

    def keyPressEvent(self, event):
        self.keyboard_input.emit(event.text())

    def keyboard_input_slot(self, text):
        self.label3.setText(f"Input : {text}")

    def mouseMoveEvent(self, event):
        self.signal3.emit(event.x(), event.y())

    def signal3_slot(self, a, b):
        self.label4.setText(f"Pos : [{a}, {b}]")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
import sys
from PyQt5.QtWidgets import (
    QApplication, QGridLayout, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
)
from PyQt5.QtCore import Qt

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()


    def init_ui(self):
        self.setWindowTitle("Layout Practice")
        self.setFixedSize(400, 200)
        self.setStyleSheet("background-color: #f0f0f0;")

        grid_layout = QGridLayout()

        label1 = QLabel("이름", self)
        label1.setAlignment(Qt.AlignCenter)
        label1.setStyleSheet(
            f"background-color: cyan; color: black; font-size: 24px; font-family: 'SUIT Light'"
        )

        label2 = QLabel("(Input Shows Here.)", self)
        label2.setAlignment(Qt.AlignCenter)
        label2.setStyleSheet(
            f"background-color: #ebc1fa; color: black; font-size: 20px; font-family: 'SUIT Light'"
        )

        Button = QPushButton("제출", self)
        Button.setStyleSheet(
            f"background-color: white; color: black; font-size: 24px; font-family: 'SUIT Light'"
        )
        Button.clicked.connect(lambda: label2.setText(Input.text()))

        Input = QLineEdit(self)
        Input.setPlaceholderText("Input Here.")
        Input.setStyleSheet(
            f"background-color: white; color: black; font-size: 24px; font-family: 'SUIT Light'"
        )

        grid_layout.addWidget(label1, 0, 0)
        grid_layout.addWidget(label2, 1, 2, 2, 1)
        grid_layout.addWidget(Button, 1, 1)
        grid_layout.addWidget(Input, 0, 1, 1, 2)

        self.setLayout(grid_layout)

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = startWindow()
    window.show()
    sys.exit(app.exec_())
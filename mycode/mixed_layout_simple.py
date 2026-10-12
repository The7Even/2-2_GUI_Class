import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout
)
from PyQt5.QtCore import Qt


class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("QHBoxLayout")
        self.setFixedSize(400, 200)
        self.setStyleSheet("background-color: #f0f0f0;")

        # Create horizontal box layout
        v_layout = QVBoxLayout()
        h_layout2 = QHBoxLayout()

        label = QLabel("수직 레이아웃 1", self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet(
            f"background-color: red; color: black; font-size: 24px;"
        )
        v_layout.addWidget(label)

        label = QLabel("수평 1", self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet(
            f"background-color: blue; color: black; font-size: 24px;"
        )
        h_layout2.addWidget(label)

        label = QLabel("수평 2", self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet(
            f"background-color: green; color: black; font-size: 24px;"
        )
        h_layout2.addWidget(label)

        label = QLabel("수평 3", self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet(
            f"background-color: yellow; color: black; font-size: 24px;"
        )
        h_layout2.addWidget(label)


        v_layout.addLayout(h_layout2)
        self.setLayout(v_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = startWindow()
    window.show()
    sys.exit(app.exec_())

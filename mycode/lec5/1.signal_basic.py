import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import pyqtSignal

class startWindow(QWidget):
    # 1) signal 만들기 (클래스 변수)
    close_app = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_ui()
        # 2) signal 과 slot 연결
        self.close_app.connect(self.close)

    def init_ui(self):
        self.setWindowTitle("1. Signal Basic")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Click anywhere to close"))
        self.setLayout(layout)
        self.show()

    def mousePressEvent(self, event):
        # 3) signal 보내기
        self.close_app.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())

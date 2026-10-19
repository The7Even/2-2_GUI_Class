import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel)
from PyQt5.QtCore import Qt, pyqtSignal

class startWindow(QMainWindow):
    resized = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_ui()

        self.resized.connect(self.update_label)  # signal 과 slot 연결

    def init_ui(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Resize / Move Example")
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label)
        self.show()

    def resizeEvent(self, event):
        # 창 크기가 바뀔 때마다 호출
        size = event.size()
        print(f"Resized: {size.width()} x {size.height()}")
        self.resized.emit()

    def moveEvent(self, event):
        # 창 위치가 바뀔 때마다 호출
        pos = event.pos()
        print(f"Moved to: ({pos.x()}, {pos.y()})")
        self.resized.emit()

    def update_label(self):
        self.label.setText(
            f"<p>Size: <b>{self.width()} x {self.height()}</b></p>"
            f"<p>Position: <b>({self.x()}, {self.y()})</b></p>")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())

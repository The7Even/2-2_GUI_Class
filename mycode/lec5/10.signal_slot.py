import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel)
from PyQt5.QtCore import Qt, pyqtSignal

class startWindow(QMainWindow):
    # 사용자 정의 signal 은 클래스 변수로 선언해야 합니다 (__init__ 안에서 X)
    key_typed = pyqtSignal(str)   # 데이터(str)를 함께 보내는 signal
    close_app = pyqtSignal()      # 데이터 없는 signal

    def __init__(self):
        super().__init__()
        self.init_ui()

        # signal 과 slot 연결: signal.connect(slot)
        self.key_typed.connect(self.show_key)
        self.close_app.connect(self.close)   # 내장 메서드도 slot 으로 사용 가능

    def init_ui(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Signal & Slot Example")
        self.label = QLabel(
            """<p>Type any key.<br>Press <b>ESC</b> to quit.</p>""")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label)
        self.show()

    def keyPressEvent(self, event):
        # event handler 는 signal 을 emit 만 하고, 실제 처리는 slot 에서
        if event.key() == Qt.Key.Key_Escape:
            print("ESC pressed -> emit close_app")
            self.close_app.emit()
        elif event.text():
            print(f"'{event.text()}' pressed -> emit key_typed")
            self.key_typed.emit(event.text())

    def show_key(self, text):
        # slot: key_typed signal 이 보낸 데이터를 받음
        self.label.setText(f"<p>You typed: <b>{text}</b></p>")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())


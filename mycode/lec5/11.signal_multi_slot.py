import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel,
                             QVBoxLayout)
from PyQt5.QtCore import Qt, pyqtSignal

class startWindow(QMainWindow):
    # signal 하나 -> slot 여러 개
    key_typed = pyqtSignal(str)
    close_app = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.count = 0  # 누른 키 개수

        # 하나의 signal 에 slot 3개 연결 (연결한 순서대로 호출됨)
        self.key_typed.connect(self.show_key)       # slot 1
        self.key_typed.connect(self.show_message)   # slot 2
        self.key_typed.connect(self.count_key)      # slot 3

        self.close_app.connect(self.close)

    def init_ui(self):
        self.setGeometry(100, 100, 350, 250)
        self.setWindowTitle("One Signal, Multiple Slots")

        self.key_label = QLabel("<p>Try <b>h</b>, <b>b</b>, <b>q</b> or a number."
                                "<br>Press <b>ESC</b> to quit.</p>")
        self.message_label = QLabel("")
        self.count_label = QLabel("Keys pressed: 0")
        for label in (self.key_label, self.message_label, self.count_label):
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.key_label)
        layout.addWidget(self.message_label)
        layout.addWidget(self.count_label)

        # QMainWindow 에 layout 을 쓰려면 QWidget 을 하나 만들어 central widget 으로
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.show()

    def keyPressEvent(self, event):
        # event handler 는 emit 한 번만 -> 연결된 slot 3개가 모두 실행됨
        if event.key() == Qt.Key.Key_Escape:
            self.close_app.emit()
        elif event.text():
            print(f"--- '{event.text()}' pressed -> emit key_typed")
            self.key_typed.emit(event.text())

    # slot 1: 어떤 키를 눌렀는지 표시
    def show_key(self, text):
        print("slot 1: show_key")
        self.key_label.setText(f"<p>You typed: <b>{text}</b></p>")

    # slot 2: 키에 따라 다른 메시지 표시
    def show_message(self, text):
        print("slot 2: show_message")
        if text == "h":
            message = "Hello! 안녕하세요 👋"
            color = "green"
        elif text == "b":
            message = "Bye! 안녕히 가세요"
            color = "blue"
        elif text == "q":
            message = "Press ESC to quit, not q 😉"
            color = "red"
        elif text.isdigit():
            message = f"{text} is a number"
            color = "purple"
        else:
            message = "Unknown key"
            color = "gray"
        self.message_label.setText(message)
        self.message_label.setStyleSheet(f"color: {color}; font-size: 18px;")

    # slot 3: 누른 키 개수 세기
    def count_key(self, text):
        print("slot 3: count_key")
        self.count += 1
        self.count_label.setText(f"Keys pressed: {self.count}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())

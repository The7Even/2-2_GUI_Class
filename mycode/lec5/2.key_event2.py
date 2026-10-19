import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel)

from PyQt5.QtCore import Qt, QTime

class startWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

        self.start_time = None  # 시간 

    def init_ui(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Event Handling Example")
        label = QLabel(
            """<p>Press the <b>ESC</b> key for 5 secs to quit this program.</p>""")
        self.setCentralWidget(label)
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_T:
            # timer 시작
            if self.start_time is None:
                print("ESC key pressed! Starting timer for 5 seconds...")
                self.start_time = QTime.currentTime()

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key.Key_T and not event.isAutoRepeat():
            if self.start_time is not None:
                current_time = QTime.currentTime()
                # "current time - start_time"직접 사용할수 없습니다, msecsTo 를 사용하시오
                elapsed_time = self.start_time.msecsTo(current_time)
                if elapsed_time >= 5000:  # 5초 이상
                    print("ESC key held for 5 seconds! Closing the window.")
                    self.close()
                else:
                    print(f"ESC key released after {elapsed_time / 1000:.2f} seconds. Not closing.")
            self.start_time = None  # reset timer

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())


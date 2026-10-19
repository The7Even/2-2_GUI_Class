from asyncio import sleep
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel)
from PyQt5.QtCore import QTime, Qt

class startWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

        self.setMouseTracking(True)
        self.label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
        self.label2.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
        self.label4.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)

        self.HoldTime = -1  # 키를 누른 시간?
        self.BackCode = 0

    def init_ui(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Mouse Press Example")
        self.label = QLabel("<p>Click anywhere with any mouse button.</p>", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setGeometry(0, 0, 300, 200)
        self.label.setStyleSheet("background-color:transparent;")
        self.label2 = QLabel("<p>Pos : (0, 0)</p>", self)
        self.label2.setGeometry(0, 0, 300, 200)
        self.label2.setStyleSheet("background-color:transparent;")
        self.label2.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight)
        self.label4 = QLabel("<p>Mouse Detector</p>",self)
        self.label4.setGeometry(0, 0, 300, 200)
        self.label4.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        self.label4.setStyleSheet("background-color:transparent;")
        self.show()

    def mousePressEvent(self, event):
        # 어떤 버튼이 눌렸는지 확인
        if event.button() == Qt.MouseButton.LeftButton:
            button = "Left"
        elif event.button() == Qt.MouseButton.RightButton:
            button = "Right"
        elif event.button() == Qt.MouseButton.MiddleButton:
            button = "Middle"
        elif event.button() == Qt.MouseButton.BackButton:
            button = "Back"
        elif event.button() == Qt.MouseButton.ForwardButton:
            button = "Forward"
        else:
            button = "Other"
        x, y = event.pos().x(), event.pos().y()
        print(f"{button} button pressed at ({x}, {y})")
        self.label.setText(f"<p><b>{button}</b> button pressed at ({x}, {y})</p>")
        if self.HoldTime == -1:
            self.HoldTime = QTime.currentTime()  # 키를 누른 시간 기록
    
    def mouseMoveEvent(self, event):
        x, y = event.pos().x(), event.pos().y()
        self.label2.setText(f"<p>Pos : ({x}, {y})</p>")
    
    def mouseReleaseEvent(self, event):
        # 어떤 버튼이 눌렸는지 확인
        if event.button() == Qt.MouseButton.LeftButton:
            button = "Left"
        elif event.button() == Qt.MouseButton.RightButton:
            button = "Right"
        elif event.button() == Qt.MouseButton.MiddleButton:
            button = "Middle"
        elif event.button() == Qt.MouseButton.BackButton:
            button = "Back"
        elif event.button() == Qt.MouseButton.ForwardButton:
            button = "Forward"
        else:
            button = "Other" 

        if self.HoldTime != -1:
            release_time = QTime.currentTime()
            self.HoldTime = self.HoldTime.msecsTo(release_time)

            print(f"Held {button} for {self.HoldTime/1000:.3f} seconds.")
            self.HoldTime = -1

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            if self.BackCode == 0 or self.BackCode == 2:
                self.setStyleSheet("background-color: black;")
                self.label.setStyleSheet("color: white; background-color:transparent;")
                self.label2.setStyleSheet("color: white; background-color:transparent;")
                self.label4.setStyleSheet("color: white; background-color:transparent;")
                self.BackCode = 1
            else:
                self.setStyleSheet("background-color: white;")
                self.label.setStyleSheet("color: black; background-color:transparent;")
                self.label2.setStyleSheet("color: black; background-color:transparent;")
                self.label4.setStyleSheet("color: black; background-color:transparent;")
                self.BackCode = 0
        if event.button() == Qt.MouseButton.RightButton:
            if self.BackCode == 0 or self.BackCode == 1:
                self.setStyleSheet("background-color: blue;")
                self.label.setStyleSheet("color: white; background-color:transparent;")
                self.label2.setStyleSheet("color: white; background-color:transparent;")
                self.label4.setStyleSheet("color: white; background-color:transparent;")
                self.BackCode = 2
            else:
                self.setStyleSheet("background-color: white;")
                self.label.setStyleSheet("color: black; background-color:transparent;")
                self.label2.setStyleSheet("color: black; background-color:transparent;")
                self.label4.setStyleSheet("color: black; background-color:transparent;")
                self.BackCode = 0

    def enterEvent(self, event):
        self.label4.setText("<p>Mouse Detected!</p>")
        self.setStyleSheet("background-color: white;")
        self.label.setStyleSheet("color: black; background-color:transparent;")
        self.label2.setStyleSheet("color: black; background-color:transparent;")
        self.label4.setStyleSheet("color: black; background-color:transparent;")
        self.BackCode = 0

    def leaveEvent(self, event):
        self.label4.setText("<p>Looking for Mouse...</p>")
        self.setStyleSheet("background-color: #ff5555;")
        self.label.setStyleSheet("color: black; background-color:transparent;")
        self.label2.setStyleSheet("color: black; background-color:transparent;")
        self.label4.setStyleSheet("color: black; background-color:transparent;")

    def resizeEvent(self, event):
        self.setBaseSize(self.width(), self.height())
        self.label.setGeometry(0, 0, self.width(), self.height())
        self.label2.setGeometry(0, 0, self.width(), self.height())
        self.label4.setGeometry(0, 0, self.width(), self.height())

    def moveEvent(self, event):
        pos = event.pos()
        self.setGeometry(pos.x(), pos.y(), self.width(), self.height())
        self.label.setGeometry(0, 0, self.width(), self.height())
        self.label2.setGeometry(0, 0, self.width(), self.height())
        self.label4.setGeometry(0, 0, self.width(), self.height())

class ScrollWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.SizeofFont = 15
        self.ScrollValue = 0
        self.init_ui()

        self.label3.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)

    def init_ui(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Mouse Scroll Example")
        self.label3 = QLabel("<p>■</p>", self)
        self.label3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label3)
        self.show()

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            self.ScrollValue = 1
        elif event.angleDelta().y() < 0:
            self.ScrollValue = -1
        else:
            self.ScrollValue = 0

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Alt and not event.isAutoRepeat():
            print("Key Held")
            if self.ScrollValue != 0:
                if self.ScrollValue == 1:
                    self.SizeofFont += 1
                elif self.ScrollValue == -1:
                    self.SizeofFont -= 1
                self.label3.setStyleSheet(f"font-size: {self.SizeofFont}px;")
                print(f"Font : {self.SizeofFont}px")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    # window2 = ScrollWindow() # 저리가라 이 더러운자식
    sys.exit(app.exec())

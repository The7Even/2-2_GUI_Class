import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Outdoor(QObject):
    signal_add = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.count = 0

    def add_number(self):
        self.count += 1
        self.signal_add.emit(self.count)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.outdoor = Outdoor()
        self.outdoor.signal_add.connect(self.show_value)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Pract 8")
        self.label = QLabel("0")

        self.addButton = QPushButton("+1")
        self.addButton.clicked.connect(self.outdoor.add_number)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.addButton)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()

    def show_value(self, value):
        self.label.setText(str(value))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
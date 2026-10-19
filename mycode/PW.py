import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    check_login = pyqtSignal(str)
    userList = {
        "admin":"adminpw1234",
        "user1":"useruser",
        "user2":"12345678"
    }

    def __init__(self):
        super().__init__()
        self.init_ui()

        self.check_login.connect(self.check_login_slot)

    def init_ui(self):
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 300, 200)

        layout = QGridLayout()

        self.label_id = QLabel("ID:")
        self.input_id = QLineEdit()
        layout.addWidget(self.label_id, 0, 0)
        layout.addWidget(self.input_id, 0, 1)

        self.label_pw = QLabel("Password:")
        self.input_pw = QLineEdit()
        layout.addWidget(self.label_pw, 1, 0)
        layout.addWidget(self.input_pw, 1, 1)
        self.input_pw.setEchoMode(QLineEdit.EchoMode.Password)

        self.Login_button = QPushButton("Login")
        self.Login_button.clicked.connect(lambda: self.check_login.emit(self.input_pw.text()))

        layout.addWidget(self.Login_button, 2, 0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Return:
            self.check_login.emit(self.input_pw.text())

        
    def check_login_slot(self, pw):
        if self.input_id.text() != '' and self.input.pw.text() != '' and self.userList[self.input_id.text()] == self.input_pw.text():
            QMessageBox.information(self, "Login", "Login successful!")
            exit(0)
        elif self.input_id.text() == '' and self.input_pw.text() == 'thesecretkeyispneumonoultramicroscopicsilicovolcanoconiosis':
            QMessageBox.critical(self, '뛟¶?&@', "Unknown Error")
            exit(66666666)
        else:
            QMessageBox.warning(self, "Login", "ID or PW Incorrect")
            self.input_pw.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


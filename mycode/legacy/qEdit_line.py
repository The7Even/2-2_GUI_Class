import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QTextEdit, QLineEdit,
    QPushButton, QMessageBox,
)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def on_click(self, caller):
            if caller =='text_edit':
                self.reslt_label.setText(f"QTextEdit: {self.text_edit.toPlainText()}")
            elif caller =='line_edit':
                self.reslt_label.setText(f"QLineEdit: {self.line_edit.text()}")
            self.reslt_label.show()
    
    def init_ui(self):
        self.setWindowTitle("QTextEdit and QLineEdit")
        self.setFixedSize(500, 260)

        self.text_label = QLabel("QTextEdit", self)
        self.text_label.move(20, 20)

        self.text_edit = QTextEdit(self)
        self.text_edit.setPlaceholderText("Edit Text Here")
        self.text_edit.setGeometry(20, 50, 220, 40)

        self.line_label = QLabel("QLineEdit", self)
        self.line_label.move(260, 20)

        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("Line Edit Here")
        self.line_edit.setGeometry(260, 50, 220, 40)
        self.line_edit.returnPressed.connect(lambda: self.on_click('line_edit'))

        self.line_edit.textChanged.connect(lambda: self.on_click('line_edit'))
        self.line_edit.setEchoMode(QLineEdit.Password)

        self.text_button = QPushButton("Text_Enter", self)
        self.text_button.setGeometry(80, 100, 100, 30)
        self.text_button.clicked.connect(lambda: self.on_click('text_edit'))

        self.reslt_label = QLabel("Result", self)
        self.reslt_label.setGeometry(20, 140, 460, 100)
        self.reslt_label.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = startWindow()
    window.show()
    sys.exit(app.exec_())

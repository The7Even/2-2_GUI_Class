import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QTextEdit, QLineEdit,
    QPushButton, QMessageBox,
)


def on_click(caller):
    if caller =='text_edit':
        reslt_label.setText(f"QTextEdit: {text_edit.toPlainText()}")
    elif caller =='line_edit':
        reslt_label.setText(f"QLineEdit: {line_edit.text()}")
    reslt_label.show()


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("QTextEdit and QLineEdit")
window.setFixedSize(500, 260)

text_label = QLabel("QTextEdit", window)
text_label.move(20, 20)

text_edit = QTextEdit(window)
text_edit.setPlaceholderText("Edit Text Here")
text_edit.setGeometry(20, 50, 220, 40)

line_label = QLabel("QLineEdit", window)
line_label.move(260, 20)

line_edit = QLineEdit(window)
line_edit.setPlaceholderText("Line Edit Here")
line_edit.setGeometry(260, 50, 220, 40)

text_button = QPushButton("Text_Enter", window)
text_button.setGeometry(80, 100, 100, 30)
text_button.clicked.connect(lambda: on_click('text_edit'))

line_button = QPushButton("Line_Enter", window)
line_button.setGeometry(320,100,100,30)
line_button.clicked.connect(lambda: on_click('line_edit'))

reslt_label = QLabel("Result", window)
reslt_label.setGeometry(20, 140, 460, 100)
reslt_label.hide()

window.show()
sys.exit(app.exec_())

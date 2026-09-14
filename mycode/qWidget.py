import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

app = QApplication(sys.argv)
window = QWidget()

window.setFixedSize(1200,50)
window.setStyleSheet("font-family: 'SUIT ExtraBold';font-size: 20px;")

window.setWindowTitle("GUI Test")
lbl = QLabel("Hello, PyQt5! GUI is Graphic User Interface.", window)
window.show()
sys.exit(app.exec())


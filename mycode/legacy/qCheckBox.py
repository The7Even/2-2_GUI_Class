import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QTextEdit, QLineEdit,
    QPushButton, QMessageBox, QCheckBox, QButtonGroup
)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("QTextEdit and QLineEdit")
        self.setFixedSize(500, 500)

        # label
        self.text_label = QLabel("좋아하는 가수?", self)
        self.text_label.setGeometry(20, 20, 100, 30)

        # check boxes
        self.singer1_checkbox = QCheckBox("BTS", self)
        self.singer1_checkbox.setGeometry(20, 60, 100, 30)
        self.singer2_checkbox = QCheckBox("BLACKPINK", self)
        self.singer2_checkbox.setGeometry(20, 100, 100, 30)
        self.singer3_checkbox = QCheckBox("TWICE", self)
        self.singer3_checkbox.setGeometry(20, 140, 100, 30)
        self.singer4_checkbox = QCheckBox("IU", self)
        self.singer4_checkbox.setGeometry(20, 180, 100, 30)
        self.singer5_checkbox = QCheckBox("aespa", self)
        self.singer5_checkbox.setGeometry(20, 220, 100, 30)
        self.singer6_checkbox = QCheckBox("Rosie", self)
        self.singer6_checkbox.setGeometry(20, 260, 100, 30)

        # Group
        self.Group = QButtonGroup(self)
        self.Group.setExclusive(False)
        self.Group.addButton(self.singer1_checkbox)
        self.Group.addButton(self.singer2_checkbox)
        self.Group.addButton(self.singer3_checkbox)
        self.Group.addButton(self.singer4_checkbox)
        self.Group.addButton(self.singer5_checkbox)
        self.Group.addButton(self.singer6_checkbox)


        # Button
        self.button = QPushButton("제출", self)
        self.button.setGeometry(20, 300, 100, 30)
        self.button.clicked.connect(self.on_click)

        # 항목 클릭시 자동 반영
        self.Group.buttonToggled.connect(self.on_click)

        # result display label
        self.result_label = QLabel("Result", self)
        self.result_label.setGeometry(20, 340, 460, 100)
        self.result_label.hide()

    def on_click(self):
        selected_singers = []
        for checkbox in self.Group.buttons():
            if checkbox.isChecked():
                selected_singers.append(checkbox.text())


        if selected_singers:
            self.result_label.setText(f"좋아하는 가수: {', '.join(selected_singers)}")
        else:
            self.result_label.setText("좋아하는 가수를 선택해주세요.")
        self.result_label.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = startWindow()
    window.show()
    sys.exit(app.exec_())

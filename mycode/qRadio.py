import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QTextEdit, QLineEdit,
    QPushButton, QMessageBox, QRadioButton, QButtonGroup
)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("QTextEdit and QLineEdit")
        self.setFixedSize(500, 260)

        # label
        self.text_label = QLabel("성별", self)
        self.text_label.setGeometry(20, 20, 100, 30)

        # radio buttons
        self.male_radio = QRadioButton("남성", self)
        self.male_radio.setGeometry(20, 60, 100, 30)

        self.female_radio = QRadioButton("여성", self)
        self.female_radio.setGeometry(20, 100, 100, 30)

        self.other_radio = QRadioButton("기타", self)
        self.other_radio.setGeometry(20, 140, 100, 30)
        self.other_line = QLineEdit(self)
        self.other_line.setPlaceholderText("Input...")
        self.other_line.setGeometry(140, 140, 100, 30)


        # Button
        self.button = QPushButton("제출", self)
        self.button.setGeometry(20, 180, 100, 30)
        self.button.clicked.connect(self.on_click)

        # result display label
        self.result_label = QLabel("Result", self)
        self.result_label.setGeometry(20, 180, 460, 100)
        self.result_label.hide()

        # ButtonGroup
        self.Group = QButtonGroup(self)
        self.Group.addButton(self.male_radio, 1)
        self.Group.addButton(self.female_radio, 2)
        self.Group.addButton(self.other_radio, 3)


    def on_click(self):
        match self.Group.checkedId:
            case 1:
                self.result_label.setText("사용자의 성별은 남성입니다.")
            case 2:
                self.result_label.setText("사용자의 성별은 여성입니다.")
            case 3:
                if self.other_line.text() != "":
                    self.result_label.setText(f"사용자는 {self.other_line.text()}(이)라고 합니다.")
                else:
                    self.result_label.setText("그럼 당신은 뭡니까?")
            case _:
                self.result_label.setText("성별을 선택해주세요.")
        self.result_label.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = startWindow()
    window.show()
    sys.exit(app.exec_())

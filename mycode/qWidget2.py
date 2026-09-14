import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("System Locker")
window.resize(300, 200)
window.setStyleSheet(
    "background-color: black; color: white; font-family: 'SUIT'; font-size:"
    " 16px;"
)

lbl = QLabel("Locked Service", window)
lbl.setStyleSheet("font-family: 'SUIT ExtraBold'; font-size: 24px; color: red;")
lbl.move(60, 30)

name_lbl = QLabel("Enter PassKey:", window)
name_lbl.resize(250, 25)
name_lbl.move(25, 60)

edit = QLineEdit(window)
edit.setFixedSize(250, 30)
edit.setEchoMode(QLineEdit.Password)
edit.move(25, 90)

btn = QPushButton("Unlock", window)
btn.setStyleSheet(
    "background-color: gray; color: white; font-family: 'SUIT'; font-size:"
    " 16px;"
)
btn.resize(100, 40)
btn.move(100, 130)

# 비밀번호 및 실패 횟수 상태 관리
CORRECT_PASSWORD = "11333355555577777777"  # 설정하고 싶은 실제 비밀번호야
fail_count = 0


def check_password():
    global fail_count

    user_input = edit.text()

    if user_input == CORRECT_PASSWORD:
        print("Password Accepted. Unlocking...")
        print("No Contents to Show. Just Watch Rick Roll.")
        print("https://youtu.be/dQw4w9WgXcQ?si=94izSRweBpNf8_tq")
        window.close()
    else:
        fail_count += 1
        edit.clear()

        if fail_count >= 5:
            print("U suck")
            window.close()
        else:
            name_lbl.setText(f"{fail_count}/5 attempts failed. Enter PassKey:")
            name_lbl.setStyleSheet(
                "color: red; font-family: 'SUIT'; font-size: 14px;"
            )


# 버튼 클릭 시 검증 함수 호출
btn.clicked.connect(check_password)

# Enter 키를 눌렀을 때도 바로 검증되도록 연결
edit.returnPressed.connect(check_password)

window.show()
sys.exit(app.exec_())
import argparse
import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMessageBox

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(
        description="지정한 시간이 지난 후 GUI 알림 메시지를 표시합니다."
    )
    parser.add_argument(
        "seconds",
        help="대기할 시간(초)",
    )
    parser.add_argument(
        "message",
        nargs="*",
        help='선택적 알림 메시지(기본값: "알림!")',
    )
    args = parser.parse_args()

    message = " ".join(args.message) if args.message else "알림!"

    try:
        secs = float(args.seconds)
        if secs < 0:
            raise ValueError
    except ValueError:
        parser.error("초는 0 이상의 숫자여야 합니다")

    app = QApplication([])
    print(sys.argv)

    def show_alert():
        QMessageBox.information(None, "알림", message)
        app.quit()

    QTimer.singleShot(int(secs * 1000), show_alert)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


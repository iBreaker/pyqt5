import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.move(100, 100)
    w.setWindowTitle("This is a title")
    w.resize(100, 100)
    w.show()

    sys.exit(app.exec_())
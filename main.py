import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox


class Tools(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.move(100, 100)                             # 位置
        self.resize(100, 100)                           # 窗口大小
        self.setWindowTitle("This is a title")          # 标题
        self.show()                                     # 显示

    def closeEvent(self, event):
        result = QMessageBox.question(self, "Message", "确认退出？"
                                      , QMessageBox.Yes|QMessageBox.No
                                      , QMessageBox.No)

        if result == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tools = Tools()
    sys.exit(app.exec_())
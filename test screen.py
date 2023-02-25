import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout


class Window1(QWidget):
    def __init__(self):
        super().__init__()

        # 버튼 생성
        self.btn = QPushButton('Open Window 2', self)

        # 버튼 클릭 시 실행할 함수 지정
        self.btn.clicked.connect(self.open_window2)

        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Window 1'))
        layout.addWidget(self.btn)
        self.setLayout(layout)

    def open_window2(self):
        self.window2 = Window2()
        self.window2.show()
        self.close()


class Window2(QWidget):
    def __init__(self):
        super().__init__()

        # 버튼 생성
        self.btn = QPushButton('Close Window 2', self)

        # 버튼 클릭 시 실행할 함수 지정
        self.btn.clicked.connect(self.close)

        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Window 2'))
        layout.addWidget(self.btn)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window1 = Window1()
    window1.show()

    sys.exit(app.exec_())

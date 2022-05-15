from random import randrange
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

class RandomButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)

    def randomize(self):
        self.setText(str(randrange(100)))

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Customer Button")
        self.layout = QHBoxLayout(self)
        btn_random = RandomButton(str(randrange(999)))
        btn_random.setMinimumSize(48, 48)
        btn_random.setFlat(True)
        btn_random.setCheckable(True)
        btn_random.setStyleSheet(f"color: rgb(255, 0, 0);")

        self.layout.addWidget(btn_random)

        self.setFocus()

app = QApplication()
win = MainWindow()
win.show()
app.exec()
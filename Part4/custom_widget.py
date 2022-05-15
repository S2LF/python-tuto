from random import randrange, random
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

class RandomButton(QPushButton):
    def __init__(self, text, size=48, flat=False):
        super().__init__(text)
        self.setText(str(randrange(999)))
        self.setMinimumSize(size, size)
        self.setFlat(flat)
        self.setCheckable(flat)
        self.random_color()
        self.clicked.connect(self.random_color)

    def random_color(self):
        self.setStyleSheet(f"color: rgb({randrange(255)}, {randrange(255)}, {randrange(255)}); background-color: rgb({randrange(255)}, {randrange(255)}, {randrange(255)});")

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Customer Button")
        self.layout = QHBoxLayout(self)
        for _ in range(12):
            btn_random = RandomButton(str(randrange(999)), randrange(10, 200), True if random() > 0.5 else False)
            self.layout.addWidget(btn_random)

        self.setFocus()

app = QApplication()
win = MainWindow()
win.show()
app.exec()
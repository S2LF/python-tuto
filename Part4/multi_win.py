from random import randrange
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Multi Window")
        self.layout = QHBoxLayout(self)
        self.btn_new_window = QPushButton("New Window")
        self.btn_new_window.clicked.connect(self.create_new_window)
        self.btn_settings = QPushButton("Settings")
        self.btn_settings.clicked.connect(self.show_settings)
        self.layout.addWidget(self.btn_new_window)
        self.layout.addWidget(self.btn_settings)
        self.windows = {}
        self.resize(600, 400)

    def create_new_window(self):
        window_number = randrange(999)
        self.windows[f"window {window_number}"] = QWidget()
        self.windows[f"window {window_number}"].setWindowTitle(f"Window {window_number}")
        self.windows[f"window {window_number}"].show()

    def show_settings(self):
        self.settings_windows = QWidget()
        self.settings_windows.setWindowTitle("Settings")
        self.settings_windows.show()

app = QApplication()
win = MainWindow()
win.show()
app.exec()
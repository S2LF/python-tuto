from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout,QHBoxLayout, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6")

        main_layout = QHBoxLayout(self)

        self.button = QPushButton("Click me")
        self.button.setCheckable(True)
        main_layout.addWidget(self.button)

        self.button.clicked.connect(self.on_button_clicked)
        self.button.pressed.connect(self.on_button_pressed)
        self.button.released.connect(self.on_button_released)

    def on_button_clicked(self, check):
        if check:
            self.button.setText("Checked")
        else:
            self.button.setText("Unchecked")
        print(check)
        print("Button clicked")

    def on_button_pressed(self):
        print("Button pressed")

    def on_button_released(self):
        print("Button released")

app = QApplication()

main_window = MainWindow()
main_window.show()

app.exec()

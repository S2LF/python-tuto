from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout,QHBoxLayout, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6")
        # # Taille fixe
        # self.setFixedSize(200, 200)
        # # Taille minimal
        # self.setMinimumSize(200, 200)
        # # Taille maximal
        # self.setMaximumSize(200, 200)
        # # Taille par défaut
        # self.resize(200, 200)

        main_layout = QHBoxLayout(self)

        left_layout = QVBoxLayout()
        left_layout.addWidget(QPushButton("Left"))
        right_layout = QVBoxLayout()
        right_layout.addWidget(QPushButton("Right"))

        middle_layout = QHBoxLayout()
        right_layout.addLayout(middle_layout)

        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        for i in range(1, 11):
            button = QPushButton(str(i))
            right_layout.addWidget(button)

        for i in range(11, 21):
            button = QPushButton(str(i))
            left_layout.addWidget(button)

        for i in range(21, 30):
            button = QPushButton(str(i))
            middle_layout.addWidget(button)

app = QApplication()

main_window = MainWindow()
main_window.show()

app.exec()

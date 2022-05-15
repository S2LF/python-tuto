from PySide6.QtGui import QShortcut, QKeySequence
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QGridLayout, QLineEdit, QSizePolicy
from PySide6 import QtCore

BUTTON = {
    "C": (1, 0, 1, 1),
    "/": (1, 3, 1, 1),
    "7": (2, 0, 1, 1),
    "8": (2, 1, 1, 1),
    "9": (2, 2, 1, 1),
    "x": (2, 3, 1, 1),
    "4": (3, 0, 1, 1),
    "5": (3, 1, 1, 1),
    "6": (3, 2, 1, 1),
    "-": (3, 3, 1, 1),
    "1": (4, 0, 1, 1),
    "2": (4, 1, 1, 1),
    "3": (4, 2, 1, 1),
    "+": (4, 3, 1, 1),
    "0": (5, 0, 1, 2),
    ".": (5, 2, 1, 1),
    "=": (5, 3, 1, 1),
}

OPERATIONS = ["+", "-", "x", "/"]

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculatrice")
        self.setStyleSheet("""
            background-color: rgb(20,20,20);
            color: rgb(220,220,220);
            font-size: 18px;
        """)
        self.buttons = {}
        self.main_layout = QGridLayout(self)
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)


        self.le_result = QLineEdit("0")
        self.le_result.setMinimumHeight(50)
        self.le_result.setAlignment(QtCore.Qt.AlignRight)
        self.le_result.setEnabled(False)
        self.le_result.setStyleSheet("""
            border: none;
            border-bottom: 2px solid rgb(30,30,30);
            padding: 0 8px;
            font-size: 24px;
            font-weight: bold;
        """)
        self.main_layout.addWidget(self.le_result, 0, 0, 1, 4)

        for text, position in BUTTON.items():
            button = QPushButton(text)
            button.setMinimumSize(48, 48)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.main_layout.addWidget(button, *position)
            button.setStyleSheet(f"""
                QPushButton {{
                    border:none;
                    font-weight: bold;
                    background-color: {'#1e1e2d' if text in OPERATIONS else 'none'};
                }}
                QPushButton:pressed {{ background-color: #f31d58;}} 
            """)
            if text not in ["=", "C"]:
                button.clicked.connect(self.number_or_operation_pressed)
            self.buttons[text] = button

        self.buttons["C"].clicked.connect(self.clear_result)
        self.buttons["="].clicked.connect(self.compute_result)
        self.buttons["="].setStyleSheet("border:none; background-color: #f31d58;")
        self.connect_keyboard_shortcuts()

    @property
    def result(self):
        return self.le_result

    def compute_result(self):
        result = self.result
        try:
            result.setText(str(eval(result.text().replace("x", "*"))))
        except SyntaxError:
            return
        
    def clear_result(self):
        self.le_result.setText("0")

    def number_or_operation_pressed(self):
        result = self.result
        sender = self.sender()

        if sender.text() in OPERATIONS:
            if result.text()[-1] in OPERATIONS or result.text() == "0":
                return

        if result.text() == "0":
            result.clear()
        result.setText(result.text() + sender.text())

    def remove_last_char(self):
        result = self.result
        if len(result.text()) > 1:
            result.setText(result.text()[:-1])
        else:
            result.setText("0")

    def connect_keyboard_shortcuts(self):
        for text, position in self.buttons.items():
            QShortcut(QKeySequence(text), self, position.clicked.emit)
        QShortcut(QKeySequence(QtCore.Qt.Key_Asterisk), self, self.buttons["x"].clicked.emit)
        QShortcut(QKeySequence(QtCore.Qt.Key_Return), self, self.compute_result)
        QShortcut(QKeySequence(QtCore.Qt.Key_Enter), self, self.compute_result)
        QShortcut(QKeySequence(QtCore.Qt.Key_Backspace), self, self.remove_last_char)



app = QApplication()
win = Calculator()
win.show()
app.exec()
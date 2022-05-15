from PySide6.QtWidgets import QApplication, QWidget, QListWidget,QVBoxLayout, QPushButton, QLineEdit

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To Do List")

        self.main_layout = QVBoxLayout(self)

        self.lw_list = QListWidget()
        self.le_add = QLineEdit()
        self.le_add.setPlaceholderText("Ajouter une tâche...")
        self.btn_remove = QPushButton("Tout supprimer")

        self.main_layout.addWidget(self.lw_list)
        self.main_layout.addWidget(self.le_add)
        self.main_layout.addWidget(self.btn_remove)

        self.btn_remove.clicked.connect(self.on_btn_remove_clicked)
        self.le_add.returnPressed.connect(self.on_le_add_return_pressed)
        self.lw_list.doubleClicked.connect(self.on_lw_list_double_clicked)

    def on_lw_list_double_clicked(self):
        self.lw_list.takeItem(self.lw_list.currentRow())


    def on_btn_remove_clicked(self):
        self.lw_list.clear()

    def on_le_add_return_pressed(self):
        self.lw_list.addItem(self.le_add.text())
        self.le_add.clear()

app = QApplication()

main_window = MainWindow()
main_window.show()

app.exec()

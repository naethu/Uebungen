import os
import sys
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QDateEdit
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QAction, QGridLayout, QLabel, \
    QSpinBox, QLineEdit, QPushButton, QComboBox, QWidget


class GUI(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("GUI-Programmierung")

        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        save_action = QAction("Save", self)
        save_action.triggered.connect(self.save_data)
        file_menu.addAction(save_action)

        quit_action = QAction("Quit", self)
        quit_action.triggered.connect(self.quit_application)
        file_menu.addAction(quit_action)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QGridLayout()

        #Mac
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        first_name_label = QLabel("Vorname:")
        layout.addWidget(first_name_label, 0, 0)
        self.first_name_edit = QLineEdit()
        layout.addWidget(self.first_name_edit, 0, 1)

        last_name_label = QLabel("Name:")
        layout.addWidget(last_name_label, 1, 0)
        self.last_name_edit = QLineEdit()
        layout.addWidget(self.last_name_edit, 1, 1)

        birthday_label = QLabel("Geburtstag:")
        layout.addWidget(birthday_label, 2, 0)
        self.birthday_edit = QDateEdit()
        self.birthday_edit.setMaximumDate(QDate.currentDate())
        self.birthday_edit.setDisplayFormat("dd/MM/yyyy")
        self.birthday_edit.setSpecialValueText("Jahr")
        layout.addWidget(self.birthday_edit, 2, 1)

        address_label = QLabel("Adresse:")
        layout.addWidget(address_label, 3, 0)
        self.address_edit = QLineEdit()
        layout.addWidget(self.address_edit, 3, 1)

        postal_code_label = QLabel("Postleitzahl:")
        layout.addWidget(postal_code_label, 4, 0)
        self.postal_code_edit = QLineEdit()
        layout.addWidget(self.postal_code_edit, 4, 1)

        city_label = QLabel("Ort:")
        layout.addWidget(city_label, 5, 0)
        self.city_edit = QLineEdit()
        layout.addWidget(self.city_edit, 5, 1)

        country_label = QLabel("Land:")
        layout.addWidget(country_label, 6, 0)
        self.country_combo = QComboBox()
        self.country_combo.addItems(["Schweiz", "Deutschland", "Österreich"])
        layout.addWidget(self.country_combo, 6, 1)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_data)
        layout.addWidget(save_button, 7, 0, 1, 2)

        central_widget.setLayout(layout)

    def save_data(self):
        data = [self.first_name_edit.text(), self.last_name_edit.text(), self.birthday_edit.date().toString("MM/dd/yyyy"),
            self.address_edit.text(), self.postal_code_edit.text(), self.city_edit.text(),
            self.country_combo.currentText()]

        with open("output.txt", "w") as f:
            f.write(",".join(data))

    def quit_application(self):
        QApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    gui.raise_()
<<<<<<< Updated upstream
    sys.exit(app.exec_())
=======
    sys.exit(app.exec_())
>>>>>>> Stashed changes

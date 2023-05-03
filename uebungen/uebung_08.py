import sys
from matplotlib.figure import Figure
from PyQt5.QtWidgets import *
from PyQt5.uic import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np


class PlotWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)

class PolyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Polynomieller Plotter")

        self.coefficients_label = QLabel("Geben Sie die Polynomkoeffizienten ein:")
        self.coefficients_edit = QLineEdit()
        self.start_label = QLabel("Startwert:")
        self.start_edit = QLineEdit()
        self.end_label = QLabel("Endwert:")
        self.end_edit = QLineEdit()
        self.points_label = QLabel("Anzahl der Punkte:")
        self.points_edit = QLineEdit()
        self.plot_button = QPushButton("Plotten")
        self.color_label = QLabel("Wählen Sie die Plotfarbe:")
        self.color_combo = QComboBox()
        self.color_combo.addItems(["schwarz", "rot", "blau", "gruen"])

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.coefficients_label)
        self.layout.addWidget(self.coefficients_edit)
        self.layout.addWidget(self.start_label)
        self.layout.addWidget(self.start_edit)
        self.layout.addWidget(self.end_label)
        self.layout.addWidget(self.end_edit)
        self.layout.addWidget(self.points_label)
        self.layout.addWidget(self.points_edit)
        self.layout.addWidget(self.color_label)
        self.layout.addWidget(self.color_combo)
        self.layout.addWidget(self.plot_button)
        self.setLayout(self.layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Polynomieller Plotter")

        self.plot_widget = PlotWidget()
        self.setCentralWidget(self.plot_widget)

        self.poly_widget = PolyWindow()
        self.setCentralWidget(self.poly_widget)
        self.poly_widget.plot_button.clicked.connect(self.plot)

    def plot(self):
        coeffs = self.poly_widget.coefficients_edit.text()
        coeffs = coeffs.split(',')
        coeffs = [float(c) for c in coeffs]

        f = np.poly1d(coeffs)

        start = float(self.poly_widget.start_edit.text())
        end = float(self.poly_widget.end_edit.text())
        num_points = int(self.poly_widget.points_edit.text())
        x = np.linspace(start, end, num_points)
        y = f(x)

        color = self.poly_widget.color_combo.currentText()

        self.plot_widget.canvas.ax.clear()
        self.plot_widget.canvas.ax.plot(x, y, color=color)
        self.plot_widget.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

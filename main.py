import sys
import numpy as np
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from PyQt6 import uic
import pyqtgraph as pg


class PlotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("plotter.ui", self)

        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setLabel('left', 'f(x)')
        self.plot_widget.setLabel('bottom', 'x')
        self.plot_widget.showGrid(x=True, y=True)
        layout = QVBoxLayout(self.graphContainer)
        layout.addWidget(self.plot_widget)

        self.plotButton.clicked.connect(self.plot)

    def plot(self):
        self.errorLabel.setText("")

        expr = self.functionEdit.text().strip()
        if not expr:
            self.errorLabel.setText("введите функцию")
            return

        x_min = self.xMinSpin.value()
        x_max = self.xMaxSpin.value()
        if x_min >= x_max:
            self.errorLabel.setText("нижняя граница должна быть меньше верхней")
            return

        x = np.linspace(x_min, x_max, 1000)
        try:
            y = eval(expr)
            if not isinstance(y, np.ndarray):
                y = np.full_like(x, float(y))
        except Exception as e:
            self.errorLabel.setText(f"Ошибка: {e}")
            return

        mask = np.isfinite(y)
        if not mask.any():
            self.errorLabel.setText("Нет конечных значений в данном диапазоне")
            return

        self.plot_widget.clear()
        self.plot_widget.plot(x[mask], y[mask], pen="r")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PlotWindow()
    window.show()
    sys.exit(app.exec())

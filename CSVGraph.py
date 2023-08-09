import csv
import sys, os
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot
from PySide2 import QtGui, QtCore, QtWidgets


class CSVGraph(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle("CSV Graph")
        self.setWindowFlags(self.windowFlags()^QtCore.Qt.WindowContextHelpButtonHint)
        self.show()
        self.resize(200,300)
        main_lay = QtWidgets.QVBoxLayout()
        horizontal_lay = QtWidgets.QHBoxLayout()

        self.path_line_edit = QtWidgets.QLineEdit()
        self.path_line_edit.setReadOnly(True)
        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow("Path: ", self.path_line_edit)
        horizontal_lay.addLayout(form_layout)

        self.browse_btn = QtWidgets.QPushButton("Browse", clicked=self.browse_btn_clk)
        horizontal_lay.addWidget(self.browse_btn)
        main_lay.addLayout(horizontal_lay)

        self.calculate_btn = QtWidgets.QPushButton("Calculate", clicked=self.calculate_btn_clk)
        main_lay.addWidget(self.calculate_btn)

        self.graph_widget = pg.PlotWidget()
        main_lay.addWidget(self.graph_widget)
        self.setLayout(main_lay)
    
    def browse_btn_clk(self):
        folder_diag = QtWidgets.QFileDialog.getExistingDirectory(self, 'Folder Selection')
        self.path_line_edit.setText(folder_diag)
    
    def calculate_btn_clk(self):
        calculation = []
        csv_path = self.path_line_edit.text()
        if os.path.exists(csv_path):
            csv_files = os.listdir(csv_path)
        for i in csv_files:
            i = os.path.join(csv_path, i)
            with open(i) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter = ',')
                for j in csv_reader:
                    mul = int(j[0])*int(j[1])
                    calculation.append(mul)

        self.graph_widget.plot(range(len(calculation)), calculation)
                    
def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = CSVGraph()
    sys.exit(app.exec_())

run()
app = QtWidgets.QApplication(sys.argv)

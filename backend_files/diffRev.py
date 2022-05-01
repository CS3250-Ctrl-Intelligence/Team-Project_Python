from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QAbstractTableModel
import sys
import os

from matplotlib.ft2font import HORIZONTAL
from dbscript import Database_Functions

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data


    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self._data[index.row()][index.column()]

        if role == Qt.ItemDataRole.ForegroundRole and index.column() == 0:
            value = self._data[index.row()][index.column()]

            return QtGui.QColor('white')

        if role == Qt.ItemDataRole.ForegroundRole and index.column() == 1:
            value = self._data[index.row()][index.column()]

            if (
                (isinstance(value, int) or isinstance(value, float))
                and value < 0
            ):
                return QtGui.QColor('red')

        if role == Qt.ItemDataRole.ForegroundRole and index.column() == 1:
            value = self._data[index.row()][index.column()]

            if (
                (isinstance(value, int) or isinstance(value, float))
                and value > 0
            ):
                return QtGui.QColor('green')

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.table = QtWidgets.QTableView()

        data = Database_Functions.getDiffRev()
        self.model = TableModel(data)
        self.table.setModel(self.model)
        self.setCentralWidget(self.table)
        self.table.setStyleSheet('QHeaderView::section { color:white; background-color:#16191d; }' 'QTableCornerButton::section { background-color:#16191d; }')
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setVisible(False)

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.setFixedHeight(300)
    main.setFixedWidth(250)
    main.setStyleSheet('background-color: #16191d; border-color: #16191d;')

    main.show()
    app.exec_()


if __name__ == '__main__':
    main()
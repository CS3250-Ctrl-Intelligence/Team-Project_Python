from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys
import os
from dbscript import Database_Functions


class MainWindow(QtWidgets.QMainWindow):
    '''This class implements main window, displays window/info for threeOrders'''

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        date, amount = Database_Functions.getThreeOrders()
        # plot data: x, y values
        self.graphWidget.setBackground('#16191d')
        pen = pg.mkPen(color=(255, 85, 0), width=5)
        self.graphWidget.plot(date, amount, pen=pen, symbol='+', symbolSize=10)
        self.graphWidget.setTitle("# of Orders by week (3-Month)", color="w", size="25pt")
        styles ={'color':'#FFFFFF', 'font-size':'20px'}
        self.graphWidget.setLabel('left', '# of Orders', **styles)
        self.graphWidget.setLabel('bottom', 'Week of Year', **styles)
        self.graphWidget.showGrid(x=True, y=True)

def main():
    '''Executes main'''
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.exec_()


if __name__ == '__main__':
    main()
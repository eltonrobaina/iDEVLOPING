#import Regression3D
#import Regression2D
from PyQt5.QtWidgets import (QApplication, QMessageBox, QMainWindow, QVBoxLayout, QAction, QFileDialog, QDialog)
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUiType
from os.path import dirname, realpath, join
from sys import argv
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from mpl_toolkits.mplot3d import axis3d ,axes3d
import matplotlib.pyplot as plt

scriptDir = dirname(realpath(__file__))
FROM_MAIN, _ = loadUiType(join(dirname(__file__), "mainwindow.ui"))

class Main(QMainWindow, FROM_MAIN):
    def __init__(self, parent=FROM_MAIN):
        super(Main, self).__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.ToolBar()
        self.sc = myCanvas()
        self.l=QVBoxLayout(self.frame)
        self.l.addWidget(self.sc)

    def BrowseFolder(self):
        global filename
        #filename, = QFileDialog.getOpenFileName((self,"Open","","Text Files (*.txt);; All Files (*)"))
        filename, _ = QFileDialog.getOpenFileName(self, "Open", "", "Text Files (*.txt);;All Files (*)")
        print("O DIRETORIO E ESTE: " + filename)

    def ToolBar(self):
        #AddFile = QAction(QIcon('images.png'),'Add File',self)
        AddFile = QAction(QIcon('icons/images.png'),'A',self) # add icon for toolbar button
        #AddFile.triggered.connect(self.open_sheet)
        AddFile.triggered.connect(self.BrowseFolder)
        self.toolBar = self.addToolBar('Add data File')
        self.toolBar.addAction(AddFile)
        addPlot = QAction(QIcon('icons/scatter.png'),'', self)
        addPlot.triggered.connect(self.Plot)
        self.toolBar.addAction(addPlot)

    def Get_List(self, filename):
        with open(filename) as f:
            array = []
            for line in f:
                array.append([float(x) for x in line.split()])
            #print(array)
            Xarray = []
            Yarray = []
            Zarray = []
            for i in range (len(array)):
                Xarray.append(array[i][0])
                Yarray.append(array[i][1])
                Zarray.append(array[i][2])
            #print(Xarray)

        return Xarray,Yarray,Zarray

    def Plot(self):
        x,y,z = self.Get_List(filename) ##get
        self.sc.plot(x,y,z)



class myCanvas(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        FigureCanvas.__init__(self, self.fig)

    def plot(self, xarray, yarray, zarray):
        self.fig.clear()
        self.ax=self.fig.add_subplot(111, projection = '3d')
        #self.ax.plot_trisurf(xarray,yarray,zarray, color = 'red', alpha=0, edgecolor = 'red', linewidth = 0.1, """antialised = True""", shade=1)
        self.ax.plot_trisurf(xarray,yarray,zarray, color = 'red', alpha=0, edgecolor = 'red', linewidth = 0.1, shade=1)
        self.ax.plot(xarray, yarray, zarray, 'or')
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        self.draw()

    def plot2(self, xarray, yarray):
        self.fig.clear()
        self.axe = self.fig.add_subplot(111)
        self.axe.plot(xarray, yarray, 'ok')
        self.axe.plot(xarray, yarray, 'r-')
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        self.draw()

def main():
    app = QApplication(argv)
    window = Main()
    # window.showFullScreen() # Start at position full screen
    window.showMaximized()  # Start position max screen
    app.exec_()


if __name__ == '__main__':
    main()










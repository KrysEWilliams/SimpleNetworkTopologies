"""
This is the module SimpleNetworkTopologies.

It is used to visualize simple computer network topologies.
"""

import sys
import pyqtgraph as pg
from PyQt5 import QtGui, QtWidgets

import networks as nw

VIEWERWIDTH = 3  # half-width of viewer


class TextDisplay(QtWidgets.QLabel):
    """ displays text """
    def __init__(self):
        super(TextDisplay, self).__init__()

        self.setText("This is sample text \n"
        "\n"
        "You can do print whatever you want here")


class NetworkViewer(pg.GraphicsLayoutWidget):
    """ main class for viewing networks """
    def __init__(self):
        super(NetworkViewer, self).__init__()
        self.v = self.addViewBox()
        self.v.setAspectLocked()
        self.v.setLimits(xMin=-VIEWERWIDTH, xMax=VIEWERWIDTH,
                         yMin=-VIEWERWIDTH, yMax=VIEWERWIDTH)
        self.v.setXRange(-VIEWERWIDTH, VIEWERWIDTH)
        self.v.setYRange(-VIEWERWIDTH, VIEWERWIDTH)

        self.generic = nw.generic_network()
        self.v.addItem(self.generic)

        # initialize all other networks
        N_ring = 5   # change this value to affect number of nodes in Ring
        self.ring = nw.Ring(N_ring)

        self.bus = nw.Bus()

        self.fullyconnected = nw.FullyConnected()

        self.mesh = nw.Mesh()

        self.star = nw.Star()

    def show_network(self, name):
        self.v.clear()

        if name == "Generic":
            self.v.addItem(self.generic)
        elif name == "Ring":
            self.v.addItem(self.ring)
        elif name == "Bus":
            self.v.addItem(self.bus)
        elif name == "FullyConnected":
            self.v.addItem(self.fullyconnected)
        elif name == "Mesh":
            self.v.addItem(self.mesh)
        elif name == "Star":
            self.v.addItem(self.star)

class networkChooser(QtWidgets.QWidget):
    """ main settings class for which network to view """
    def __init__(self, parent=None):
        super(networkChooser, self).__init__(parent)

        layout = QtWidgets.QVBoxLayout()
        solution_label = QtGui.QLabel("Choose which network to view")
        self.viewGenericRadio = QtGui.QRadioButton("Generic")
        self.viewRingRadio = QtGui.QRadioButton("Ring")
        self.viewBusRadio = QtGui.QRadioButton("Bus")
        self.viewStarRadio = QtGui.QRadioButton("Star")
        self.viewMeshRadio = QtGui.QRadioButton("Mesh")
        self.viewFullyConnectedRadio = QtGui.QRadioButton("FullyConnected")

        self.viewGenericRadio.setChecked(True)

        layout.addWidget(solution_label)
        layout.addWidget(self.viewGenericRadio)
        layout.addWidget(self.viewRingRadio)
        layout.addWidget(self.viewBusRadio)
        layout.addWidget(self.viewStarRadio)
        layout.addWidget(self.viewMeshRadio)
        layout.addWidget(self.viewFullyConnectedRadio)

        self.setLayout(layout)


class Settings(QtWidgets.QWidget):
    """ main settings class """
    def __init__(self, parent=None):
        super(Settings, self).__init__(parent)

        layout = QtWidgets.QVBoxLayout()

        self.nc = networkChooser()

        layout.addWidget(self.nc)
        layout.addStretch(1)

        self.setLayout(layout)


class MainWindow(QtWidgets.QMainWindow):
    """ main class for SimpleNetworkTopologies """
    def __init__(self):
        super(MainWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('SimpleNetworkTopologies')
        self.resize(1000, 600)

        self.text = TextDisplay()
        self.nv = NetworkViewer()
        self.sl = Settings()

        left_l = QtWidgets.QVBoxLayout()
        left_l.addWidget(self.text)
        left_l.addWidget(self.nv)
        self.left_w = QtWidgets.QWidget()
        self.left_w.setLayout(left_l)

        main_layout = QtWidgets.QHBoxLayout()
        main_layout.addWidget(self.left_w)
        main_layout.addWidget(self.sl)

        main_widget = QtWidgets.QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # connects settings to view window
        self.sl.nc.viewGenericRadio.toggled.connect(lambda: self.nv.show_network("Generic"))
        self.sl.nc.viewRingRadio.toggled.connect(lambda: self.nv.show_network("Ring"))
        self.sl.nc.viewBusRadio.toggled.connect(lambda: self.nv.show_network("Bus"))
        self.sl.nc.viewFullyConnectedRadio.toggled.connect(lambda: self.nv.show_network("FullyConnected"))
        self.sl.nc.viewMeshRadio.toggled.connect(lambda: self.nv.show_network("Mesh"))
        self.sl.nc.viewStarRadio.toggled.connect(lambda: self.nv.show_network("Star"))


def main():
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('SimpleNetworkTopologies')

    main = MainWindow()
    main.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

"""
This is the module SimpleNetworkTopologies.

It is used to visualize simple computer network topologies.
"""

import sys
import pyqtgraph as pg
from PyQt5 import QtGui, QtWidgets

import networks as nw

VIEWERWIDTH = 3  # half-width of viewer
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600


class TextDisplay(QtWidgets.QLabel):
    """ displays text """
    def __init__(self):
        super(TextDisplay, self).__init__()

        # Krystal: define 6 string variables
        self.example_text = "This is sample text\n" \
        "\n" \
        "You can do print whatever you want here"

        self.setText(self.example_text)

         # Krystal: define 6 string variables
        self.generic_text = "Generic Topologies are just basic setups of any number of nodes/ Computers that are connected in no specific way, and can be changed to accommodate different connections.\n" \
        "\n" \
        "You can do print whatever you want here"

        self.ring_text = "Ring Topologies are made of nodes that are connected by edges that pass around a token to receive connection. This is helpful when a Network needs to flow all in one directiont. "
    
        self.bus_text = "The Bus Networking topology is built using multiple nodes/ Computers connected to a switch or hub by a single connection cable.This is not too common due to its ability to run slower than normal, because of a high influx of connections all through one single cable."
    
        self.fullyconnected_text = "FullyConnected topologies are made of a group of nodes that are each connected to every other node/computer on the network. This allows for fast connections within  a network simultaneously. "

        self.mesh_text = " Mesh is helpful to attend to different needs of a network. Like a hybrid of Generic and Fully Connected topologies that can be used to enstate a network with mixed needs."

        self.star_text = "Star Networking topologies consist of each separate computer/ node that separately connect to a central switch or hub. This is a common topology that allows for continued use, if for some reason one cable or connection fails. "
        
        
    def show_text(self, name):
        if name == "Generic":
            self.setText(self.generic_text)
        elif name == "Ring":
            self.setText(self.ring_text)
        elif name == "Bus":
            self.setText(self.bus_text)
        elif name == "FullyConnected":
            self.setText(self.fullyconnected_text)
        elif name == "Mesh":
            self.setText(self.mesh_text)
        elif name == "Star":
            self.setText(self.star_text)


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


class IntroWidget(QtWidgets.QWidget):
    """ intro widget class for SimpleNetworkTopologies """
    def __init__(self):
        super(IntroWidget, self).__init__()

        self.intro_text = QtGui.QLabel("This is a label")
        self.enter_main_btn = QtWidgets.QPushButton("This is a button")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.intro_text)
        layout.addWidget(self.enter_main_btn)

        self.setLayout(layout)


class MainWidget(QtWidgets.QWidget):
    """ main window for SimpleNetworkTopologies """
    def __init__(self):
        super(MainWidget, self).__init__()

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

        self.setLayout(main_layout)

        # connects settings to view window
        self.sl.nc.viewGenericRadio.toggled.connect(
            lambda: self.nv.show_network("Generic"))
        self.sl.nc.viewRingRadio.toggled.connect(
            lambda: self.nv.show_network("Ring"))
        self.sl.nc.viewBusRadio.toggled.connect(
            lambda: self.nv.show_network("Bus"))
        self.sl.nc.viewFullyConnectedRadio.toggled.connect(
            lambda: self.nv.show_network("FullyConnected"))
        self.sl.nc.viewMeshRadio.toggled.connect(
            lambda: self.nv.show_network("Mesh"))
        self.sl.nc.viewStarRadio.toggled.connect(
            lambda: self.nv.show_network("Star"))

        # connects settings to text display
        self.sl.nc.viewGenericRadio.toggled.connect(
            lambda: self.text.show_text("Generic"))
        self.sl.nc.viewRingRadio.toggled.connect(
            lambda: self.text.show_text("Ring"))
        self.sl.nc.viewBusRadio.toggled.connect(
            lambda: self.text.show_text("Bus"))
        self.sl.nc.viewFullyConnectedRadio.toggled.connect(
            lambda: self.text.show_text("FullyConnected"))
        self.sl.nc.viewMeshRadio.toggled.connect(
            lambda: self.text.show_text("Mesh"))
        self.sl.nc.viewStarRadio.toggled.connect(
            lambda: self.text.show_text("Star"))


class MainWindow(QtWidgets.QMainWindow):
    """ main window for SimpleNetworkTopologies """
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('SimpleNetworkTopologies')
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.setWindowIcon(QtGui.QIcon("images/out.png"))

        # load in different 'main windows'
        self.intro_widget = IntroWidget()
        self.main_widget = MainWidget()

        # this needs to switch based on clicking a button
        self.setCentralWidget(self.intro_widget)

        self.intro_widget.enter_main_btn.clicked.connect(self.switch_to_main)

    def switch_to_main(self):
        self.setCentralWidget(self.main_widget)

        # define status bar and toolbar here


def main():
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('SimpleNetworkTopologies')

    main = MainWindow()
    main.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

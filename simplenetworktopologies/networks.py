"""
.. module:: networks
   :synopsis: defines functions and classes for creating networks.
"""

import numpy as np
import pyqtgraph as pg
from PyQt5 import QtCore


class Network(pg.GraphItem):
    """ Class for drawing and storing/computing network properties

    Derived from pyqtgraph examples CustomGraphItem.py found at
    https://github.com/pyqtgraph/pyqtgraph/blob/master/examples/
    CustomGraphItem.py """
    def __init__(self):
        self.name = "No Name"
        self.dragPoint = None
        self.dragOffset = None
        self.textItems = []
        pg.GraphItem.__init__(self)
        self.scatter.sigClicked.connect(self.clicked)

    def setData(self, **kwds):
        self.text = kwds.pop('text', [])
        self.data = kwds

        if 'pos' in self.data:
            self.npts = self.data['pos'].shape[0]
            self.data['data'] = np.empty(self.npts, dtype=[('index', int)])
            self.data['data']['index'] = np.arange(self.npts)
        self.setTexts(self.text)
        self.updateGraph()

    def setTexts(self, text):
        for i in self.textItems:
            i.scene().removeItem(i)
        self.textItems = []
        for t in text:
            item = pg.TextItem(t)
            self.textItems.append(item)
            item.setParentItem(self)

    def updateGraph(self):
        pg.GraphItem.setData(self, **self.data)
        for i, item in enumerate(self.textItems):
            item.setPos(*self.data['pos'][i])

    def mouseDragEvent(self, ev):
        if ev.button() != QtCore.Qt.LeftButton:
            ev.ignore()
            return

        if ev.isStart():
            # We are already one step into the drag.
            # Find the point(s) at the mouse cursor when the button was first
            # pressed:
            pos = ev.buttonDownPos()
            pts = self.scatter.pointsAt(pos)
            if len(pts) == 0:
                ev.ignore()
                return
            self.dragPoint = pts[0]
            ind = pts[0].data()[0]
            self.dragOffset = self.data['pos'][ind] - pos
        elif ev.isFinish():
            self.dragPoint = None
            return
        else:
            if self.dragPoint is None:
                ev.ignore()
                return

        ind = self.dragPoint.data()[0]
        self.data['pos'][ind] = ev.pos() + self.dragOffset
        self.updateGraph()
        ev.accept()

    def clicked(self, pts):
        print("clicked: %s" % pts)


def SwitchSymbol():
    """Symbol for switch device."""
    valves = np.asarray([
                    [-0.9782608695652174, -0.49173553719008334],
                    [0.9869565217391303, -0.4834710743801658],
                    [0.9913043478260866, 0.49173553719008245],
                    [-1, 0.475206611570248],
                    [-0.991304347826087, 0.012396694214875659],
                    [-0.7217391304347827, 0.037190082644627864],
                    [-0.7217391304347827, -0.11983471074380159],
                    [-0.4652173913043478, -0.11157024793388448],
                    [-0.4782608695652175, 0.02892561983471076],
                    [-0.40869565217391324, 0.02892561983471076],
                    [-0.40869565217391324, -0.11157024793388448],
                    [-0.15652173913043488, -0.10330578512396693],
                    [-0.16086956521739137, 0.037190082644627864],
                    [-0.16086956521739137, 0.037190082644627864],
                    [-0.0913043478260871, 0.045454545454545414],
                    [-0.10000000000000009, -0.09504132231404938],
                    [0.15652173913043477, -0.08677685950413272],
                    [0.15652173913043477, 0.02892561983471076],
                    [0.21739130434782594, 0.037190082644627864],
                    [0.21304347826086945, -0.08677685950413272],
                    [0.4739130434782608, -0.09504132231404938],
                    [0.4739130434782608, 0.02066115702479321],
                    [0.5478260869565217, 0.037190082644627864],
                    [0.5434782608695652, -0.09504132231404938],
                    [0.8043478260869565, -0.12809917355371914],
                    [0.8304347826086955, 0.2603305785123964],
                    [0.7304347826086954, 0.2520661157024793],
                    [0.7304347826086954, 0.2933884297520657],
                    [0.6347826086956521, 0.2933884297520657],
                    [0.6347826086956521, 0.23553719008264418],
                    [0.5478260869565217, 0.24380165289256173],
                    [0.5478260869565217, 0.06198347107438007],
                    [0.4739130434782608, 0.05371900826446252],
                    [0.4826086956521738, 0.23553719008264418],
                    [0.3999999999999997, 0.23553719008264418],
                    [0.3999999999999997, 0.2851239669421486],
                    [0.3043478260869563, 0.2768595041322315],
                    [0.3086956521739128, 0.22727272727272707],
                    [0.21739130434782594, 0.23553719008264418],
                    [0.21739130434782594, 0.06198347107438007],
                    [0.16086956521739126, 0.05371900826446252],
                    [0.16086956521739126, 0.23553719008264418],
                    [0.08260869565217388, 0.24380165289256173],
                    [0.08260869565217388, 0.2851239669421486],
                    [-0.013043478260869712, 0.2851239669421486],
                    [-0.013043478260869712, 0.24380165289256173],
                    [-0.0913043478260871, 0.24380165289256173],
                    [-0.0913043478260871, 0.07851239669421473],
                    [-0.15652173913043488, 0.07851239669421473],
                    [-0.15652173913043488, 0.23553719008264418],
                    [-0.23478260869565226, 0.23553719008264418],
                    [-0.23478260869565226, 0.2768595041322315],
                    [-0.33043478260869585, 0.2768595041322315],
                    [-0.33043478260869585, 0.23553719008264418],
                    [-0.40869565217391324, 0.22727272727272707],
                    [-0.40434782608695663, 0.05371900826446252],
                    [-0.4739130434782609, 0.05371900826446252],
                    [-0.482608695652174, 0.21900826446280997],
                    [-0.5521739130434783, 0.22727272727272707],
                    [-0.5565217391304349, 0.2851239669421486],
                    [-0.6478260869565218, 0.26859504132231393],
                    [-0.6478260869565218, 0.22727272727272707],
                    [-0.7217391304347827, 0.22727272727272707],
                    [-0.7217391304347827, 0.07024793388429762]
                    ])
    new_valves = 0.7*valves

    return pg.arrayToQPath(new_valves[:, 0], new_valves[:, 1], connect='all')


def ComputerSymbol():
    """Symbol for computer device.

    Taken from: https://en.wikipedia.org/wiki/File:Simple_Monitor_Icon.svg
    and https://apps.automeris.io/wpd/
    """
    valves = np.asarray([
                [0.063, 0.91],
                [0.066, 0.93],
                [0.075, 0.96],
                [0.10, 0.98],
                [0.12, 0.99],
                [0.90, 0.99],
                [0.93, 0.98],
                [0.95, 0.96],
                [0.96, 0.94],
                [0.96, 0.92],
                [0.94, 0.24],
                [0.93, 0.21],
                [0.91, 0.19],
                [0.88, 0.17],
                [0.63, 0.17],
                [0.62, 0.068],
                [0.81, 0.063],
                [0.83, 0.054],
                [0.83, 0.041],
                [0.83, 0.024],
                [0.82, 0.0051],
                [0.81, -0.0013],
                [0.15, 0.0015],
                [0.14, 0.010],
                [0.13, 0.021],
                [0.13, 0.040],
                [0.14, 0.059],
                [0.16, 0.068],
                [0.34, 0.067],
                [0.35, 0.17],
                [0.35, 0.22],
                [0.87, 0.22],
                [0.88, 0.23],
                [0.89, 0.24],
                [0.91, 0.92],
                [0.91, 0.93],
                [0.89, 0.93],
                [0.13, 0.94],
                [0.12, 0.93],
                [0.11, 0.91],
                [0.089, 0.25],
                [0.095, 0.24],
                [0.11, 0.23],
                [0.35, 0.22],
                [0.35, 0.18],
                [0.090, 0.18],
                [0.070, 0.19],
                [0.054, 0.21],
                [0.038, 0.24]
                ])
    ones = np.ones((49, 2), dtype=float)
    new_valves = (valves - 0.5*ones)

    return pg.arrayToQPath(new_valves[:, 0], new_valves[:, 1], connect='all')


def get_sizes(symbols):
    N = len(symbols)
    sizes = np.zeros(N)
    for ti in range(N):
        if symbols[ti] == 's':
            sizes[ti] = 0.1
        else:
            sizes[ti] = 0.5

    return sizes


class generic_network(Network):
    """Class for generic network."""
    def __init__(self):
        #super(generic_network, self).__init__()
        Network.__init__(self)
        self.name = "Generic"

        pos = self.get_positions()
        adj = self.get_edges()
        texts = self.get_texts()
        symbols = [ComputerSymbol(),
                   ComputerSymbol(),
                   's',
                   's',
                   's',
                   SwitchSymbol(),
                   ComputerSymbol()]
        sizes = get_sizes(symbols)

        self.setData(pos=pos, adj=adj, symbol=symbols, pxMode=False,
                     size=sizes, text=texts)

    def get_positions(self):
        return np.array([
                        [-2, 1],
                        [-2, -1],
                        [-2, 0],
                        [-1, 0],
                        [0, 0],
                        [1, 0],
                        [0, 1]
                        ], dtype=float)

    def get_edges(self):
        return np.array([
                        [0, 2],
                        [1, 2],
                        [2, 3],
                        [3, 4],
                        [4, 5],
                        [4, 6]
                        ])

    def get_texts(self):
        return ["Point %d" % i for i in range(7)]

    def get_symbols(self):
        return ['s', 's', 'o', 'o', 'o', '+', 's']

    def get_sizestest(self, symbols):
        N = len(symbols)
        sizes = np.zeros(N)
        for ti in range(N):
            if symbols[ti] == 's':
                sizes[ti] = 0.5
            elif symbols[ti] == 'o':
                sizes[ti] = 0.1
            elif symbols[ti] == '+':
                sizes[ti] = 0.5

        return sizes


class Ring(Network):
    """Class for Ring network."""
    def __init__(self, N):
        super(Ring, self).__init__()
        self.name = "Ring"

        pos = self.get_positions(N)
        adj = self.get_edges(N)
        symb = self.get_symbols(N)
        texts = self.get_texts(N)
        sizes = get_sizes(symb)

        self.setData(pos=pos, adj=adj, symbol=symb, pxMode=False,
                     size=sizes, text=texts)

    def get_positions(self, N):
        radius = 2
        pos = np.zeros((N, 2))
        theta = np.linspace(0, 2*np.pi, num=N+1)
        for ti in range(N):
            pos[ti, 0] = radius*np.cos(theta[ti])
            pos[ti, 1] = radius*np.sin(theta[ti])

        return pos

    def get_edges(self, N):
        edges = np.zeros((N, 2), dtype=int)
        for ti in range(N):
            edges[ti, 0] = ti
            edges[ti, 1] = ti+1

        edges[N-1, 0] = N-1
        edges[N-1, 1] = 0

        return edges

    def get_texts(self, N):
        return ["Point %d" % i for i in range(N)]

    def get_symbols(self, N):
        return ['s']*N

    def get_sizes(self, N):
        symb = self.get_symbols(N)
        sizes = np.zeros(N)
        for ti in range(N):
            if symb[ti] == 's':
                sizes[ti] = 0.5
            elif symb[ti] == 'o':
                sizes[ti] = 0.1
            elif symb[ti] == '+':
                sizes[ti] = 0.5

        return sizes


class Bus(Network):
    """Class for Bus network."""
    def __init__(self):
        super(Bus, self).__init__()
        self.name = "Bus"

        pos = self.get_positions()
        adj = self.get_edges()
        symb = self.get_symbols()
        texts = self.get_texts()
        sizes = get_sizes(symb)

        self.setData(pos=pos, adj=adj, symbol=symb, pxMode=False,
                     size=sizes, text=texts)

    def get_positions(self):
        return np.array([
                        [-1, 1],
                        [-2, 0],
                        [-1, 0],
                        [0, 0],
                        [1, 0],
                        [0, 1]
                        ], dtype=float)

    def get_edges(self):
        return np.array([
                        [0, 2],
                        [1, 2],
                        [2, 3],
                        [3, 5],
                        [3, 4]
                        ])

    def get_texts(self):
        return ["Point %d" % i for i in range(6)]

    def get_symbols(self):
        return ['s', 's', 'o', 'o', 'o', 's']


class Mesh(Network):
    """Class for Mesh network."""
    def __init__(self):
        super(Mesh, self).__init__()
        self.name = "Mesh"

        pos = self.get_positions()
        adj = self.get_edges()
        symb = self.get_symbols()
        texts = self.get_texts()
        sizes = get_sizes(symb)

        self.setData(pos=pos, adj=adj, symbol=symb, pxMode=False,
                     size=sizes, text=texts)

    def get_positions(self):
        return np.array([
                        [-1, 1],
                        [-2, 0],
                        [-1, 0],
                        [0, 0],
                        [1, 0],
                        [0, 1]
                        ], dtype=float)

    def get_edges(self):
        return np.array([
                        [0, 2],
                        [1, 2],
                        [2, 3],
                        [3, 5],
                        [3, 4],
                        [0, 1],
                        [4, 5]
                        ])

    def get_texts(self):
        return ["Point %d" % i for i in range(6)]

    def get_symbols(self):
        return ['s', 's', 'o', 'o', 'o', 's']


class Star(Network):
    """Class for star network."""
    def __init__(self):
        super(Star, self).__init__()
        self.name = "Star"

        pos = self.get_positions()
        adj = self.get_edges()
        symb = self.get_symbols()
        texts = self.get_texts()
        sizes = get_sizes(symb)

        self.setData(pos=pos, adj=adj, symbol=symb, pxMode=False,
                     size=sizes, text=texts)

    def get_positions(self):
        return np.array([
                        [0, 0],
                        [-1, 0],
                        [1, 0],
                        [0, -1],
                        [0, 1]
                        ], dtype=float)

    def get_edges(self):
        return np.array([
                        [0, 1],
                        [0, 2],
                        [0, 3],
                        [0, 4]
                        ])

    def get_texts(self):
        return ["Point %d" % i for i in range(5)]

    def get_symbols(self):
        return ['o', 's', 's', 's', 's']


class FullyConnected(Network):
    """Class for fully connected network."""
    def __init__(self):
        super(FullyConnected, self).__init__()
        self.name = "FullyConnected"

        pos = self.get_positions()
        adj = self.get_edges()
        symb = self.get_symbols()
        texts = self.get_texts()
        sizes = get_sizes(symb)

        self.setData(pos=pos, adj=adj, symbol=symb, pxMode=False,
                     size=sizes, text=texts)

    def get_positions(self):
        return np.array([
                        [-1, 0],
                        [1, 0],
                        [0, -1],
                        [0, 1]
                        ], dtype=float)

    def get_edges(self):
        return np.array([
                        [0, 1],
                        [0, 2],
                        [0, 3],
                        [1, 2],
                        [1, 3],
                        [2, 3]
                        ])

    def get_texts(self):
        return ["Point %d" % i for i in range(4)]

    def get_symbols(self):
        return ['s', 's', 's', 's']

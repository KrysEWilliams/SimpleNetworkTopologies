import numpy as np
import pyqtgraph as pg
from PyQt5 import QtGui, QtWidgets, QtCore


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


def get_sizes(symbols):
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


class generic_network(Network):
    def __init__(self):
        super(generic_network, self).__init__()
        self.name = "Generic"

        pos = self.get_positions()
        adj = self.get_edges()
        symb = self.get_symbols()
        texts = self.get_texts()
        sizes = get_sizes(symb)

        self.setData(pos=pos, adj=adj, symbol=symb, pxMode=False,
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


class Ring(Network):
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
        symb = self.get_symbols()
        sizes = np.zeros(N)
        for ti in range(N):
            if symb[ti] == 's':
                sizes[ti] = 0.5
            elif symb[ti] == 'o':
                sizes[ti] = 0.1
            elif symb[ti] == '+':
                sizes[ti] = 0.5

        return sizes

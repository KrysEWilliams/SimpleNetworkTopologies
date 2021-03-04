import unittest
import simplenetworktopologies.networks as nw
#import pyqtgraph as pg


class NetworksTest(unittest.TestCase):

    def test_constructors(self):
        pass
        # need to initialize QApplication to avoid segfault on
        # generating networks
        #_ = pg.QtGui.QApplication(["test"])

        #nw.generic_network()

        # test that running nw.Ring(0) gives IndexError
        #self.assertRaises(IndexError, nw.Ring, 0)

        #for ti in range(1, 20):
        #    nw.Ring(ti)

        #nw.Bus()
        #nw.FullyConnected()
        #nw.Mesh()
        #nw.Star()


if __name__ == '__main__':
    unittest.main()

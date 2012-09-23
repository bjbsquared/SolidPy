from SolidPy import *
from math import tan, radians

class FHscrew(object):
    def __init__(self, size = "#6", length = 10, angle = 100):
        """
        size="#6" or "M5"
        length in mm
        angle = screwhead angle
        """
        self.size = size
        self.length = length
        if self.size == "#6":
            self.thd = inches(0.149)
            self.angle = angle
            self.cs_dia = inches(0.295)

    def hole(self):
        """
        1mm added to top and bottom for cut through
        """

        cntr_sink_ht = self.cs_dia / 2 * tan(radians(90 - self.angle / 2))

        cntr_sink = Cylinder(cntr_sink_ht, r = self.cs_dia / 2, r2 = 0.01, fs = .1)

        top = Cylinder(h = 1, r = self.cs_dia / 2, fs = 0.1)
        top.translate ([0, 0, -1])

        shank = Cylinder(h = self.length + 1, r = self.thd / 2, fs = 0.1)

        screw = top + cntr_sink + shank
        return screw
def main():

    theScrew = FHscrew(size = "#6", length = inches(1.04), angle = 100)
    junk = theScrew.hole()
    writeSCADfile('junk.scad', junk)
if __name__ == '__main__':

    main()



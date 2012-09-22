from SolidPy import *
from math import sin, cos, radians
from screw import FHscrew
from fillet import *

SolidPyObj.fs=0.1
SolidPyObj.fn = 30

base_thk=inches(0.06)
TH_dia=inches(0.45)
base_dia=inches(1.7)

TH=Cylinder(h=2*base_thk,rad=TH_dia/2,center=True)



base = Cylinder(h=base_thk, rad=base_dia/2)


theScrew = FHscrew(size="#10",length=inches(1.04),angle=100)
screw_hole = theScrew.hole()


junk = base -TH
writeSCADfile('junk.scad',junk,render=False)
def main():
    pass

if __name__ == '__main__':
    main()
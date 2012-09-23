from SolidPy import *
from math import sin, cos, radians
from screw import FHscrew
from fillet import *

Defaults.fs = 0.1
Defaults.fn = 30
Defaults.augment = False

base_dia = inches(1.30)
base_thk = inches(0.06)

post_dia = inches(0.400)
post_hgt = inches(1.04)

base_fil_rad = inches(0.4)
post_fil_rad = inches(1.0 / 16.0)

base = Cylinder(h = base_thk, r = base_dia / 2)
post = Cylinder(h = post_hgt, r = post_dia / 2)

theScrew = FHscrew(size = "#6", length = inches(1.04), angle = 100)
screw_hole = theScrew.hole()
Defaults.augList += [screw_hole]
AF = AxialFillet(post_dia / 2, base_fil_rad)
base_fillet = AF.innerFillet()
base_fillet.rotate([180, 0, 0])
base_fillet.translate([0, 0, base_thk])

CF = AxialFillet(post_dia / 2, post_fil_rad)
post_fillet = CF.outterFillet()
post_fillet.translate([0, 0, post_hgt])

junk = base + post + base_fillet - post_fillet - screw_hole
writeSCADfile('junk.scad', junk)

print "it worked"

def main():
    pass

if __name__ == '__main__':
    from datetime import datetime
    print datetime.now()
